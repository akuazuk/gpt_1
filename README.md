# Probability Tools

This repository provides utilities for calculating probabilities and
an interactive web application for visualising the risk of bankruptcy
based on expected cash flow.

## Command Line Bayes Calculator

`bayes.py` exposes both a function and a CLI interface for computing
posterior probabilities using Bayes' theorem:

```bash
python bayes.py --p_a <P(A)> --p_b_given_a <P(B|A)> --p_b_given_not_a <P(B|¬A)>
```

For example:

```bash
python bayes.py --p_a 0.01 --p_b_given_a 0.9 --p_b_given_not_a 0.05
```

outputs:

```
P(A|B) = 0.15385
```

## Web Application

The Flask application `app.py` lets you explore how the probability of
bankruptcy evolves if a required cash amount is not received on time.

Install the dependencies and run the app:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser and enter:

- the cash that must be received within 30 days,
- the minimum and maximum expected weekly cash flow,
- the day when the risk jumps (default 30),
- the probability on that day (default 0.8), and
- the day when bankruptcy certainly occurs (default 37).

After submitting the form a chart will display the cumulative
probability of bankruptcy for the minimum and maximum weekly cash flow
scenarios.

## Running Tests

Tests are written with `pytest`:

```bash
pytest
```
