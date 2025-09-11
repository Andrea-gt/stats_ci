"""
Unit tests for py

This test suite validates the behavior of all statistical functions:
- mean
- median
- mode
- variance
- ds (standard deviation)

Tests:
1. Two "happy path" tests per function
   (valid inputs → expected result).
2. One "edge/error case" per function
   (invalid input → exception).
"""

import pytest
from lib import mean, median, mode, variance, ds

# =====================================================
# mean()
# =====================================================

def test_mean():
    # Mean of odd and even sized lists.
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([10, 20]) == 15 # 15


def test_mean_edge():
    #Error case: mean of empty list should raise ValueError.
    with pytest.raises(ValueError):
        mean([])

# =====================================================
# median()
# =====================================================

def test_median():
    # Median of odd and even sized lists.
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5


def test_median_edge():
    # Error case: median of empty list should raise ValueError.
    with pytest.raises(ValueError):
        median([])

# =====================================================
# mode()
# =====================================================

def test_mode():
    # Mode with one clear most frequent value.
    assert mode([1, 1, 2, 3]) == 1
    assert mode([5, 5, 5, 6, 7]) == 5


def test_mode_edge():
    # Empty list and multiple modes should raise ValueError.
    with pytest.raises(ValueError):
        mode([])

    with pytest.raises(ValueError):
        mode([1, 1, 2, 2])

# =====================================================
# variance()
# =====================================================

def test_variance():
    # Variance of a spread-out list and a constant list.
    assert round(variance([1, 2, 3, 4, 5]), 2) == 2.5
    assert round(variance([10, 10, 10, 10]), 2) == 0


def test_variance_edge():
    # Variance requires at least 2 data points.
    with pytest.raises(ValueError):
        variance([42])

# =====================================================
# ds() - standard deviation
# =====================================================

def test_ds():
    # Standard deviation of spread-out list and constant list.
    assert round(ds([1, 2, 3, 4, 5]), 2) == 1.58
    assert ds([10, 10, 10, 10]) == pytest.approx(0, abs=1e-6)

def test_ds_edge():
    # Standard deviation requires at least 2 data points.
    with pytest.raises(ValueError):
        ds([99])