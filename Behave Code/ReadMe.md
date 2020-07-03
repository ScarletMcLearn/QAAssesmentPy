Project System:
VirtualBox
Guest Additions
Linux Mint 18.3 Sylvia

Working Directory: 
/home/scarlet/Projects/Automation/Assesment/Py Assesment/1/Behave Code


Python version: 3.5

Install requirements by using :
pip3.5 install -r requirements.txt


Configuration Variables:

config.py


Run Particular Feature:
behave -n 'Go to different Locale site'

Run All Features:
behave

Generate Report : 

For Particular Feature:

behave -f allure_behave.formatter:AllureFormatter -o %allure_res
ult_folder% -n 'Go to different Locale site'

allure serve %allure_result_folder%

