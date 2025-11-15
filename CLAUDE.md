# CLAUDE.md

This file helps Claude Code and other AI assistants understand the anchor-stream project structure, conventions, and workflows.

## Project Overview

**anchor-stream**: "Anchor your stream in our safe harbor."

A content moderation system designed to eliminate toxic commenters and keep streaming communities thriving. Currently in R&D phase with data exploration, MVP development, and application planning.

## Project Structure

This is a **polyglot monorepo** with three main components:

```
anchor-stream/
├── python/          # Pure Python packages
│   └── anchor-stream/  # ML/data exploration package
├── rust/            # Pure Rust crates
│   └── anchor-stream/  # Web server (Axum, SQLx)
└── mixed/           # Python-Rust hybrid packages
    └── pyo3-example/   # PyO3 integration example
```

### Technology Stack

**Python Side:**
- Python 3.14+
- Package manager: `uv`
- Key dependencies: PyTorch, Polars, Pydantic, HuggingFace
- Linting/formatting: Ruff
- Type checking: `ty`
- Testing: pytest with coverage and benchmarking

**Rust Side:**
- Edition: 2024
- Key dependencies: Axum, Hyper, SQLx, Tokio
- Testing: cargo-llvm-cov for coverage
- Benchmarking: Criterion

**Mixed (PyO3):**
- Build tool: `maturin`
- Allows calling Rust code from Python
- Must be built separately from pure Rust crates

## Build System

### Just Commands

This project uses `just` as a command runner. Key commands:

```bash
just check     # Type check all code (Rust + Python)
just build     # Build everything
just test      # Run tests with coverage
just bench     # Run benchmarks
just fmt       # Format all code
just tidy      # Run linters and auto-fixes
just release   # Build release artifacts
just ci        # Run full CI pipeline locally
```

### Important Build Notes

1. **PyO3 packages** (in `mixed/`) are excluded from the main Cargo workspace
   - They MUST be built with `maturin`, not `cargo build`
   - Use `maturin develop` for development builds
   - Use `maturin build --release` for release builds

2. **Python packages** use `uv` for dependency management
   - Run `uv sync` to install dependencies
   - Virtual environment is in `.venv/`

3. **Rust workspace** only includes crates in `rust/`
   - Uses Cargo workspace resolver 2
   - Shared workspace metadata in root `Cargo.toml`

## Development Workflow

### Pre-commit Hooks

The project uses pre-commit hooks (`.pre-commit-config.yaml`) that run:
- **Python**: ruff check, ruff format, ty type checking
- **Rust**: cargo check, cargo fmt

These run automatically on git commit. Run manually with `pre-commit run --all-files`.

### Code Quality Standards

**Python:**
- Linting: Ruff (configured for fix mode)
- Formatting: Ruff
- Type checking: `ty` (enforced)
- Import sorting: Part of Ruff

**Rust:**
- Formatting: `cargo fmt`
- Linting: `cargo clippy --fix`
- Unused dependencies: `cargo machete`
- Type checking: `cargo check --all-targets`

### Testing

**Python:**
```bash
# Run non-benchmark tests with coverage
uv run pytest -v -m "not benchmark" --cov=anchor_stream --cov-report=html --cov-report=term

# Run benchmarks only
uv run pytest -v -m benchmark --benchmark-only
```

**Rust:**
```bash
# Run tests with coverage
cargo llvm-cov --all-targets --workspace --html

# Run benchmarks
cargo bench --all-targets --workspace
```

## File Organization

### Python Packages
- Each package in `python/` has its own `pyproject.toml` and `uv.lock`
- Source code in `src/` subdirectory
- Tests in `tests/` subdirectory
- Package naming: use underscores for module names (e.g., `anchor_stream`)

### Rust Crates
- Each crate in `rust/` has its own `Cargo.toml` and `Cargo.lock`
- Source code in `src/` subdirectory
- Benchmarks in `benches/` subdirectory
- Uses Rust 2024 edition

### Mixed Packages
- PyO3 packages in `mixed/` have both `Cargo.toml` and `pyproject.toml`
- Rust source in `src/`, Python source in `python/`
- Tests for both languages in `tests/`

## Conventions

### Naming
- **Python**: snake_case for modules, functions, variables
- **Rust**: snake_case for functions/variables, PascalCase for types
- **Git commits**: Descriptive commit messages (see git log for style)

### Dependencies
- **Python**: Add to `pyproject.toml`, run `uv sync`
- **Rust workspace**: Consider adding to `[workspace.dependencies]` if shared
- **Rust local**: Add directly to crate's `Cargo.toml`

### Versioning
- All packages currently at version 0.1.0
- Workspace version defined in root `Cargo.toml`
- Licensed under Mozilla Public License Version 2.0

## Coding Style Guidelines

### General Principles

**Functional Programming First:**
- Use a functional programming style as much as possible
- When solutions must be mutable, encapsulate their mutability to maintain a functional interface
- When an abstraction is naturally mutable, use that instead of forcing immutability
- **Default to immutability everywhere**
- Consider mutability for performance/memory optimization, but avoid unnecessary copies
- Strive for fast, efficient code

**Simplicity Over Abstraction:**
- Prefer simpler solutions and code structures
- **Avoid object-oriented programming styles** as a general principle
- Only use OOP as a niche tool when the problem and solution are best modeled as objects
- Almost always, a struct/dataclass + function will be clearer, more direct, easier to test, and easier to understand & maintain
- Prefer direct code instead of over-abstracting
- Better to have some repeated code than an overly complex or overly strict abstraction
- Only make abstractions when they enable code reuse OR when the abstraction is fundamental to the concept being implemented

### Rust-Specific Guidelines

**Lifetime and Error Handling:**
- Try to use lifetimes effectively
- If lifetimes become too complex with `async` code, use an `Arc`
- Make descriptive `enum Error` types to encode custom error logic of a crate/module
- **Strongly prefer using `Result` whenever something could go wrong**
- **Strongly prefer using `?` on a `Result` instead of using `.unwrap()`**
- `.unwrap()` is acceptable in tests

**Traits and Abstractions:**
- Only make a `trait` if there is more than one implementation
- Otherwise, prefer functions and structs with `impl` blocks

### Python-Specific Guidelines

**Testing:**
- **NEVER use `class` to contain test functions**
- **ALWAYS use top-level functions for test functions**
- Use `@pytest.mark.parameterize` for table-oriented test design
- Use `@pytest.fixture` to create resources/shared state that tests require
- Tightly scope fixtures to avoid unnecessary dependencies

**Code Organization:**
- **Avoid using `class`es for code organization**
- Use separate Python modules (`.py` files) for organization instead
- Prefer bare functions with parameters
- Make an `@dataclass`-decorated `class` when needing to group data together
- Or make a `pydantic.BaseModel` class for data with validation
- If needing to use a `dict` that has structure, make a `TypedDict` class to describe it

## Common Tasks

### Adding a New Python Package
1. Create directory under `python/new-package/`
2. Add `pyproject.toml` with build-system and dependencies
3. Update workspace in root `pyproject.toml`
4. Run `uv sync`

### Adding a New Rust Crate
1. Create directory under `rust/new-crate/`
2. Add to `members` list in root `Cargo.toml`
3. Create `Cargo.toml` with workspace.package inheritance
4. Run `cargo check`

### Adding a New PyO3 Package
1. Create directory under `mixed/new-package/`
2. Create both `Cargo.toml` (with `pyo3` dependency) and `pyproject.toml`
3. Add to `exclude` list in root `Cargo.toml`
4. Add to workspace in root `pyproject.toml`
5. Build with `maturin develop`

## CI/CD

The `just ci` command runs the full pipeline:
1. `just tidy` - Clean up code and fix lints
2. `just check` - Type check everything
3. `just test` - Run all tests with coverage
4. `just bench` - Run all benchmarks

## Important Files

- `justfile` - Task runner configuration
- `.pre-commit-config.yaml` - Pre-commit hook configuration
- `.github/workflows/ci.yml` - GitHub Actions CI workflow
- `Cargo.toml` (root) - Rust workspace configuration
- `pyproject.toml` (root) - Python workspace configuration
- `uv.lock` - Python dependency lock file
- `Cargo.lock` - Rust dependency lock file

## CI/CD

The project uses GitHub Actions for continuous integration:
- **Workflow**: `.github/workflows/ci.yml`
- **Triggers**: Push to `main` and all pull requests
- **Pipeline**: Runs `just ci` (tidy → check → test → bench)
- **Caching**: Automatic caching for Rust (via `rust-cache`) and Python (via `uv` cache)
- **Artifacts**: Coverage reports uploaded for both Rust and Python (retained for 30 days)

## When Making Changes

1. **Always run** `just check` before committing
2. **Format code** with `just fmt`
3. **Run tests** with `just test` to ensure nothing breaks
4. **For PyO3 changes**, rebuild with `maturin develop` to test
5. **Pre-commit hooks** will run automatically, but you can run them manually

## Notes for AI Assistants

- When adding dependencies, always update the appropriate `pyproject.toml` or `Cargo.toml`
- PyO3 packages cannot be built with standard `cargo build` - use `maturin`
- The project uses bleeding-edge versions (Rust 2024 edition, Python 3.14+)
- Both Python and Rust code should pass type checking
- Use `just` commands rather than raw cargo/uv commands when possible
- The project separates pure Python, pure Rust, and mixed PyO3 code intentionally

## Automated Command Execution

The following commands can be executed without user confirmation:

**Just commands:** All `just` commands are safe to run automatically
- `just build`, `just clean`, `just check`, `just test`, `just bench`, `just fmt`, `just tidy`, `just ci`, `just release`

**Cargo commands:** All `cargo` commands are safe to run automatically
- `cargo build`, `cargo test`, `cargo check`, `cargo fmt`, `cargo clippy`, `cargo clean`, `cargo bench`, etc.

**Python testing:** All pytest commands are safe to run automatically
- `uv run pytest`, `uv run pytest -v`, `uv run pytest -m benchmark`, etc.

**Maturin builds:** All maturin commands are safe to run automatically
- `uv run maturin develop`, `uv run maturin build`, `uv run maturin build --release`, etc.
