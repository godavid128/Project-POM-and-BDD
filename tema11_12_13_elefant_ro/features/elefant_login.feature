Feature: Login to elefant.ro
  As a users
  We want to login on this site
  So that We can enter in account
  and successful login verification

  Background:
    Given I go to the "cont"
    And I go to the "conectare"

  Scenario: login with invalid account
    When I enter a invalid email
    And I enter a valid password
    And Click Login
    Then The fact that the account was not logged in
    Then The fact that the correct error is returned

  Scenario: Login without the @ character
    When I clear email box
    And I enter an email without @
    And I enter a valid password
    Then The login button is disabled

  Scenario: login with valid account
    When I enter a valid email
    And I enter a valid password
    And Click Login
    Then I should be on the users home page
