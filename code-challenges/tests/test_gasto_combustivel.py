import pytest

from problems.gasto_combustivel import Solution

@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution.fuel_spent(10, 85) == '70.833'

def test_case_2(solution):
    assert solution.fuel_spent(2, 92) == '15.333'

def test_case_3(solution):
    assert solution.fuel_spent(22, 67) == '122.833'