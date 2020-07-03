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


    Scenario: Upload File to One Drive

        When the User makes POST request to API
        Then File uploaded successfuly to One Drive 


    Scenario: Verify File on One Drive

        When the User makes GET request to API
        Then File found successfuly on One Drive 