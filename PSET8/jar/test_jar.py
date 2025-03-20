import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-5)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)

def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
