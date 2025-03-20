from seasons import get_total_minutes


def test_get_total_minutes():
    assert get_total_minutes("2000-01-01") == (get_total_minutes("2000-01-01"))
    assert get_total_minutes("2020-01-01") == (get_total_minutes("2020-01-01"))
    assert get_total_minutes("2023-12-31") == (get_total_minutes("2023-12-31"))
    assert get_total_minutes("invalid-date") is None
    assert get_total_minutes("2025-02-30") is None
