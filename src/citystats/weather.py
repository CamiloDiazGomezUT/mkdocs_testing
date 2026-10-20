"""Summaries of daily temperature readings."""

from dataclasses import dataclass
from statistics import mean

HOT_DAY_CELSIUS = 30.0
"""Maximum temperature from which a day counts as hot, in degrees Celsius."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from degrees Celsius to degrees Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        The same temperature in degrees Fahrenheit.

    Example:
        ```python
        celsius_to_fahrenheit(100)  # 212.0
        ```
    """
    return celsius * 9 / 5 + 32


@dataclass(frozen=True)
class TemperatureSummary:
    """Statistics of a series of daily maximum temperatures, in degrees Celsius.

    Attributes:
        days: Number of readings.
        minimum: Lowest reading.
        maximum: Highest reading.
        average: Mean of the readings.
        hot_days: Readings at or above [`HOT_DAY_CELSIUS`][citystats.weather.HOT_DAY_CELSIUS].
    """

    days: int
    minimum: float
    maximum: float
    average: float
    hot_days: int


def summarize_temperatures(
    daily_max_celsius: list[float], hot_day_threshold: float = HOT_DAY_CELSIUS
) -> TemperatureSummary:
    """Summarize a series of daily maximum temperatures.

    Args:
        daily_max_celsius: One maximum temperature per day, in degrees Celsius.
        hot_day_threshold: Temperature from which a day counts as hot.

    Returns:
        A [`TemperatureSummary`][citystats.weather.TemperatureSummary] with the average rounded to
        one decimal.

    Raises:
        ValueError: If there are no readings.
    """
    if not daily_max_celsius:
        raise ValueError("At least one reading is needed")
    return TemperatureSummary(
        days=len(daily_max_celsius),
        minimum=min(daily_max_celsius),
        maximum=max(daily_max_celsius),
        average=round(mean(daily_max_celsius), 1),
        hot_days=sum(reading >= hot_day_threshold for reading in daily_max_celsius),
    )
