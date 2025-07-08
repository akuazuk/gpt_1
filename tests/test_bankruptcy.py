import math
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bankruptcy import bankruptcy_probabilities


def test_bankruptcy_curve_reaches_one():
    probs = bankruptcy_probabilities(1600, 200)
    assert probs[-1] == 1.0


def test_probability_increase_after_high_risk():
    probs = bankruptcy_probabilities(1600, 350)
    # Probability on high_risk_day should equal the configured value
    assert math.isclose(probs[29], 0.8, rel_tol=1e-6)
    # The next day should be greater
    assert probs[30] > probs[29]
