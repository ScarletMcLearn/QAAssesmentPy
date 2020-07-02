from behave import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select


# testing
import time

from selenium.common.exceptions import NoSuchElementException

# Utilities

import sys
sys.path.insert(0, '/home/scarlet/Projects/Automation/Assesment/Py Assesment/1/Behave Code/features/utils')
import utilities


@given(u'the User is on Google home page')
def step_impl(context):
    context.driver.get('https://www.google.com')

    # time.sleep(50)


@when(u'User enters search terms in search bar')
def step_impl(context):
    driver = context.driver

    srch_fld = utilities.finds_elements_by_tag_attribute_value(driver, 'input', 'name', 'q')[0]
   
        
    srch_fld.send_keys('test abc 2#')



    


@when(u'clicks search button')
def step_impl(context):
    driver = context.driver

    srch_btn = utilities.finds_elements_by_tag_attribute_value(driver, 'input', 'value', 'Google সার্চ')[1]

    srch_btn.send_keys('\n')
    
    


@then(u'search results are shown')
def step_impl(context):
    context.driver.find_elements_by_class_name('r')
    
