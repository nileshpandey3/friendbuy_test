
Feature: Friendbuy API end point verification

  Scenario: Verify POST request for authentication
    Then Verify a user can successfully authenticate and receive an auth token

  Scenario: Verify GET all users end-point
    Then  Verify successful GET request for retrieving entire user list

  Scenario: Verify GET individual users end-point
    Then Verify successful GET request to retrieve individual user info

  Scenario: Verify negative case for GET users API [Invalid Auth token]
    Then Verify GET users API response for invalid auth token

  Scenario: Verify negative case for GET users API [No Auth token]
    Then Verify GET users API response when no auth token is provided
