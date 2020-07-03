
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




@when(u'the User makes POST request to API')
def step_impl(context):
    # img_name = 'chr.jpg'
    # requests.get("https://graph.microsoft.com/v1.0/me/drive/root/search(q='" + img_name + "')?select=name,id,webUrl" + headers={"Authorization":  config.authorization_token + }).text
    pass


@then(u'File uploaded successfuly to One Drive')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then File uploaded successfuly to One Drive')





@when(u'the User makes GET request to API')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the User makes GET request to API')


@then(u'File found successfuly on One Drive')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then File found successfuly on One Drive')

