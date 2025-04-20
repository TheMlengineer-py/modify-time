from datetime import datetime, timedelta

import pytest
from dateutil.relativedelta import relativedelta

from time_parser import parse_time_expression


def test_day_add():
    """
    Test that 1 day is correctly added to the base datetime.
    """
    now = datetime(2022, 1, 8, 9, 0, 0)
    result = parse_time_expression("now()+1d", base_time=now)
    expected = now + timedelta(days=1)
    print(f"[test_day_add] Result: {result}, Expected: {expected}")
    assert result == expected


def test_multiple_units():
    """
    Test that multiple modifiers (days and hours) are added correctly.
    """
    now = datetime(2022, 1, 8, 9, 0, 0)
    result = parse_time_expression("now()+10d+12h", base_time=now)
    expected = now + timedelta(days=10, hours=12)
    print(f"[test_multiple_units] Result: {result}, Expected: {expected}")
    assert result == expected


def test_months():
    """
    Test that 1 month is correctly added using relativedelta.
    """
    now = datetime(2022, 1, 8, 9, 0, 0)
    result = parse_time_expression("now()+1mon", base_time=now)
    expected = now + relativedelta(months=1)
    print(f"[test_months] Result: {result}, Expected: {expected}")
    assert result == expected


def test_invalid():
    """
    Test that expressions not starting with 'now()' raise ValueError.
    """
    with pytest.raises(ValueError):
        print("[test_invalid] Expected ValueError for missing 'now()'")
        parse_time_expression("tomorrow+1d")


def test_unknown_unit():
    """
    Test that an unknown time unit (e.g., 'x') raises ValueError.
    """
    with pytest.raises(ValueError):
        print(
            "[test_unknown_unit]" "Expected" "ValueError for unknowntime unit 'x'"
        )
        parse_time_expression("now()+5x")
