"""
lib

This package exposes all functions from stats.py directly,
so they can be imported.
"""

from .stats import mean, median, mode, variance, ds

__all__ = ["mean", "median", "mode", "variance", "ds"]