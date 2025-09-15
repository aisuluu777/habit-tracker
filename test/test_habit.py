import pytest

def minus(a, b):
    return a - b


@pytest.mark.parametrize("a, b, expected_sum", [(7, 2, 5), 
                                                (6, 5, 1)])
def test_add_func(a, b, expected_sum):
    assert minus(a, b) == expected_sum


@pytest.mark.parametrize("a, b, error", [(7, "h", TypeError), 
                                         ])
def test_type_error(a, b, error):
    with pytest.raises(error):
        assert minus(a, b) == error