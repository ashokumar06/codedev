import pytest
from main import hello_world, calculate_fibonacci

def test_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(10) == 55

def test_hello_world():
    # This would test the function if it returned something
    pass
