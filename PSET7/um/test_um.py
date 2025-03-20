from um import count


def test_count():
    assert count("Hello, um, world!") == 1
    assert count("Um, thanks, um, for the album.") == 2
    assert count("Yummy food!") == 0
    assert count("UM is not the same as um.") == 2
    assert count("This is um... um... um... a test.") == 3
    assert count("um?") == 1
    assert count("Um, um, um, um!") == 4
    assert count("") == 0
    assert count("um") == 1
    assert count("UM") == 1
    assert count("um um um") == 3
    assert count("umum") == 0
    assert count("yummy") == 0
