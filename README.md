# Bayes Theorem Calculator

This repository contains a simple command line application for computing the posterior probability `P(A|B)` using Bayes' theorem.

## Usage

The script `bayes.py` exposes both a function and a CLI interface. To compute the probability, run:

```bash
python bayes.py --p_a <P(A)> --p_b_given_a <P(B|A)> --p_b_given_not_a <P(B|not A)>
```

For example:

```bash
python bayes.py --p_a 0.01 --p_b_given_a 0.9 --p_b_given_not_a 0.05
```

This will output:

```
P(A|B) = 0.15385
```

## Running Tests

Tests are provided using `pytest`. To run them execute:

```bash
pytest
```

