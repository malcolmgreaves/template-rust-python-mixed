"""Unit tests for PyO3 functions."""

from pyo3_example import add_numbers, fibonacci, sort_numbers


def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 20) == 30


def test_add_zero():
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 5) == 5


def test_add_large_numbers():
    assert add_numbers(100, 200) == 300
    assert add_numbers(1000, 2000) == 3000


def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_small_numbers():
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610


def test_fibonacci_sequence():
    """Test that fibonacci follows the correct sequence."""
    fib_sequence = [fibonacci(i) for i in range(10)]
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib_sequence == expected


def test_sort_unsorted_list():
    assert sort_numbers([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
    assert sort_numbers([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_sort_already_sorted():
    assert sort_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_sort_reverse_sorted():
    assert sort_numbers([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_sort_empty_list():
    assert sort_numbers([]) == []


def test_sort_single_element():
    assert sort_numbers([42]) == [42]


def test_sort_duplicates():
    assert sort_numbers([3, 3, 1, 2, 2]) == [1, 2, 2, 3, 3]


def test_sort_negative_numbers():
    assert sort_numbers([-5, -2, -8, -1]) == [-8, -5, -2, -1]
    assert sort_numbers([-3, 0, 3, -1, 1]) == [-3, -1, 0, 1, 3]
