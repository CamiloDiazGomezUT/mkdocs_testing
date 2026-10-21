# Weather

[`summarize_temperatures`][citystats.weather.summarize_temperatures] turns daily maximum
temperatures into a [`TemperatureSummary`][citystats.weather.TemperatureSummary]:

```python
from citystats import summarize_temperatures

summary = summarize_temperatures([28.0, 31.5, 33.0, 29.9])
summary.average  # 30.6
summary.hot_days  # 2
```

A day counts as hot from 30 °C. Pass another threshold with
`#!python summarize_temperatures(readings, hot_day_threshold=35.0)`.

[`celsius_to_fahrenheit`][citystats.weather.celsius_to_fahrenheit] converts a reading.

The source is in [weather.py](../../src/citystats/weather.py).
