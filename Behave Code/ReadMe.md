Project System:
VirtualBox (Version 6.0.14 r133895 (Qt5.6.2))
Guest Additions
Linux Mint 18.3 Sylvia

Working Directory: 
/home/scarlet/Projects/Automation/Assesment/Py Assesment/1/Behave Code


Python version: 3.5

Install requirements by using :
pip3.5 install -r requirements.txt


Configuration Variables:

config.py

Variables:
    - browser [options: 'chrome' | 'firefox']
    - country [options : 'ww' | 'uk' | 'nz']
    - cookies [options : 'off']  *Keep Cookies on for Browser Test
    - email   
    [OneDrive Email]

    - password 
    [OneDrive Password]

    - incorrect_email 
    [Incorrect Email]

    - incorrect_password 
    [Incorrect Password]

    - authorization_token
    [
    Can be gotten from : 
    https://developer.microsoft.com/en-us/graph/graph-explorer
    
    Note: - Needs top be updated before running tests

          - Can be found in 'Access token' tab from Panel
    ]

    - file_to_upload
    [
    Name of the file to Upload 
    Should include Extension
    Keep file in features folder
    ]

    - file_to_search
    [
    Name of the file to Search
    ]

Run Particular Feature:
behave -n 'Go to different Locale site'

Run All Features:
behave

Generate Report : 

For Particular Feature:

behave -f allure_behave.formatter:AllureFormatter -o %allure_res
ult_folder% -n 'Go to different Locale site'

allure serve %allure_result_folder%


For All Features:

behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

allure serve %allure_result_folder%