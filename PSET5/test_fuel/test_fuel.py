from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_convert_errors():
    try:
        convert("cat/dog")
        assert False
    except ValueError:
        assert True

    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        assert True

    try:
        convert("5/3")
        assert False
    except ValueError:
        assert True
