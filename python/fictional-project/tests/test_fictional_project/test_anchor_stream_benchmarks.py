import pytest


def fibonacci(n: int) -> int:
    """Example function to benchmark."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@pytest.mark.benchmark
def test_fibonacci_benchmark(benchmark):
    """Example benchmark test for fibonacci function."""
    # benchmark(function, *args, **kwargs)
    result = benchmark(fibonacci, 15)
    assert result == 610


@pytest.mark.benchmark
def test_list_comprehension_benchmark(benchmark):
    """Benchmark list comprehension vs map."""

    def list_comp():
        return [x * 2 for x in range(10000)]

    result = benchmark(list_comp)
    assert len(result) == 10000
