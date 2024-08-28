"""Unit testing file for Gaussian Quadrature"""
import gaussian_quadrature
import numpy as np
import pytest


def test_init():
    # Test correct storage of attributes
    gauss1 = gaussian_quadrature.GaussianQuadrature(20, 'legendre')
    gauss2 = gaussian_quadrature.GaussianQuadrature(5, 'chebyshev')

    assert (gauss1.ptype == 'legendre'), "Polytype not stored"
    assert (gauss2.ptype == 'chebyshev'), "Polytype not stored"

    # Test the respective weight functions
    input_value = 0.25
    assert (gauss1.w_inv(input_value) == 1)
    assert (gauss2.w_inv(input_value) == np.sqrt(1-input_value**2))

    # Test giving invalid polytype
    with pytest.raises(ValueError):
        gaussian_quadrature.GaussianQuadrature(1, 'Legendre')

    with pytest.raises(ValueError):
        gaussian_quadrature.GaussianQuadrature(20, 'invalid')


def test_point_weights():
    # Write unit tests for testing the point_weights function
    raise NotImplementedError()
