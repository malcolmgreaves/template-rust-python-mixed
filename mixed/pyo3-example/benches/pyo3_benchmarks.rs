use criterion::{black_box, criterion_group, criterion_main, Criterion};
use pyo3_example::{add_numbers, fibonacci, sort_numbers, Calculator};

fn benchmark_add_numbers(c: &mut Criterion) {
    c.bench_function("pyo3 add_numbers", |b| {
        b.iter(|| add_numbers(black_box(100), black_box(200)))
    });
}

fn benchmark_fibonacci(c: &mut Criterion) {
    c.bench_function("pyo3 fibonacci 20", |b| {
        b.iter(|| fibonacci(black_box(20)))
    });
}

fn benchmark_sort_numbers(c: &mut Criterion) {
    c.bench_function("pyo3 sort 1000 numbers", |b| {
        b.iter(|| {
            let numbers: Vec<i32> = (0..1000).rev().collect();
            sort_numbers(black_box(numbers))
        })
    });
}

fn benchmark_calculator(c: &mut Criterion) {
    c.bench_function("pyo3 calculator operations", |b| {
        b.iter(|| {
            let mut calc = Calculator::new(black_box(0));
            for i in 0..100 {
                calc.add(black_box(i));
            }
            calc.get_value()
        })
    });
}

criterion_group!(
    benches,
    benchmark_add_numbers,
    benchmark_fibonacci,
    benchmark_sort_numbers,
    benchmark_calculator
);
criterion_main!(benches);
