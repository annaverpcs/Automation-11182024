# Author: Anna Verkhovskaya
# Jira ID ABC-123

Feature: Profitolizer Login Test Scenarios for functional testing

  Scenario: Login with valid username and valid password
    # this is test case from ABC-234
    Given Open "https://profitolizer.com/"
    When Verify page by title "Home - Profitolizer"
    Then Click element "//a[contains(text(),'Login')]"
    Then Wait for the element with xpath "//h5" to be present
    And Verify that xpath "//h5" should contain text "Login to Your Account"
    And Verify that xpath "//p[contains(text(),'Enter your username & password to login')]" should contain text "Enter your username & password to login"
    #fill out email textfield with valid username and password textfield with valid password
    When Type "annaverpcs+11@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    Then Click element "//button[@type='submit']"
    #Verification for valid login on Home page
    Then Verify page by title "Profotolizer - Projects"
    Then Wait for the element with xpath "//span[contains(text(),'annaverpcs11')]" to be present
    And Verify that xpath "//span[contains(text(),'annaverpcs11')]" should contain text "annaverpcs11"

  Scenario: Login with valid username and valid password for the user who has 1 project
    # this is test case from ABC-234
    Given Open "https://profitolizer.com/"
    When Verify page by title "Home - Profitolizer"
    Then Click element "//a[contains(text(),'Login')]"
    Then Wait for the element with xpath "//h5" to be present
    And Verify that xpath "//h5" should contain text "Login to Your Account"
    And Verify that xpath "//p[contains(text(),'Enter your username & password to login')]" should contain text "Enter your username & password to login"
    #fill out email textfield with valid username and password textfield with valid password
    When Type "annaverpcs+10@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    Then Click element "//button[@type='submit']"
    #Verification for valid login on Profotolizer - P&L charts page
    Then Verify page by title "Profotolizer - P&L charts"
    Then Wait for the element with xpath "//span[contains(text(),'annaverpcs10')]" to be present
    And Verify that xpath "//span[contains(text(),'annaverpcs10')]" should contain text "annaverpcs10"
    And Wait 1 seconds
    And Verify that xpath "//h1" should contain text "P&L Graphs"


  Scenario: Login with valid username and empty password
    # this is test case from ABC-234
    Given Open "https://profitolizer.com/"
    When Verify page by title "Home - Profitolizer"
    Then Click element "//a[contains(text(),'Login')]"
    Then Wait for the element with xpath "//h5" to be present
    And Verify that xpath "//h5" should contain text "Login to Your Account"
    And Verify that xpath "//p[contains(text(),'Enter your username & password to login')]" should contain text "Enter your username & password to login"
    #fill out email textfield with valid username and password textfield with valid password
    When Type "annaverpcs+11@gmail.com" into "//input[@type='text']"
    Then Click element "//button[@type='submit']"
    #Verify that error message appears on Login page
    Then Verify presents of element "//div[@class='invalid-feedback' and contains(text(),'Password is required')]"
