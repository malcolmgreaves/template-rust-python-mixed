clean:
  cargo clean
  cd rust/ && \
    for d in */; do \
      (cd "$d" && cargo clean); \
    done
  cd mixed/ && \
    for d in */; do \
      (cd "$d" && cargo clean); \
    done
  find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
  find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
  find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
  find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
  find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
  find . -type f -name "*.pyc" -delete 2>/dev/null || true
  find . -type f -name "*.pyo" -delete 2>/dev/null || true
  find . -type f -name "*.so" -delete 2>/dev/null || true
  find . -type f -name "*.pyd" -delete 2>/dev/null || true
  find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
  echo "Build artifacts cleaned!"

check:
  cargo check --all-targets --workspace
  cargo check --manifest-path mixed/pyo3-example/Cargo.toml
  uv run ruff check . && uv run ty check .

build:
  cargo build
  uv sync
  cd mixed/pyo3-example && uv run maturin develop

test:
  cargo install cargo-llvm-cov || true
  cargo llvm-cov --all-targets --workspace --html
  uv run pytest -v -m "not benchmark" --cov=fictional_project --cov-report=html --cov-report=term

release:
  cargo build --release --all-targets --workspace
  cd python/ && \
    for d in */; do \
      (cd "$d" && uv build); \
    done
  cd mixed/ && \
    for d in */; do \
      (cd "$d" && uv run maturin build --release); \
    done

bench:
  cargo bench --all-targets --workspace
  uv run pytest -v -m benchmark --benchmark-only

fmt:
  cargo fmt --all
  uv run ruff format

tidy:
  cargo install cargo-machete || true
  cargo machete --with-metadata
  cargo clippy --all-targets --workspace --fix

ci: tidy check test bench
  echo "Success!"
