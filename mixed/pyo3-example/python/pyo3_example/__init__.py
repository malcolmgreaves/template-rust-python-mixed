"""
PyO3 Example Package

This package demonstrates:
- Rust functions exposed to Python via PyO3
- Using local Rust crates (fictional-project)
- Using local Python packages (fictional-project)
"""

# Import Rust functions from the compiled extension
from pyo3_example._core import add_numbers, fibonacci, sort_numbers, Calculator  # type: ignore

# Import from the local Python fictional-project package
try:
    from fictional_project.main import main as py_main
except ImportError:
    py_main = None  # type: ignore


def demo():
    """Demonstrate PyO3 functionality."""
    print("=== PyO3 Example Demo ===")
    print()

    # Use Rust functions
    print("1. Add numbers (from Rust):", add_numbers(10, 32))
    print("2. Fibonacci(15) (from Rust):", fibonacci(15))
    print("3. Sort numbers (from Rust):", sort_numbers([5, 2, 8, 1, 9]))
    print()

    # Use Calculator class
    calc = Calculator(10)
    print("4. Calculator demo:")
    print(f"   Initial: {calc}")
    calc.add(5)
    print(f"   After add(5): {calc}")
    print(f"   Value: {calc.get_value()}")
    print()

    # Use Python package if available
    if py_main:  # type: ignore
        print("5. Calling Python fictional-project package:")
        py_main()


__all__ = [
    "add_numbers",
    "fibonacci",
    "sort_numbers",
    "Calculator",
    "demo",
]
