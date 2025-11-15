"""Benchmark tests for PyO3 functions."""

import pytest
from pyo3_example import add_numbers, fibonacci, sort_numbers, Calculator


@pytest.mark.benchmark
def test_benchmark_add_numbers(benchmark):
    """Benchmark add_numbers function."""
    result = benchmark(add_numbers, 100, 200)
    assert result == 300


@pytest.mark.benchmark
def test_benchmark_fibonacci_10(benchmark):
    """Benchmark fibonacci with n=10."""
    result = benchmark(fibonacci, 10)
    assert result == 55


@pytest.mark.benchmark
def test_benchmark_fibonacci_20(benchmark):
    """Benchmark fibonacci with n=20."""
    result = benchmark(fibonacci, 20)
    assert result == 6765


@pytest.mark.benchmark
def test_benchmark_sort_small_list(benchmark):
    """Benchmark sorting a small list."""

    def sort_small():
        return sort_numbers([5, 2, 8, 1, 9, 3, 7, 4, 6])

    result = benchmark(sort_small)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.benchmark
def test_benchmark_sort_large_list(benchmark):
    """Benchmark sorting a large list."""

    def sort_large():
        numbers = list(range(1000, 0, -1))
        return sort_numbers(numbers)

    result = benchmark(sort_large)
    assert len(result) == 1000
    assert result[0] == 1
    assert result[-1] == 1000


@pytest.mark.benchmark
def test_benchmark_calculator_operations(benchmark):
    """Benchmark Calculator operations."""

    def calc_ops():
        calc = Calculator(0)
        for i in range(100):
            calc.add(i)
        return calc.get_value()

    result = benchmark(calc_ops)
    assert result == sum(range(100))


@pytest.mark.benchmark
def test_benchmark_calculator_single_add(benchmark):
    """Benchmark single Calculator add operation."""
    calc = Calculator(10)
    result = benchmark(calc.add, 5)
    # Note: calculator state persists, so value keeps increasing
    assert result >= 15
