# Basic Statistics Library

`lib` is a small Python package that provides basic statistical functions implemented from scratch, without any external dependencies.

---

## Features

The library includes the following functions:

- `mean(data)` – Returns the mean (average) of a list of numbers.
- `median(data)` – Returns the median value.
- `mode(data)` – Returns the mode (most frequent value) of a list.
- `variance(data)` – Returns the variance of a list of numbers.
- `ds(data)` – Returns the standard deviation of a list of numbers.

All functions raise appropriate exceptions for invalid inputs (e.g., empty lists, multiple modes, insufficient data).

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Andrea-gt/stats_ci.git
cd stats_ci
````

No external packages are required to use `lib`. For running tests, `pytest` is recommended:

```bash
pip install pytest
```

---

## Usage

```python
from lib import mean, median, mode, variance, ds

data = [1, 2, 3, 4, 5]

print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", mode([1,1,2,3]))
print("Variance:", variance(data))
print("Standard Deviation:", ds(data))
```

---

## Running Tests

The repository includes a comprehensive set of unit tests in the `tests/` folder. To run the tests:

```bash
pytest -v
```

GitHub Actions automatically runs these tests on every push or pull request to the `main` branch.

---

## Folder Structure

```
stats_ci/
├── lib/
│   ├── __init__.py
│   └── stats.py
├── tests/
│   └── test_stats.py
├── .github/
│   └── workflows/
│       └── tests.yml
└── README.md
└── pyproject.toml
```
