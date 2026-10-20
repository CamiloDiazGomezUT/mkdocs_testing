import pytest

from citystats.weather import celsius_to_fahrenheit, summarize_temperatures


@pytest.mark.parametrize(("celsius", "fahrenheit"), [(0, 32.0), (100, 212.0), (-40, -40.0)])
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == fahrenheit


def test_summarize_temperatures():
    summary = summarize_temperatures([28.0, 31.5, 33.0, 29.9])

    assert summary.days == 4
    assert summary.minimum == 28.0
    assert summary.maximum == 33.0
    assert summary.average == 30.6
    assert summary.hot_days == 2


def test_summarize_temperatures_with_custom_threshold():
    assert summarize_temperatures([20.0, 25.0], hot_day_threshold=25.0).hot_days == 1


def test_summarize_temperatures_needs_readings():
    with pytest.raises(ValueError):
        summarize_temperatures([])
