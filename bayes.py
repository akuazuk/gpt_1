"""
A simple Bayes theorem calculator.
"""

from typing import Union


def compute_posterior(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
    """Compute P(A|B) using Bayes' theorem.

    Parameters
    ----------
    p_a: float
        Prior probability of A.
    p_b_given_a: float
        Probability of B given A.
    p_b_given_not_a: float
        Probability of B given not A.

    Returns
    -------
    float
        Posterior probability P(A|B).
    """
    if not (0 <= p_a <= 1 and 0 <= p_b_given_a <= 1 and 0 <= p_b_given_not_a <= 1):
        raise ValueError("Probabilities must be between 0 and 1")

    p_not_a = 1 - p_a
    numerator = p_b_given_a * p_a
    denominator = numerator + p_b_given_not_a * p_not_a
    if denominator == 0:
        raise ZeroDivisionError("Denominator in Bayes calculation is zero")
    return numerator / denominator


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compute probability using Bayes' theorem")
    parser.add_argument("--p_a", type=float, required=True, help="Prior probability P(A)")
    parser.add_argument("--p_b_given_a", type=float, required=True, help="Conditional probability P(B|A)")
    parser.add_argument(
        "--p_b_given_not_a", type=float, required=True, help="Conditional probability P(B|not A)"
    )

    args = parser.parse_args()
    result = compute_posterior(args.p_a, args.p_b_given_a, args.p_b_given_not_a)
    print(f"P(A|B) = {result:.5f}")

