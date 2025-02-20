import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from utils.api_helper import send_api_request
from utils.data_generator import generate_random_address
from shared.common_steps import context, validate_response_http_status

USPS_API_URL = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"
HEADERS = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://tools.usps.com",
    "referer": "https://tools.usps.com/zip-code-lookup.htm?byaddress",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}

(then(parsers.parse('the http response status code should be {expected_status_code}')))(validate_response_http_status)

# Link the feature file to step definitions
# scenarios("usps_address_lookup.feature")

@scenario("usps_address_lookup.feature", "Verify USPS address lookup API response for different states")
def test_usps_address_lookup():
    pass

@pytest.fixture
def address_lookup_resp():
    return "{}"

@given("the USPS API is available")
def usps_api_available():
    """Check if USPS API page is accessible."""
    response = send_api_request("GET", "https://tools.usps.com/zip-code-lookup.htm?byaddress", allow_redirects=False)
    assert response.status_code == 302, "USPS API may not be available as it should redirect"

@given("the target fixture of address lookup response should be empty")
def target_fixture_is_empty(address_lookup_resp):
    print(f"address_lookup_response: {address_lookup_resp}")
    assert address_lookup_resp == "{}"

"""
  Use target_fixture to store the API response for later use
"""
@when(parsers.parse('I send a request to USPS address lookup with a randomly generated address from "{state}"'), target_fixture="address_lookup_resp")
def send_post_request(state):
    """Send a USPS API request with a dynamic address from the specified state."""
    method = "POST"
    url = USPS_API_URL
    
    pytest.test_address = generate_random_address(state)
    payload = {
        "companyName": "",
        "address1": pytest.test_address["address1"],
        "address2": pytest.test_address["address2"],
        "city": pytest.test_address["city"],
        "state": pytest.test_address["state"],
        "urbanCode": "",
        "zip": pytest.test_address["zip"],
    }
    print(payload)
    pytest.response = send_api_request(method, url, headers=HEADERS, payload=payload)
    return pytest.response

"""
    Input parameters: 
    * The resultStatus of the API response
    * The target fixture stored from previous API call
"""
@then(parsers.parse('the result status should be "{expected_status}"'))
def validate_result_status(expected_status, address_lookup_resp):
    """Verify response resultStatus."""
    print(f"address_lookup_response: {address_lookup_resp.json()}")
    response_json = address_lookup_resp.json()
    print(response_json)
    assert response_json.get("resultStatus") == expected_status, f"Expected {expected_status}, but got {response_json.get('resultStatus')}"

@then("the response should contain the correct city and state")
def validate_city_state(address_lookup_resp):
    """Check if the response contains the correct city and state."""
    #response_json = pytest.response.json()
    response_json = address_lookup_resp.json()
    address = response_json["addressList"][0]

    assert address["city"].upper() == pytest.test_address["city"].upper(), f"City mismatch: {address['city']}"
    assert address["state"] == pytest.test_address["state"], f"State mismatch: {address['state']}"
