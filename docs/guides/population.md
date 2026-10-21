# Population

A [`City`][citystats.population.City] holds the census counts by year and computes density and
growth:

```python
from citystats import City

madrid = City(
    name="Madrid",
    area_km2=604.3,
    population_by_year={2014: 3_165_000, 2024: 3_416_000},
)
madrid.density()  # inhabitants per km², latest census
madrid.growth_rate(2014, 2024)  # CAGR between the two censuses
```

`#!python madrid.density(2014)` uses a given census instead of the latest one.

To get the CAGR between two counts without a `City`, use
[`annual_growth_rate`][citystats.population.annual_growth_rate].

The source is in [population.py](../../src/citystats/population.py).
