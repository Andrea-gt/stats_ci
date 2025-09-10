"""
stats.py

A small library that implements basic statistical functions:
- mean
- median
- mode
- variance
- standard deviation (c)

Universidad del Valle de Guatemala
Sept. 10 2025
"""

from typing import List
from collections import Counter

def mean(data: List[float]) -> float:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        data (List[float]): A list of numerical values.

    Returns:
        float: The mean of the input numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("mean() requires at least one data point.")

    total = 0
    count = 0
    for x in data:
        total += x
        count += 1

    return total / count


def median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[float]): A list of numerical values.

    Returns:
        float: The median value.

    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("median() requires at least one data point.")

    sorted_ = sorted(data)
    n = len(sorted_)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_[mid - 1] + sorted_[mid]) / 2
    else:
        return sorted_[mid]


def mode(data: List[float]) -> float:
    """
    Calculate the mode of a list of numbers.

    Args:
        data (List[float]): A list of numerical values.

    Returns:
        float: The most common value.

    Raises:
        ValueError: If the input list is empty or if there are multiple modes.
    """
    if not data:
        raise ValueError("mode() requires at least one data point.")

    counts = Counter(data)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]

    if len(modes) > 1:
        raise ValueError("mode() is undefined when multiple modes exist.")
    return modes[0]


def variance(data: List[float]) -> float:
    """
    Calculate the variance of a list of numbers.

    Args:
        data (List[float]): A list of numerical values.

    Returns:
        float: The variance of the input numbers.

    Raises:
        ValueError: If the input list has fewer than 2 elements.
    """
    n = len(data)
    if n < 2:
        raise ValueError("variance() requires at least two data points.")

    m = mean(data)
    squared_diffs = 0

    for x in data:
        squared_diffs += (x - m) ** 2

    return squared_diffs / (n - 1)


def ds(data: List[float]) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[float]): A list of numerical values.

    Returns:
        float: The standard deviation of the input numbers.

    Raises:
        ValueError: If the input list has fewer than 2 elements.
    """
    var = variance(data)

    # Manual square root (Newton's method)
    guess = var / 2 if var > 1 else 1
    for _ in range(20):  # iterate for precision
        guess = (guess + var / guess) / 2

    return guess