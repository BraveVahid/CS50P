from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

    assert validate("256.0.0.1") == False
    assert validate("0.256.0.1") == False
    assert validate("0.0.256.1") == False
    assert validate("0.0.0.256") == False

    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.4.") == False
    assert validate(".1.2.3.4") == False
    assert validate("1..2.3.4") == False
