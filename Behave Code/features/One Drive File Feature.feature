Feature: OneDrive upload and verification 

    Scenario: User uploads a file to OneDrive 

    Given the User is navigates to One Drive page
    And selects Locale
    When the User clicks Sign In
    And the User enters email in E-mail field
    And submits email
    And the User enters password in Password field
    And submits password
    And One Drive is shown
    And the User clicks the Upload File dropdown menu
    And selects Files from dropdown menu
    And select File to Upload
    Then file is uploaded

    # When User enters search terms in search bar
    # And clicks search button
    # Then search results are shown

    # https://onedrive.live.com/about/en-us/signin/


    Scenario: Invalid Email address cannot log in 

    Given the User is navigates to One Drive page
    And selects Locale
    When the User clicks Sign In
    And the User enters incorrect email in E-mail field
    And submits email
    Then incorrect email error message is shown


    Scenario: Incorrect password cannot log in 

    Given the User is navigates to One Drive page
    And selects Locale
    When the User clicks Sign In
    And the User enters email in E-mail field
    And submits email
    And the User enters incorrect password in Password field
    And submits password
    Then incorrect password error message is shown


    Scenario: Go to different Locale site
        Given the User is navigates to One Drive page with selected locale
        And selects custom Locale
        Then One Drive site is shown 


    Scenario: Upload File to One Drive using API

        Given the User has valid Authentication Key
        When the User makes PUT request to API
        Then response status code shows file uploaded 


    Scenario: Verify File on One Drive

        Given the User has valid Authentication Key
        When the User makes GET request to API
        Then File found successfuly on One Drive 