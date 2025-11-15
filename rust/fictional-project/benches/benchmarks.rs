use criterion::{Criterion, black_box, criterion_group, criterion_main};
use fictional_project::{fibonacci, sort_numbers};

fn fibonacci_benchmark(c: &mut Criterion) {
    c.bench_function("fibonacci 20", |b| b.iter(|| fibonacci(black_box(20))));
}

fn sort_benchmark(c: &mut Criterion) {
    c.bench_function("sort 1000 numbers", |b| {
        b.iter(|| {
            let numbers: Vec<i32> = (0..1000).rev().collect();
            sort_numbers(black_box(numbers))
        })
    });
}

fn sort_already_sorted_benchmark(c: &mut Criterion) {
    c.bench_function("sort already sorted 1000 numbers", |b| {
        b.iter(|| {
            let numbers: Vec<i32> = (0..1000).collect();
            sort_numbers(black_box(numbers))
        })
    });
}

criterion_group!(
    benches,
    fibonacci_benchmark,
    sort_benchmark,
    sort_already_sorted_benchmark
);
criterion_main!(benches);
