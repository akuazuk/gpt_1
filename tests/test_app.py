import os
import sys
import pytest

pytest.importorskip("flask")
from flask.testing import FlaskClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app


def test_index_get():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bankruptcy Probability Calculator" in response.data


def test_index_post():
    client = app.app.test_client()
    response = client.post('/', data={
        'target_cash': '1600',
        'weekly_min': '350',
        'weekly_max': '390',
        'high_risk_day': '30',
        'prob_at_high_risk': '0.8',
        'bankruptcy_day': '37'
    })
    assert response.status_code == 200
    assert b"Bankruptcy Probability Calculator" in response.data
