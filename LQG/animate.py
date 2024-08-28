from collections.abc import Callable

from matplotlib import pyplot as plt, animation
import numpy as np


# Shuttle, earth, moon, target
colors = {
    "shuttle": "green",
    "earth": "blue",
    "moon": "gray",
    "target": "orange",
    "control": "red",
}


def animate2d(
    filename: str,
    xs: list | np.ndarray,
    us: list | np.ndarray,
    position_earth: np.ndarray,
    position_moon: np.ndarray,
    position_target: np.ndarray,
    acceleration_earth: Callable[[np.ndarray], np.ndarray],
    acceleration_moon: Callable[[np.ndarray], np.ndarray],
    fit_data: bool = False,
    skip: int = 10,
):
    """Animate the rescue mission in 2D.

    Plot on the xy-plane, though note that z-coordinates are still expected in
    the parameters (i.e., three dimensions are expected).

    Params:
        filename : the name to give the saved animation (include the .mp4 file extension)
        xs : the shuttle states with shape
             (num_steps, 6 [3 spatial components and 3 velocity components])
        us : the shuttle controls with shape
             (num_steps, 3 [3 acceleration components])
        position_earth : shape (3,)
        position_moon : shape (3,)
        position_target : shape (3,)
        acceleration_earth : acceleration of shuttle due to earth's gravity
            should accept shuttle position as argument and return acceleration
        acceleration_moon : acceleration of shuttle due to moon's gravity
            should accept shuttle position as argument and return acceleration
        fit_data : if true, fit the bounding box to the data,
                   otherwise use default values that should show a successful
                   mission using the positions given in the lab
        skip : the number of steps to skip between animation frames
    """
    if isinstance(xs, list):
        xs = np.array(xs)
    if isinstance(us, list):
        us = np.array(us)

    # Add a row of zeros, corresponding to zero control input on the last
    # time step.
    us = np.concatenate((us, [np.zeros_like(us[0])]))

    if fit_data:
        data_lims = np.array([(min(coord), max(coord)) for coord in xs.T[:2]])
        xlim, ylim = data_lims
    else:
        xlim = (-300_000, 50_000)
        ylim = (-600_000, 50_000)

    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    @np.vectorize
    def accleration_log_magnitude(x, y):
        """Return the magnitude of the accleration due to the combined gravity
        of the earth and moon.
        """
        p = np.array([x, y, 0])
        return np.log1p(
            np.linalg.norm(acceleration_moon(p) + acceleration_earth(p))
        )

    # Compute meshgrid of the acceleration due to gravity of the earth and moon.
    n = 100
    xls = np.linspace(*xlim, n)
    yls = np.linspace(*ylim, n)
    X, Y = np.meshgrid(xls, yls)
    Z = accleration_log_magnitude(X, Y)

    # Plot the acceleration due to gravity of the earth and moon.
    contour = ax.contourf(X, Y, Z, levels=200, cmap="viridis_r")
    plt.colorbar(contour)

    earth = ax.scatter(*position_earth[:2], color=colors["earth"])
    moon = ax.scatter(*position_moon[:2], color=colors["moon"])
    target = ax.scatter(*position_target[:2], color=colors["target"])

    # The shuttle's position, path, and control direction and relative magnitude
    point = ax.plot([], [], "o", color=colors["shuttle"])[0]
    line = ax.plot([], [], color=colors["shuttle"])[0]
    arrow = ax.quiver(
        *xs[0, :2],
        *us[0, :2],
        color=colors["control"],
        angles="xy",
        scale_units="xy",
        scale=0.01,
    )

    ax.legend(
        [earth, moon, target, point],
        ["Earth", "Moon", "Target", "Shuttle"],
        loc="upper left",
    )
    ax.set_aspect("equal")

    def update(i):
        line.set_data(*xs[:i, :2].T)
        point.set_data(*xs[i, :2])

        arrow.set_offsets(xs[i, :2])
        arrow.set_UVC(*us[i, :2])

    idx = np.arange(len(xs), step=skip)
    ani = animation.FuncAnimation(fig, update, frames=idx, interval=10 * skip)
    ani.save(filename)
    plt.close()


def animate3d(
    filename: str,
    xs: list | np.ndarray,
    us: list | np.ndarray,
    position_earth: np.ndarray,
    position_moon: np.ndarray,
    position_target: np.ndarray,
    fit_data: bool = False,
    skip: int = 10,
):
    """Animate the rescue mission in 3D.

    Params:
        filename : the name to give the saved animation (include the .mp4 file extension)
        xs : the shuttle states with shape
             (num_steps, 6 [3 spatial components and 3 velocity components])
        us : the shuttle controls with shape
             (num_steps, 3 [3 acceleration components])
        position_earth : shape (3,)
        position_moon : shape (3,)
        position_target : shape (3,)
        fit_data : if true, fit the bounding box to the data,
                   otherwise use default values that should show a successful
                   mission using the positions given in the lab
        skip : the number of steps to skip between animation frames
    """
    if isinstance(xs, list):
        xs = np.array(xs)
    if isinstance(us, list):
        us = np.array(us)

    # Add a row of zeros, corresponding to zero control input on the last
    # time step.
    us = np.concatenate((us, [np.zeros_like(us[0])]))

    if fit_data:
        data_lims = np.array([(min(coord), max(coord)) for coord in xs.T[:3]])
        xlim, ylim, zlim = data_lims
    else:
        xlim = (-150_000, 1_000)
        ylim = (-600_000, 1_000)
        zlim = (-100, 100)

    fig, ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"})
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)

    earth = ax.scatter3D(*position_earth, color=colors["earth"])
    moon = ax.scatter3D(*position_moon, color=colors["moon"])
    target = ax.scatter3D(*position_target, color=colors["target"])

    # The shuttle's position, path, and control direction and relative magnitude
    point = ax.plot([], [], [], "o", color=colors["shuttle"])[0]
    line = ax.plot([], [], [], color=colors["shuttle"])[0]
    arrow = ax.quiver([], [], [], [], [], [], color=colors["control"])

    ax.legend(
        [earth, moon, target, point],
        ["Earth", "Moon", "Target", "Shuttle"],
        loc="upper left",
    )
    ax.set_aspect("equalxy")

    # Scale the control vector
    length = 100

    def update3d(i):
        line.set_data_3d(*xs[:i, :3].T)
        point.set_data_3d(*xs[i, :3])
        arrow.set_segments([[xs[i, :3], xs[i, :3] + us[i] * length]])

    idx = np.arange(len(xs), step=skip)
    ani = animation.FuncAnimation(fig, update3d, frames=idx, interval=10 * skip)
    ani.save(filename)
    plt.close()
