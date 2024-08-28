from collections.abc import Callable, Iterable
from functools import partial

import numpy as np
import jax
from jax import jacfwd as jac, numpy as jnp, jit, lax

jax.config.update("jax_enable_x64", True)

# Useful: jax.debug.print


def _one_cost(mat: np.ndarray, xs: Iterable[np.ndarray]):
    """
    Get the cost given a cost matrix and a sequence of states/controls.

    Parameters
    ----------
        mat
            cost matrix
        xs
            sequence of states or controls
            shape: (number of xs, dimension of each x)
    Returns
    -------
        cost of entire sequence
    """
    return np.sum([x @ mat @ x for x in xs])


def get_costs(
    Q: np.ndarray,
    R: np.ndarray,
    M: np.ndarray,
    xs: Iterable[np.ndarray],
    us: Iterable[np.ndarray],
):
    """
    Get the cost of the sequences of states and controls.

    Parameters
    ----------
        Q
            terminal state cost matrix
        R
            control cost matrix
        M
            running state cost matrix
        xs
            states
            shape: (number of xs, dimension of each x)
        us
            controls
            shape: (number of us, dimension of each u)
    Returns
    -------
        sum of all costs
        dictionary of costs
    """
    costs = {
        "control": _one_cost(R, us),
        "running": _one_cost(Q, xs[:-1]),
        "terminal": _one_cost(M, xs[-1].reshape(1, -1)),
    }
    return sum(costs.values()), costs


class Simulator:
    def __init__(
        self,
        f: Callable[[np.ndarray, np.ndarray], np.ndarray],
        dt: float,
        n: int | None = None,
        W: np.ndarray | None = None,
        D: np.ndarray | None = None,
        H: np.ndarray | None = None,
        state_seed: int | None = 42,
        observation_seed: int | None = 17,
    ):
        """
        Evolve a system and provide observations.
        Optionally include noise in the evolution and/or the observations.

        Either n or H must be given.
        If n is given but H is not, H is set as the identity matrix of size n.
        If both n and H are given, n is ignored.

        To assume the entire true state is visible, don't specify the
        observation matrix H or the observation covariance matrix D. Then
        `observe` returns the true state.

        Parameters
        ----------
            f
                transition function
                dx/dt = f(x, u)
                x_{k+1} = x_k + Δt f(x_k, u_k)
            dt
                time step size Δt
            n
                state x_k dimension
            W
                state covariance
                x_{k+1} = x_k + Δt f(x_k, u_k) + w_k
                w_k ~ N(0, W)
            D
                observation covariance
                z_k = H @ x_k + v_k
                d_k ~ N(0, D)
            H
                observation matrix, i.e., z_k = H @ x_k
            state_seed
                the seed to use when generating noise in the state evolution. If
                None, randomly pick a seed. Ignored if W is None.
            observation_seed
                the seed to use when generating noise in the state observation.
                If None, randomly pick a seed. Ignored if D is None.
        Methods
        -------
            set_initial_state
                compute and record the (possibly noisy) initial state
            evolve
                compute and record the (possibly noisy) next state
            observe
                compute and return the (possibly noisy) observation of the
                      current true state
        Attributes
        ----------
            true_states
                the list of true states
        Raises
        ------
            ValueError
                If neither n nor H is specified.
        """
        self._f = f
        self._dt = dt
        self._n = n
        self._W, self._D = W, D

        if n is None and H is None:
            raise ValueError("either n or H must be specified")

        # If H is not specified, use the identity matrix of shape n
        # (i.e., the entire true state is visible).
        if H is None:
            H = np.eye(n)
        self._H = H

        # Dimensions of observations (m) and states (n)
        self._m, self._n = H.shape

        if W is not None and W.shape[0] != self._n:
            raise ValueError("W's dimension does not match H.shape[1]")
        if D is not None and D.shape[0] != self._m:
            raise ValueError("D's dimension does not match H.shape[0]")

        # Define noise generators.
        self._w = iter(self._w_fun(state_seed))
        self._d = iter(self._d_fun(observation_seed))

        self.true_states = list()

    def set_initial_state(self, mu0: np.ndarray):
        """
        Given the expected initial state, compute and record the true initial
        state.
        Add noise if the state covariance W was defined.

        This method deletes any states previously stored in `true_states`.

        Parameters
        ----------
            mu0
                expected initial state
        Saves
        -----
            true_states[0]
                x0, the true initial state (possibly with noise added)
        """
        self.true_states = list()
        self.true_states.append(mu0 + next(self._w))

    def evolve(self, u: np.ndarray):
        """
        Given the control u_k, compute and record the next true state x_{k+1}
        Add noise if the state covariance W was defined.

        Parameters
        ----------
            u
                control u_k
        Saves
        -----
            true_states[k+1]
                x_{k+1}, the next true (possibly noisy) state using control u_k
        """
        xk = self.true_states[-1]
        self.true_states.append(xk + self._dt * self._f(xk, u) + next(self._w))

    def observe(self) -> np.ndarray:
        """
        Compute and return the observation z_k.
        Add noise if the observation covariance D was defined.

        If H was not specified at initialization, it was set as the identity
        matrix. If D was also not specified (so that there is no observation
        noise), then this returns the true state x_k.

        Returns
        -------
            z_k
                (possibly noisy) observation
        """
        xk = self.true_states[-1]
        return self._H @ xk + next(self._d)

    def _w_fun(self, state_seed):
        """
        Return state noise if the state covariance W was defined,
        zeros otherwise.
        """
        if self._W is None:
            while True:
                yield np.zeros(self._n)
        else:
            rng = np.random.default_rng(state_seed)
            while True:
                yield rng.multivariate_normal(np.zeros(self._n), self._W)

    def _d_fun(self, observation_seed):
        """
        Return observation noise if the observation covariance D was defined,
        zeros otherwise.
        """
        if self._D is None:
            while True:
                yield np.zeros(self._m)
        else:
            rng = np.random.default_rng(observation_seed)
            while True:
                yield rng.multivariate_normal(np.zeros(self._m), self._D)


class Controller:
    def __init__(
        self,
        f: Callable[[jnp.ndarray, jnp.ndarray], jnp.ndarray],
        Q: np.ndarray,
        M: np.ndarray,
        R: np.ndarray,
        T: float,
        N: int,
        ε: float = 1e-2,
    ):
        """
        Given a transition system and cost matrices, compute an optimal
        trajectory, an associated optimal control sequence, and an optimal
        control rule given state feedback.

        Assume M, Q are (n, n) and R is (m, m).

        Source: https://homes.cs.washington.edu/~todorov/papers/TodorovACC05.pdf

        Parameters
        ----------
            f
                transition function
                dx/dt = f(x, u)
                x_{k+1} = x_k + Δt f(x_k, u_k)
            Q
                state intermediate cost matrix x_k\trp Q x_k
                positive semi-definite
            M
                state final cost matrix x_N\trp M x_N
                positive semi-definite
            R
                control cost matrix u_k\trp R u_k
                positive definite
            T
                length of time
            N
                number of steps 0, ..., N
            ε
                step size for computing optimal control update or deviation du
        Methods
        -------
            fit
                fit the controller
            compute_control
                compute the optimal control
        Attributes (available after `fit`)
        ----------
            xs
                optimal zero-noise trajectory
            us
                optimal zero-noise controls
            num_iterations
                the number of iterations for `fit` to converge
            As
                linearized dynamics, A_k = dg/dx_k
                where x_{k+1} = g(x_k, u_k)
                (dg/dx_k = I + Δt df/dx_k)
        """
        self._f = f

        # Dimensions of states (n) and controls (c)
        self._n, self._c = M.shape[0], R.shape[0]

        self._M, self._Q, self._R = M, Q, R
        self._T, self._N = T, N
        self._dt = T / N

        self._ε = ε

    def compute_control(self, k: int, x: np.ndarray) -> jnp.ndarray:
        """Compute the optimal control.

        Parameters
        ----------
            k
                current time step index [k in (0, ..., N-1)]
            x
                current state x_k
        Returns
        -------
            u_k
                optimal control
        """
        dx = x - self.xs[k]
        du = self._du(self._gs[k], np.linalg.inv(self._Hs[k]), dx, self._Gs[k])
        u = self.us[k] + du

        return u

    def fit(
        self,
        x0: np.ndarray,
        us: np.ndarray,
        max_iters: int = 5000,
        tol: float = 1e-4,
    ):
        """
        Given an initial state estimate x0 and an initial guess of controls us,
        perform iLQG until convergence of us or until a maximum number of
        iterations is reached.

        Parameters
        ----------
            x0
                initial state
                shape: (n,)
            us
                initial guess of controls [u_0, u_1, ..., u_{N-1}].T
                shape: (N, m)
            max_iters
                the maximum number of iterations of iLQG to perform
            tol
                consider the us converged when
                norm(new_us - old_us, ord=2) < tol
        Saves
        -----
            xs
                optimal zero-noise trajectory x_k for k in (0, ..., N)
                shape: (N+1, n)
            us
                optimal zero-noise controls u_k for k in (0, ..., N-1)
                shape: (N, m)
            num_iterations
                number of iterations of iLQG used while fitting
            gs, Gs, Hs, As, Bs
                values used in `compute_control`
        """
        new_us, num_iterations = self._fit(x0, us, max_iters, tol)

        # Perform one final iteration to get the latest values of xs, gs, Gs,
        # Hs, As, and Bs.
        _, (xs, gs, Gs, Hs, As, Bs) = self._iter(x0, new_us)

        # Zero-noise trajectory, controls, and other values
        self.xs, self.us = xs, new_us
        self._gs, self._Gs, self._Hs = gs, Gs, Hs
        self.As, self._Bs = As, Bs
        self.num_iterations = num_iterations

    @partial(jit, static_argnums=0)
    def _fit(
        self, x0: jnp.ndarray, us: jnp.ndarray, max_iters, tol
    ) -> tuple[jnp.ndarray, int]:
        """jitted helper method for fit."""

        def condition(args):
            """
            Return True (i.e., continue iterating) if us and new_us differ by
            more than tol and i is less than max_iters, False otherwise.
            """
            us, new_us, i = args
            diff = jnp.linalg.norm(new_us - us)
            return jnp.logical_and(diff > tol, i < max_iters)

        def iteration(args):
            """Perform an iteration of iLQG."""
            _, us, i = args
            new_us, _ = self._iter(x0, us)

            # Swap the order: new_us are now the current us.
            # `condition` will check whether us and new_us are within tolerance.
            return us, new_us, i + 1

        # Perform iLQG until convergence or reach max_iters.
        _, new_us, num_iterations = lax.while_loop(
            condition, iteration, (jnp.full_like(us, jnp.inf), us, 0)
        )

        return new_us, num_iterations

    def _iter(self, x0: jnp.ndarray, us: jnp.ndarray):
        """
        Given an initial position and guess of controls, return an updated
        sequence of controls.

        Also return other values to be saved by `fit` after the final iteration.
        """

        # Forward pass
        xs = jnp.full((self._N + 1, self._n), jnp.inf)
        xs = xs.at[0].set(x0)

        As = jnp.full((self._N + 1, self._n, self._n), jnp.inf)
        As = As.at[0].set(self._A(xs[0], us[0]))

        Bs = jnp.full((self._N + 1, self._n, self._c), jnp.inf)
        Bs = Bs.at[0].set(self._B(xs[0], us[0]))

        (xs, As, Bs), _ = lax.fori_loop(
            0, self._N, self._forward, ((xs, As, Bs), (us,))
        )

        # Backward pass
        new_us = jnp.full_like(us, jnp.inf)

        Ss = jnp.full((self._N + 1, self._n, self._n), jnp.inf)
        Ss = Ss.at[self._N].set(self._QN())

        ss = jnp.full((self._N + 1, self._n), jnp.inf)
        ss = ss.at[self._N].set(self._qN(xs[self._N]))

        gs = jnp.full((self._N, self._c), jnp.inf)
        Gs = jnp.full((self._N, self._c, self._n), jnp.inf)
        Hs = jnp.full((self._N, self._c, self._c), jnp.inf)

        (Ss, ss, new_us, gs, Gs, Hs), _ = lax.fori_loop(
            0,
            self._N,
            self._backward,
            ((Ss, ss, new_us, gs, Gs, Hs), (xs, us, As, Bs)),
        )

        return new_us, (xs, gs, Gs, Hs, As, Bs)

    def _forward(self, k: int, args):
        """Given x_k and u_k, compute x_{k+1}, A_{k+1}, and B_{k+1}."""

        # Args that are modified, args that are not modified (necessary for jit)
        (xs, As, Bs), (us,) = args

        xs = xs.at[k + 1].set(self._x(xs[k], us[k]))

        As = As.at[k + 1].set(self._A(xs[k + 1], us[k + 1]))
        Bs = Bs.at[k + 1].set(self._B(xs[k + 1], us[k + 1]))

        return (xs, As, Bs), (us,)

    def _backward(self, k: int, args):
        """
        Compute an updated control u_k and various values for an optimal
        control rule.
        """

        # Note that since we assume the matrix F multiplying the noise
        # is constant (identity), the terms with C_{i, k} are zero.
        # Similarly, the P_k terms are zero since our state intermediate cost
        # functional has a mixed dxdu derivative equal to zero.

        # Args that are modified, args that are not modified (necessary for jit)
        (Ss, ss, new_us, gs, Gs, Hs), (xs, us, As, Bs) = args

        # lax.fori_loop only allows forward iteration, so reverse the index.
        k = self._N - 1 - k

        gs = gs.at[k].set(self._g(us[k], Bs[k], ss[k + 1]))
        Gs = Gs.at[k].set(self._G(Bs[k], Ss[k + 1], As[k]))
        Hs = Hs.at[k].set(self._H(Bs[k], Ss[k + 1]))

        Hkinv = jnp.linalg.inv(Hs[k])
        Ss = Ss.at[k].set(self._S(As[k], Ss[k + 1], Gs[k], Hkinv))
        ss = ss.at[k].set(self._s(xs[k], As[k], ss[k + 1], Gs[k], Hkinv, gs[k]))

        new_us = new_us.at[k].set(us[k] + self._du(gs[k], Hkinv))

        return (Ss, ss, new_us, gs, Gs, Hs), (xs, us, As, Bs)

    """
    The below helper functions and their parameters have the following naming
    conventions to represent their return values and arguments:
        a   : a_k
        ap1 : a_{k+1}
        am1 : a_{k-1}
    """

    def _x(self, xm1, um1):
        return xm1 + self._dt * self._f(xm1, um1)

    def _du(self, g, Hinv, dx=None, G=None):
        return (
            -self._ε * Hinv @ (g + 0 if (dx is None or G is None) else G @ dx)
        )

    def _A(self, x, u):
        return np.eye(self._n) + self._dt * jac(self._f, 0)(x, u)

    def _B(self, x, u):
        return self._dt * jac(self._f, 1)(x, u)

    def _qk(self, x):
        return self._dt * 2 * x @ self._Q

    def _qN(self, x):
        return 2 * x @ self._M

    # Note Q_k is the Q defined in equation (3) of the paper, not the state
    # intermediate cost matrix stored in self._Q.
    def _Qk(self):
        return 2 * self._Q

    def _QN(self):
        return 2 * self._M

    def _r(self, u):
        return self._dt * 2 * u @ self._R

    def _R_(self):
        return self._dt * 2 * self._R

    def _g(self, u, B, sp1):
        return self._r(u) + B.T @ sp1

    def _G(self, B, Sp1, A):
        return B.T @ Sp1 @ A

    def _H(self, B, Sp1):
        return self._R_() + B.T @ Sp1 @ B

    # Note _s is the bold s in equation (7).
    def _s(self, x, A, sp1, G, Hinv, g):
        return self._qk(x) + A.T @ sp1 - G.T @ Hinv @ g

    def _S(self, A, Sp1, G, Hinv):
        return self._Qk() + A.T @ Sp1 @ A - G.T @ Hinv @ G


class Estimator:
    def __init__(
        self,
        f: Callable[[jnp.ndarray, jnp.ndarray], jnp.ndarray],
        dt: float,
        H: np.ndarray,
        W: np.ndarray,
        D: np.ndarray,
        N: int,
    ):
        """Provide state estimation using an Extended Kalman Filter.

        Parameters
        ----------
            f
                zero-noise transition function
                dx/dt = f(x, u)
                x_{k+1} = x_k + Δt f(x_k, u_k)
            dt
                time step size Δt
            H
                observation matrix, i.e., z_k = H @ x_k
            W
                state covariance
                x_{k+1} = x_k + Δt f(x_k, u_k) + w_k
                w_k ~ N(0, Q)
            D
                observation covariance
                z_k = H @ x_k + v_k
                v_k ~ N(0, R)
            N
                number of steps 0, ...., N
        Methods
        -------
            fit
                fit the Estimator
            estimate_state
                estimate the state given an observation, control, and the
                previous state
        """
        self._f, self._dt = f, dt
        self._H = H
        self._W, self._D = W, D
        self._N = N

        # Dimensions of observations (m) and states (n)
        self._m, self._n = H.shape

    def predict_state(self, x: np.ndarray, u: np.ndarray):
        """
        Given the last state estimate and the control used, return the
        prediction of the next state.

        Parameters
        ----------
            x
                the last state estimate \hat x_{k-1|k-1}
            u
                the control used u_{k-1}
        Returns
        -------
            the prediction of the next state \hat x_{k|k-1]}
        """
        pred = x + self._dt * self._f(x, u)
        return pred

    def update_state(self, k: int, pred: np.ndarray, z: np.ndarray):
        """
        Given the step k, the prediction of the current state, and an
        observation, return the updated estimate of the current state.

        Parameters
        ----------
            k
                the current step
            pred
                the current state prediction x_{k|k-1}
            z
                the current observation z_k
        Returns
        -------
            the updated estimate of the current state x_{k|k}
        """
        residual = z - self._H @ pred
        return pred + self._gains[k] @ residual

    def fit(self, As: np.ndarray):
        """
        Compute and save gain matrices given linearized dynamics along an
        expected trajectory.

        Parameters
        ----------
            As
                linearized dynamics, A_k = dg/dx_k
                where x_{k+1} = g(x_k, u_k) + w_k
                (dg/dx_k = I + Δt df/dx_k)
        """

        # S_{k|k-1} state covariance predictions
        Spreds = jnp.full((self._N + 1, self._n, self._n), jnp.inf)
        # L_{k} gains
        Ls = jnp.full((self._N + 1, self._n, self._m), jnp.inf)
        # S_{k|k} state covariance updated estimates
        Sests = jnp.full((self._N + 1, self._n, self._n), jnp.inf)

        Spreds = Spreds.at[0].set(self._W.copy())
        Ls = Ls.at[0].set(
            Spreds[0]
            @ self._H.T
            @ jnp.linalg.inv(self._H @ Spreds[0] @ self._H.T + self._D)
        )
        Sests = Spreds.at[0].set(
            (jnp.eye(self._n) - Ls[0] @ self._H) @ Spreds[0]
        )

        (_, gains, _), _ = lax.fori_loop(
            1,
            self._N + 1,
            self._fit,
            ((Spreds, Ls, Sests), (As,)),
        )

        self._gains = gains

    @partial(jit, static_argnums=0)
    def _fit(self, k: int, args):
        """jitted helper method for fit."""

        # Args that are modified, args that are not modified (necessary for jit)
        (Spreds, Ls, Sests), (As,) = args

        Spreds = Spreds.at[k].set(As[k] @ Sests[k - 1] @ As[k].T + self._W)
        Ls = Ls.at[k].set(
            Spreds[k]
            @ self._H.T
            @ jnp.linalg.inv(self._H @ Spreds[k] @ self._H.T + self._D)
        )
        Sests = Sests.at[k].set(
            (jnp.eye(self._n) - Ls[k] @ self._H) @ Spreds[k]
        )

        return (Spreds, Ls, Sests), (As,)
