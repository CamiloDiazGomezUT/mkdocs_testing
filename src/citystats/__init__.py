"""Small helpers to describe a city from its population and weather data.

The package has two modules:

- [`citystats.population`][citystats.population] computes density and growth from census data.
- [`citystats.weather`][citystats.weather] summarizes daily temperature readings.

Example:
    ```python
    from citystats import City, summarize_temperatures

    madrid = City(
        name="Madrid", area_km2=604.3, population_by_year={2014: 3_165_000, 2024: 3_416_000}
    )
    madrid.density()
    summarize_temperatures([31.5, 33.0, 29.8])
    ```
"""

from citystats.population import City, annual_growth_rate
from citystats.weather import TemperatureSummary, celsius_to_fahrenheit, summarize_temperatures

__all__ = [
    "City",
    "TemperatureSummary",
    "annual_growth_rate",
    "celsius_to_fahrenheit",
    "summarize_temperatures",
]
