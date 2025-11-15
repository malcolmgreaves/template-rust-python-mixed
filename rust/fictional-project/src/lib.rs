pub fn add(left: u64, right: u64) -> u64 {
    left + right
}

/// Example function to benchmark: computes fibonacci number recursively
pub fn fibonacci(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}

/// Example function to benchmark: sorts a vector
pub fn sort_numbers(mut numbers: Vec<i32>) -> Vec<i32> {
    numbers.sort_unstable();
    numbers
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn test_fibonacci() {
        assert_eq!(fibonacci(0), 0);
        assert_eq!(fibonacci(1), 1);
        assert_eq!(fibonacci(10), 55);
        assert_eq!(fibonacci(15), 610);
    }

    #[test]
    fn test_sort_numbers() {
        let numbers = vec![5, 2, 8, 1, 9];
        let sorted = sort_numbers(numbers);
        assert_eq!(sorted, vec![1, 2, 5, 8, 9]);
    }
}
