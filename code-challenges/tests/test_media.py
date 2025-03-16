import pytest
from problems.media import Solution

@pytest.fixture
def solution():
    return Solution()

def test_exemple1(solution):
    assert solution.media(5.0, 7.1) == 'MEDIA = 6.43182'

def test_exemple2(solution):
    assert solution.media(0.0, 7.1) == 'MEDIA = 4.84091'

def test_exemple3(solution):
    assert solution.media(10.0, 10.0) == 'MEDIA = 10.00000'