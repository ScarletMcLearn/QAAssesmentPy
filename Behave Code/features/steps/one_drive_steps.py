
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

