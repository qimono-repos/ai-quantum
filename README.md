# Qi-Mono: AI & Quantum Machine Learning

A hybrid development environment for Quantum Machine Learning (QML) projects. This project uses [uv](https://docs.astral.sh/uv/) for high-performance dependency management, providing an `npm`-like experience for Python.

## INSTALLATION

### Prerequisites

- Python 3.13+
- `uv` installed on your system:
  - **Linux/macOS:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - **Windows:** `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
  - powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### Installation (The Ritual)

Clone the repository and sync the environment. This will create a local `.venv` and install all dependencies (Qiskit, PennyLane, PyTorch, etc.) with exact version locking.

```zsh
git clone <your-repo-url>
cd ai-quantum
uv sync
```
