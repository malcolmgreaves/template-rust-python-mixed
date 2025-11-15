use pyo3::prelude::*;

/// Example function that uses the local fictional-project crate
#[pyfunction]
pub fn add_numbers(a: u64, b: u64) -> PyResult<u64> {
    // Using the add function from the local fictional-project crate
    Ok(fictional_project::add(a, b))
}

/// Example function that calculates fibonacci using fictional-project
#[pyfunction]
pub fn fibonacci(n: u64) -> PyResult<u64> {
    // Using the fibonacci function from the local fictional-project crate
    Ok(fictional_project::fibonacci(n))
}

/// Example function that sorts numbers using fictional-project
#[pyfunction]
pub fn sort_numbers(numbers: Vec<i32>) -> PyResult<Vec<i32>> {
    // Using the sort_numbers function from the local fictional-project crate
    Ok(fictional_project::sort_numbers(numbers))
}

/// Example PyO3 class
#[pyclass]
pub struct Calculator {
    value: u64,
}

#[pymethods]
impl Calculator {
    #[new]
    pub fn new(initial: u64) -> Self {
        Calculator { value: initial }
    }

    pub fn add(&mut self, other: u64) -> u64 {
        self.value = fictional_project::add(self.value, other);
        self.value
    }

    pub fn get_value(&self) -> u64 {
        self.value
    }

    fn __repr__(&self) -> String {
        format!("Calculator(value={})", self.value)
    }
}

/// PyO3 module definition
#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    m.add_function(wrap_pyfunction!(sort_numbers, m)?)?;
    m.add_class::<Calculator>()?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_numbers() {
        assert_eq!(add_numbers(2, 3).unwrap(), 5);
        assert_eq!(add_numbers(0, 0).unwrap(), 0);
        assert_eq!(add_numbers(100, 200).unwrap(), 300);
    }

    #[test]
    fn test_fibonacci() {
        assert_eq!(fibonacci(0).unwrap(), 0);
        assert_eq!(fibonacci(1).unwrap(), 1);
        assert_eq!(fibonacci(10).unwrap(), 55);
        assert_eq!(fibonacci(15).unwrap(), 610);
    }

    #[test]
    fn test_sort_numbers() {
        let input = vec![5, 2, 8, 1, 9];
        let expected = vec![1, 2, 5, 8, 9];
        assert_eq!(sort_numbers(input).unwrap(), expected);

        let input = vec![1, 2, 3];
        assert_eq!(sort_numbers(input.clone()).unwrap(), input);

        let input: Vec<i32> = vec![];
        assert_eq!(sort_numbers(input.clone()).unwrap(), input);
    }

    #[test]
    fn test_calculator_new() {
        let calc = Calculator::new(42);
        assert_eq!(calc.get_value(), 42);
    }

    #[test]
    fn test_calculator_add() {
        let mut calc = Calculator::new(10);
        assert_eq!(calc.add(5), 15);
        assert_eq!(calc.get_value(), 15);
        assert_eq!(calc.add(10), 25);
        assert_eq!(calc.get_value(), 25);
    }

    #[test]
    fn test_calculator_repr() {
        let calc = Calculator::new(42);
        assert_eq!(calc.__repr__(), "Calculator(value=42)");
    }
}
