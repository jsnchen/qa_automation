Feature: USPS Address Lookup API

  Scenario Outline: Verify USPS address lookup API response for different states
    Given the USPS API is available
    * the target fixture of address lookup response should be empty
    When I send a request to USPS address lookup with a randomly generated address from "<state>"
    Then the http response status code should be 200
    * the result status should be "SUCCESS"
    And the response should contain the correct city and state

    Examples:
      | state |
      | CA    |
      | FL    |