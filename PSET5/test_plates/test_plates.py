from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("ECTO88") == True


def test_invalid_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_invalid_start():
    assert is_valid("50CS") == False
    assert is_valid("1234") == False


def test_invalid_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False


def test_invalid_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
