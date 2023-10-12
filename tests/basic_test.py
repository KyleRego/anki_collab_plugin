import sys
sys.path.append("../src")

from basic_add import function_to_test

def test_function_to_test():
    assert function_to_test(5, 5) == 10
