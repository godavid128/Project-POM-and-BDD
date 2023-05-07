Feature: Click on the search box
  As a users
  We want to go to the results page
  So we can check the products

  Scenario: We access a search box
    When We search a product of your choice
    Then we check that at least 5 results were returned
    When We click filtrer price
    And We filter by price
    And we check that all returned products have a price within the filter range

  Scenario: We search a non-existent product
    When We search a non-existent product
    Then we have the error message "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."
