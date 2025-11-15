# PyO3 Example

This package demonstrates PyO3 integration between Rust and Python.

## Features

- Exposes Rust functions to Python via PyO3
- Uses local Rust crate `anchor-stream`
- Uses local Python package `anchor-stream`
- Demonstrates both functions and classes

## Building

```bash
# From repository root
just build

# Or directly with maturin
cd mixed/pyo3-example
maturin develop
```

## Usage

```python
from pyo3_example import add_numbers, fibonacci, sort_numbers, Calculator, demo

# Use Rust functions
result = add_numbers(10, 20)
fib = fibonacci(15)
sorted_list = sort_numbers([5, 2, 8, 1])

# Use Calculator class
calc = Calculator(10)
calc.add(5)
print(calc.get_value())

# Run demo
demo()
```
