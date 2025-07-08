import os
import sys

from flask.testing import FlaskClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app


def test_index_get():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bayes Theorem Calculator" in response.data


def test_index_post():
    client = app.app.test_client()
    response = client.post('/', data={
        'p_a': '0.01',
        'p_b_given_a': '0.9',
        'p_b_given_not_a': '0.05'
    })
    assert response.status_code == 200
    assert b"P(A|B)" in response.data
    assert b"0.15385" in response.data
