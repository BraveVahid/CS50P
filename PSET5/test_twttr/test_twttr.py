from twttr import shorten


def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("python") == "pythn"


def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("PYTHON") == "PYTHN"


def test_shorten_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLlO") == "HLl"
    assert shorten("PyThOn") == "PyThn"


def test_shorten_no_vowels():
    assert shorten("xyz") == "xyz"
    assert shorten("bcdfg") == "bcdfg"


def test_shorten_empty_string():
    assert shorten("") == ""


def test_shorten_numbers_and_symbols():
    assert shorten("12345") == "12345"
    assert shorten("!@#$%") == "!@#$%"
