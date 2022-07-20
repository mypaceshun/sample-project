from sample_project.main import func


def test_func_success_str():
    assert func("abc") == 3


def test_func_success_int():
    assert func(10) == 10
