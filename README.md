# citystats

Sandbox repository to test [MkDocs](https://www.mkdocs.org/) documentation that is built for every
GitHub release and attached to it as a zip file.

The code is a small Python package, `citystats`, with Google-style docstrings that
[mkdocstrings](https://mkdocstrings.github.io/) turns into an API reference.

## Quick start

```bash
uv sync --all-extras
uv run pytest
uv run mkdocs serve   # http://127.0.0.1:8000
```
