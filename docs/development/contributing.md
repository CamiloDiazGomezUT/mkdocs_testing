# Contributing

## Set up

```bash
uv sync --all-extras
```

## Checks

The CI runs the same commands on every pull request:

```bash
uv run ruff check .
uv run ruff format --check
uv run pytest          # fails below 90 % coverage
uv run mkdocs build --strict
```

## Documentation

Preview the site while editing:

```bash
uv run mkdocs serve   # http://127.0.0.1:8000
```

Where each page goes:

Getting started
:   Installation and a first example.

Guides
:   How to do one task with the package.

Explanation
:   How the package is organized and why.

API Reference
:   Generated from the docstrings in `src/` by `docs/scripts/gen_ref_pages.py`. Do not edit it
    by hand.

Development
:   Working on the project itself.

Docstrings follow the [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings),
checked by Ruff.

Abbreviations are defined once in `docs/includes/glossary.md` and show their meaning on hover
in every page:

```markdown
*[CAGR]: Compound Annual Growth Rate
```

Add an entry to `CHANGELOG.md` under **Unreleased** for every user-facing change.
