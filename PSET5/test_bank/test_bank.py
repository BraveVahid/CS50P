from bank import value


def test_value_hello():
    assert value("Hello") == 0
    assert value("hello, world") == 0
    assert value("HELLO") == 0


def test_value_h():
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("H") == 20


def test_value_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("123") == 100
