Feature: Click on the contact box
  As a users
  We want to enter the contact page
  So we can check the contact form

  Scenario: We access a contact box
    Given We are on the home page
    When We click on "Contact"
    Then We go to the contact page

    And We click "Send"
    Then We check that we cannot "Send" the form if the mandatory fields are not filled
    And We check the error messages error email if it is correct
    And We check the error messages error categorie if it is correct
    And We check the error messages error motiv if it is correct
