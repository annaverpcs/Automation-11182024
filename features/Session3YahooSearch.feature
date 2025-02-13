# Created by averkhovskaya at 2/13/25

Feature: Yahoo Search functional testing

  Scenario: Yahoo Web Search by valid name
    Given Open "https://search.yahoo.com/"
    Then Type "Python" into "//input[@id='yschsp']"
    And Click element "//button[@id='sbq-submit']"
    # move to Yahoo Search Result page
    Then Verify presents of element "//input[@id='yschsp' and @value='Python']"
    Then Wait 2 seconds
    And Verify that xpath "//div[@id='left']" should contain text "Python"


