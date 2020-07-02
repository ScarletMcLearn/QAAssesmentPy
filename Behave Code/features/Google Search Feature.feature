Feature: Google Search Feature 

    Scenario: Do simple google search

    Given the User is on Google home page
    When User enters search terms in search bar
    And clicks search button
    Then search results are shown