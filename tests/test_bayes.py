import math
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bayes import compute_posterior


def test_smoke_example():
    result = compute_posterior(0.01, 0.9, 0.05)
    assert math.isclose(result, 0.153846, rel_tol=1e-6)


def test_equal_probabilities():
    result = compute_posterior(0.5, 0.7, 0.3)
    assert math.isclose(result, 0.7, rel_tol=1e-9)

