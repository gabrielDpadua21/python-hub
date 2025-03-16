import pytest
from problems.diferenca import Solution

@pytest.fixture
def solution():
    return Solution()

def test_exemple1(solution):
    assert solution.difference(5, 6, 7, 8) == -26

def test_exemple2(solution):
    assert solution.difference(0, 0, 7, 8) == -56

def test_exemple3(solution):
    assert solution.difference(10, 10, 10, 10) == 0