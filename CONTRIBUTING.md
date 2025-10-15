# Contributing

We welcome contributions! This project favors a clean, zero-dependency runtime with strong testing and tooling in dev.

Development setup
- Install dev tools:
```bash path=null start=null
pip install -r requirements-dev.txt
pre-commit install
```
- Run checks locally:
```bash path=null start=null
ruff check . && black --check . && isort --check-only . && mypy --config-file mypy.ini && pytest -q --tb=short
```

Branches & PRs
- Create feature branches from main.
- Keep PRs focused; include tests when possible.
- CI must pass (lint/type/test) before merge.

Commit style
- Conventional-ish messages are appreciated, e.g.:
  - feat: add X
  - fix: resolve Y
  - docs: update Z
  - ci: improve workflow

License
- By contributing, you agree contributions are licensed under the repository’s MIT license.
