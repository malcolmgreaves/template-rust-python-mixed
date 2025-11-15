"""Unit tests for Calculator class."""

from pyo3_example import Calculator


def test_calculator_new():
    """Test Calculator initialization."""
    calc = Calculator(42)
    assert calc.get_value() == 42

    calc = Calculator(0)
    assert calc.get_value() == 0


def test_calculator_add():
    """Test Calculator add method."""
    calc = Calculator(10)
    result = calc.add(5)
    assert result == 15
    assert calc.get_value() == 15


def test_calculator_add_multiple():
    """Test multiple add operations."""
    calc = Calculator(0)
    calc.add(5)
    calc.add(10)
    calc.add(15)
    assert calc.get_value() == 30


def test_calculator_add_zero():
    """Test adding zero."""
    calc = Calculator(42)
    result = calc.add(0)
    assert result == 42
    assert calc.get_value() == 42


def test_calculator_repr():
    """Test Calculator string representation."""
    calc = Calculator(42)
    assert repr(calc) == "Calculator(value=42)"

    calc = Calculator(0)
    assert repr(calc) == "Calculator(value=0)"


def test_calculator_chaining():
    """Test that we can chain operations."""
    calc = Calculator(10)
    calc.add(5)
    calc.add(10)
    calc.add(20)
    assert calc.get_value() == 45


def test_calculator_large_numbers():
    """Test with large numbers."""
    calc = Calculator(1000000)
    calc.add(2000000)
    assert calc.get_value() == 3000000
