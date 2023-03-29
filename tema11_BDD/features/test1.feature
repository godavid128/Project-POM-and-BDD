Feature: Login to the internet
  As a users
  We want to login on this site
  So that We can enter in account
  and successful login verification

Scenario: We access a few clicks
  Given We are on the home page
  When We click to the 'Floating Menu'
  And click to the 'Forgot Password'
  And we click to the 'Form Authentication'
  Then we access a new page

Scenario: login with valid account
  Given I go to the 'Form Authentication'
  When I enter a valid email
  And I enter a valid password
  And I press 'Login'
  Then I should be on the users home page

Scenario: successful login verification
  Given We are on the Secure page
  When I should see 'You logged into a secure area!' is displayed
  And To contain the 'Logout' button
  Then we click to the button 'Logout'