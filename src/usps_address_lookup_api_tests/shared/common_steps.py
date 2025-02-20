import pytest
import json
from pytest_bdd import (
    parsers,
    scenario,
    given,
    when,
    then
)

@pytest.fixture(scope="function")
def context():
    return{}

@then(parsers.parse('the http response status code should be {expected_status_code}'))
def validate_response_http_status(expected_status_code):
    """Verify http response status code."""
    assert str(pytest.response.status_code) == str(expected_status_code), f"Expected http status code {expected_status_code}, but got {pytest.response.status_code}"
