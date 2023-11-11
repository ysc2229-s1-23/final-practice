import pytest
from questions.min_tokens import min_tokens_for_total

@pytest.mark.parametrize("n, x, token_values, expected", [
    (3, 11, [1, 5, 7], 3),
    (3, 9, [2, 3, 5], 3),

    (1, 100, [1], 100),  # Only one type of coin
    (5, 8, [2, 4, 6, 8, 10], 1),  # Direct match with a single coin
    (3, 1, [2, 3, 4], -1),  # Impossible to form the sum
    (3, 0, [1, 5, 7], 0),  # Zero sum

    (5, 100, [1, 10, 25, 50, 100], 1),  # Large denominations available
    (10, 1000, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], 1),  # Many denominations

    (100, 10000, list(range(1, 101)), 100),  # Many coins, large sum
    (50, 999, list(range(1, 51)), 20),  # Many coins, sum not directly reachable
    (100, 100000, [i**2 for i in range(1, 101)], 10),  # Quadratic coin values

    (100, 98765, [i for i in range(1, 101) if i % 2 == 0], -1),  # Even coin values, approximate match
    (100, 123456, [i for i in range(1, 101) if i % 2 != 0], 1248),

    (0, 0, [], 0),  # No coins and zero sum
    (0, 10, [], -1),  # No coins but positive sum
])
def test_min_tokensfor_sum(n, x, token_values, expected):
    assert min_tokens_for_total(n, x, token_values) == expected
