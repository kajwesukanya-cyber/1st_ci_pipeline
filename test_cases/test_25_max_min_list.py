import importlib

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([10, 20, 5, 40, 15]) == (40, 5)


def test_single_element():
    assert find_max_min([10]) == (10, 10)


def test_negative_numbers():
    assert find_max_min([-5, -10, -2]) == (-2, -10)


def test_duplicate_numbers():
    assert find_max_min([5, 5, 5]) == (5, 5)


def test_empty_list():
    try:
        find_max_min([])
        assert False
    except ValueError:
        assert True