"""Population figures of a city: density and growth over time.

```mermaid
flowchart LR
    C[Census by year] --> D[City.density]
    C --> G[City.growth_rate]
    G --> A[annual_growth_rate]
```
"""

from dataclasses import dataclass, field


def annual_growth_rate(start_population: int, end_population: int, years: int) -> float:
    """Return the compound annual growth rate between two population counts.

    Args:
        start_population: Population at the start of the period. Must be positive.
        end_population: Population at the end of the period. Must not be negative.
        years: Length of the period, in years. Must be positive.

    Returns:
        The growth rate per year as a fraction, e.g. ``0.01`` for 1 % a year.

    Raises:
        ValueError: If a population or the number of years is out of range.

    Example:
        ```python
        annual_growth_rate(1_000_000, 1_210_000, 2)  # 0.1
        ```
    """
    if start_population <= 0 or end_population < 0:
        raise ValueError("Populations must be positive")
    if years <= 0:
        raise ValueError("The period must be at least one year")
    return (end_population / start_population) ** (1 / years) - 1


@dataclass(frozen=True)
class City:
    """A city and its population census.

    Attributes:
        name: Name of the city.
        area_km2: Surface of the city, in square kilometres.
        population_by_year: Population counts keyed by census year.
    """

    name: str
    area_km2: float
    population_by_year: dict[int, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the area.

        Raises:
            ValueError: If the area is zero or negative.
        """
        if self.area_km2 <= 0:
            raise ValueError("The area must be positive")

    @property
    def latest_year(self) -> int:
        """Most recent census year.

        Returns:
            The highest year in [`population_by_year`][citystats.population.City].

        Raises:
            ValueError: If the city has no census data.
        """
        if not self.population_by_year:
            raise ValueError(f"{self.name} has no census data")
        return max(self.population_by_year)

    def density(self, year: int | None = None) -> float:
        """Return the population density.

        Args:
            year: Census year to use. Defaults to the
                [`latest_year`][citystats.population.City.latest_year].

        Returns:
            Inhabitants per square kilometre.

        Raises:
            KeyError: If there is no census for ``year``.
        """
        year = self.latest_year if year is None else year
        return self.population_by_year[year] / self.area_km2

    def growth_rate(self, start_year: int, end_year: int) -> float:
        """Return the compound annual growth rate between two census years.

        Uses [`annual_growth_rate`][citystats.population.annual_growth_rate].

        Args:
            start_year: First census year.
            end_year: Last census year, after ``start_year``.

        Returns:
            The growth rate per year as a fraction.

        Raises:
            KeyError: If there is no census for one of the years.
        """
        return annual_growth_rate(
            self.population_by_year[start_year],
            self.population_by_year[end_year],
            end_year - start_year,
        )
