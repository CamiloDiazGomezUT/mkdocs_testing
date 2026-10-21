# Getting started

## Install

The package is not published on PyPI. Clone the repository and install it with
[uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/CamiloDiazGomezUT/mkdocs_testing.git
cd mkdocs_testing
uv sync
```

## First example

```python
from citystats import City, summarize_temperatures

madrid = City(
    name="Madrid",
    area_km2=604.3,
    population_by_year={2014: 3_165_000, 2024: 3_416_000},
)
madrid.density()  # inhabitants per km², latest census

summarize_temperatures([31.5, 33.0, 29.8])
```

## Next steps

- [Population](guides/population.md) and [Weather](guides/weather.md) guides.
- [API Reference](reference/index.md) for every function and class.
