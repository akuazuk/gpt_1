from typing import List

def bankruptcy_probabilities(
    target_cash: float,
    weekly_cash: float,
    high_risk_day: int = 30,
    prob_at_high_risk: float = 0.8,
    bankruptcy_day: int = 37,
) -> List[float]:
    """Return cumulative probability of bankruptcy for each day.

    Parameters
    ----------
    target_cash : float
        Cash amount that must be collected to avoid bankruptcy.
    weekly_cash : float
        Expected cash flow per week.
    high_risk_day : int, default 30
        Day after which the probability jumps to ``prob_at_high_risk``
        if the target cash is not met.
    prob_at_high_risk : float, default 0.8
        Probability of bankruptcy on ``high_risk_day`` when the target
        cash has not been received.
    bankruptcy_day : int, default 37
        Day by which bankruptcy definitely occurs if cash is still
        insufficient.

    Returns
    -------
    List[float]
        Probability of bankruptcy for each day from 1 to ``bankruptcy_day``.
    """
    if not 0 <= prob_at_high_risk <= 1:
        raise ValueError("prob_at_high_risk must be between 0 and 1")
    if high_risk_day >= bankruptcy_day:
        raise ValueError("bankruptcy_day must be greater than high_risk_day")
    if weekly_cash < 0:
        raise ValueError("weekly_cash must be non-negative")

    slope = (1.0 - prob_at_high_risk) / (bankruptcy_day - high_risk_day)
    daily_cash = weekly_cash / 7.0
    probabilities = []
    for day in range(1, bankruptcy_day + 1):
        cash = daily_cash * day
        if cash >= target_cash:
            prob = 0.0
        elif day < high_risk_day:
            prob = 0.0
        elif day == high_risk_day:
            prob = prob_at_high_risk
        else:
            prob = prob_at_high_risk + slope * (day - high_risk_day)
            prob = min(prob, 1.0)
        probabilities.append(prob)
    return probabilities
