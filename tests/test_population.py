import pytest

from citystats.population import City, annual_growth_rate


@pytest.fixture
def city():
    return City(name="Testville", area_km2=100.0, population_by_year={2020: 10_000, 2022: 12_100})


def test_annual_growth_rate():
    assert annual_growth_rate(1_000_000, 1_210_000, 2) == pytest.approx(0.1)


@pytest.mark.parametrize(("start", "end", "years"), [(0, 10, 1), (10, -1, 1), (10, 10, 0)])
def test_annual_growth_rate_rejects_invalid_input(start, end, years):
    with pytest.raises(ValueError):
        annual_growth_rate(start, end, years)


def test_density_uses_latest_year_by_default(city):
    assert city.latest_year == 2022
    assert city.density() == pytest.approx(121.0)
    assert city.density(2020) == pytest.approx(100.0)


def test_growth_rate_between_census_years(city):
    assert city.growth_rate(2020, 2022) == pytest.approx(0.1)


def test_city_without_census_has_no_latest_year():
    with pytest.raises(ValueError, match="no census"):
        _ = City(name="Empty", area_km2=1.0).latest_year


def test_city_area_must_be_positive():
    with pytest.raises(ValueError, match="area"):
        City(name="Nowhere", area_km2=0)
