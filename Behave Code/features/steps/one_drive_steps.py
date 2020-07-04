
from behave import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

import time

from selenium.common.exceptions import NoSuchElementException

# Utilities

import sys
sys.path.insert(0, '/home/scarlet/Projects/Automation/Assesment/Py Assesment/1/Behave Code/features/utils')
import utilities

import config

import pyautogui


@given('the User is navigates to One Drive page')
def navigate_to_one_drive(context):
    driver = context.driver

    driver.get('https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage')
    
    time.sleep(5)
    
@given('selects Locale') 
def select_locale(context): 
    driver = context.driver

    try:
        locale_btn = driver.find_element_by_id('dynamicmarketredirect-dialog-submit')
    except NoSuchElementException:
        print("No elements found")
    
    locale_btn.click()

    time.sleep(5)


@when('the User clicks Sign In')
def click_sign_in(context):
    driver = context.driver

    try:
        sign_in_btn = driver.find_element_by_partial_link_text('Sign in')
    except NoSuchElementException:
        print("No elements found")
    
    sign_in_btn.click()

    time.sleep(5)


@when('the User enters email in E-mail field')
def enter_email(context):
    context.driver.switch_to.frame(context.driver.find_element_by_css_selector('iframe[class="SignIn"]'))

    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'type', 'email')[0].send_keys(config.email)


@when('submits email')
def submit_email(context):
    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'type', 'submit')[0].click()

    time.sleep(5)

@when('the User enters password in Password field')
def enter_password(context):
    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'name', 'passwd')[0].send_keys(config.password)

@when('submits password')
def submit_pass(context):
    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'type', 'submit')[0].click()
    time.sleep(20)

@when('One Drive is shown')
def one_drive_shown(context):
    assert context.driver.title=='My files - OneDrive'


@when('the User clicks the Upload File dropdown menu')
def click_up_file_dd_menu(context):
    utilities.finds_elements_by_tag_attribute_value(context.driver, 'button', 'name', 'Upload')[0].click()


@when('selects Files from dropdown menu')
def selects_files(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), 'Files')]")[8].click()

@when('select File to Upload')
def locate_and_select_file(context):
    # Linux Mint Config
    # File has to exist in path : /home/scarlet/0/0.txt

    

    pyautogui.doubleClick(x=221, y=146)
    pyautogui.doubleClick(x=221, y=146)

    time.sleep(10)



@then('file is uploaded')
def file_uploaded(context):

    assert driver.title == 'My files - OneDrive' 


@when('the User enters incorrect email in E-mail field')
def enter_incorrect_email(context):
    context.driver.switch_to.frame(context.driver.find_element_by_css_selector('iframe[class="SignIn"]'))

    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'type', 'email')[0].send_keys(config.incorrect_email)


@then ('incorrect email error message is shown')
def incorr_email_error_msg(context):
    # context.driver.switch_to.frame(context.driver.find_element_by_css_selector('iframe[class="SignIn"]'))

    assert context.driver.find_elements_by_class_name('alert')[0].text == "We couldn't find an account with that email address or phone number. Would you like to sign up for a new Microsoft account? Sign up"


@when('the User enters incorrect password in Password field')
def enter_password(context):
    utilities.finds_elements_by_tag_attribute_value(context.driver, 'input', 'name', 'passwd')[0].send_keys(config.incorrect_password)




@then ('incorrect password error message is shown')
def incorr_pass_error_msg(context):
    # context.driver.switch_to.frame(context.driver.find_element_by_css_selector('iframe[class="SignIn"]'))

    time.sleep(60)

    assert bool(context.driver.find_elements_by_class_name('alert-error')) == True




@given('the User is navigates to One Drive page with selected locale')
def navigate_to_one_drive(context):
    driver = context.driver

    driver.get('https://www.microsoft.com/' + config.country + '/microsoft-365/onedrive/online-cloud-storage')
    
    time.sleep(5)




@given('selects custom Locale') 
def select_custom_locale(context): 
    driver = context.driver

    try:
        locale_btn = driver.find_element_by_id('dynamicmarketredirect-dialog-close')
    except NoSuchElementException:
        print("No elements found")
    
    locale_btn.click()

    time.sleep(5)


    

@then ('One Drive site is shown')
def one_drive_shown(context):
        # time.sleep(20)
        assert context.driver.current_url == 'https://www.microsoft.com/' + config.country + '/microsoft-365/onedrive/online-cloud-storage'




