# Created by averkhovskaya at 2/20/25
Feature:  Profitolizer Login Test Scenarios for functional testing with custom steps
  # Enter feature description here

  Scenario: Login to app with custom steps
    #Given Open "https://profitolizer.com/"
    Given I would like to open "Profitolizer"
    # When Verify page by title "Home - Profitolizer"
    Then AnnaV verify that the page title is "Home - Profitolizer"
    #Then Click element "//a[contains(text(),'Login')]"
   # Then Wait for the element with xpath "//h5" to be present