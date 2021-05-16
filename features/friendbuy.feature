
Feature: Friendbuy referral flow
  Verify the complete user journey to perform a successful referral

  Scenario: Verify friendbuy referral flow
    Given I go to partner websites homepage
    When  I click on ribbon to pop up friendbuy widget
    And   I enter my email address
    And   I click on start sharing
    And   I enter my friends email address
    And   I click on send email
    Then  I verify that the referral was successful