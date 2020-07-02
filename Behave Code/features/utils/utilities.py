from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select


# testing
import time

from selenium.common.exceptions import NoSuchElementException

def finds_elements_by_tag_attribute_value(driver, tag, attribute, value):
    try:
        elements = driver.find_elements_by_xpath('//'+tag+'[@'+attribute+'="' + value + '"]')

        return elements

    except NoSuchElementException:
        print("No elements found")

        
    # srch_fld.send_keys('test abc 2#')