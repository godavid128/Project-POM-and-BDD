Feature: Home page welcome message
  As a user
  I want to be welcome
  So that I know I am on the right spot

  @smoke
  Scenario: Check curent url
    When We open internet page
    Then We see this url "https://www.elefant.ro/"