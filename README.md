# template-rust-python-mixed

[![CI](https://github.com/malcolmgreaves/template-rust-python-mixed/actions/workflows/ci.yml/badge.svg)](https://github.com/malcolmgreaves/template-rust-python-mixed/actions/workflows/ci.yml)

Template repository for a mixed Rust & Python project. Separate Rust-only, Python-only, and mixed via PyO3 codebase.

---

## Overview

A production-ready polyglot monorepo template that demonstrates best practices for building projects with **Rust**, **Python**, and **Rust-Python integration** using PyO3. Perfect for ML/data science applications requiring high-performance computing, web services, or any project benefiting from both ecosystems.

## Features

### Architecture
- **🦀 Pure Rust packages** - High-performance crates with full Cargo workspace support
- **🐍 Pure Python packages** - ML/data packages managed with `uv` for blazing-fast dependency resolution
- **🔗 Rust-Python hybrid packages** - PyO3-powered bindings for calling Rust from Python
- **📦 Monorepo structure** - Organized workspace with shared dependencies and tooling

### Developer Experience
- **⚡ Just command runner** - Unified task execution across all languages
- **🔍 Type safety** - Full type checking for both Rust and Python codebases
- **✨ Auto-formatting** - Consistent code style with `cargo fmt` and `ruff`
- **🧪 Comprehensive testing** - Coverage reporting and benchmarking for both languages
- **🪝 Pre-commit hooks** - Automated quality checks before every commit
- **🤖 CI-ready** - Complete pipeline with `just ci` command

### Tech Stack

**Rust** (Edition 2024)
- Testing: `cargo-llvm-cov` for coverage
- Benchmarking: Criterion
- Linting: Clippy with auto-fix
- Dependency cleanup: `cargo-machete`

**Python** (3.14+)
- Package manager: `uv` (ultra-fast pip alternative)
- Key libraries: PyTorch, Polars, Pydantic, HuggingFace
- Linting/formatting: Ruff
- Type checking: `ty`
- Testing: pytest with coverage and benchmarking
- Build backend: `uv_build`

**PyO3 Integration**
- Build tool: `maturin`
- Seamless Rust-Python interop
- Workspace-aware dependency management

## Quick Start

### Prerequisites
```bash
# Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install just (command runner)
cargo install just
```

### Initial Setup
```bash
# Clone the template
git clone https://github.com/yourusername/template-rust-python-mixed.git
cd template-rust-python-mixed

# Build everything
just build

# Run the full CI pipeline
just ci
```

## Available Commands

All project tasks are managed through `just`. Run `just --list` to see all commands.

### Core Commands

| Command | Description |
|---------|-------------|
| `just build` | Build all Rust crates, sync Python dependencies, and compile PyO3 packages |
| `just clean` | Remove all build artifacts (Rust target/, Python caches, compiled extensions) |
| `just check` | Type check all code (Rust with cargo check, Python with ruff and ty) |
| `just test` | Run all tests with coverage reporting (cargo-llvm-cov + pytest) |
| `just bench` | Run all benchmarks (Criterion for Rust, pytest-benchmark for Python) |
| `just ci` | Run the full CI pipeline: tidy → check → test → bench |

### Code Quality

| Command | Description |
|---------|-------------|
| `just fmt` | Format all code (cargo fmt + ruff format) |
| `just tidy` | Clean up unused dependencies and run linters with auto-fix (machete + clippy) |

### Release

| Command | Description |
|---------|-------------|
| `just release` | Build release artifacts for all Rust crates and Python packages |

## Project Structure

```
template-rust-python-mixed/
├── rust/                   # Pure Rust crates
│   └── fictional-project/  # Example Rust crate
├── python/                 # Pure Python packages
│   └── fictional-project/  # Example Python package
├── mixed/                  # Rust-Python hybrid packages
│   └── pyo3-example/       # Example PyO3 integration
├── justfile                # Task runner configuration
├── Cargo.toml              # Rust workspace configuration
├── pyproject.toml          # Python workspace configuration
└── CLAUDE.md               # AI assistant guidance
```

### Adding New Packages

**Pure Rust crate:**
```bash
cd rust
cargo new my-crate
# Add "rust/my-crate" to workspace members in root Cargo.toml
```

**Pure Python package:**
```bash
cd python
uv init my-package --app
# Add "python/my-package" to workspace members in root pyproject.toml
uv sync
```

**PyO3 hybrid package:**
```bash
cd mixed
maturin new my-pyo3-package --bindings pyo3
# Add to workspace in root pyproject.toml
# Add to exclude list in root Cargo.toml
cd my-pyo3-package
uv run maturin develop
```

## Testing

**Run Rust tests:**
```bash
just test  # With coverage
cargo test --workspace  # Without coverage
```

**Run Python tests:**
```bash
uv run pytest -v  # All non-benchmark tests
uv run pytest -v -m benchmark --benchmark-only  # Benchmarks only
```

## Development Workflow

1. **Make changes** to your code
2. **Format**: `just fmt`
3. **Check types**: `just check`
4. **Run tests**: `just test`
5. **Commit** (pre-commit hooks run automatically)

For major changes, run the full pipeline:
```bash
just ci
```

## Continuous Integration

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- Runs on every push to `main` and all pull requests
- Installs Rust, Python (via `uv`), and `just`
- Caches dependencies for faster builds (Rust via `rust-cache`, Python via `uv` cache)
- Executes the full CI pipeline (`just ci`)
- Uploads coverage reports as artifacts:
  - **Rust coverage**: `target/llvm-cov/html/`
  - **Python coverage**: `htmlcov/`

Coverage reports are retained for 30 days and can be downloaded from the Actions tab.

## License

Mozilla Public License Version 2.0

## Contributing

This is a template repository. Fork it and customize for your needs! See `CLAUDE.md` for detailed project conventions and AI assistant guidance.
