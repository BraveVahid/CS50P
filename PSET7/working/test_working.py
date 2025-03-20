from working import convert
import pytest


def test_convert_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00")
