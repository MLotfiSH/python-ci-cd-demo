import add

def test_add():
    assert add.add_numbers(2, 3) == 5
    assert add.add_numbers(-1, 1) == 0
    assert add.add_numbers(0, 0) == 0
    assert add.add_numbers(2.5, 3.5) == 6.0
    print("All tests passed!")

if __name__ == "__main__":
    test_add()