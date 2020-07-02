from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


from config import *

import time 

# Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver

def get_firefox_with_cache_cleared():
    profile = FirefoxProfile()
    profile.set_preference('browser.cache.disk.enable', False)
    profile.set_preference('browser.cache.memory.enable', False)
    profile.set_preference('browser.cache.offline.enable', False)
    profile.set_preference('network.cookie.cookieBehavior', 2)

    driver = webdriver.Firefox(executable_path=r'/home/scarlet/Projects/PyEnvs/WebScrapingEnv/geckodriver', firefox_profile=profile)

    driver.maximize_window()
    return driver

# Chrome
def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")


def get_chrome_with_cache_cleared():
    # ADD Chrome Driver Path Variable Here
     driver = webdriver.Chrome(executable_path='/home/scarlet/Projects/PyEnvs/WebScrapingEnv/chromedriver', chrome_options=chrome_options)      # Chrome Driver Path 
     # clear_cache(context.driver)

     return driver
    
def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    #  # ADD Chrome Driver Path Variable Here
    #  context.driver = webdriver.Chrome(executable_path='/home/scarlet/Projects/PyEnvs/WebScrapingEnv/chromedriver', chrome_options=chrome_options)      # Chrome Driver Path 
    #  # clear_cache(context.driver)

     if (cookies == 'off'):
          if (browser == 'chrome'):
               context.driver = get_chrome_with_cache_cleared()
          elif (browser == 'firefox'):
               context.driver = get_firefox_with_cache_cleared()
     elif (cookies == 'on'):
          if (browser == 'chrome'):
               context.driver =  webdriver.Chrome(executable_path='/home/scarlet/Projects/PyEnvs/WebScrapingEnv/chromedriver')
          elif (browser == 'firefox'):
               context.driver = webdriver.Firefox(executable_path=r'/home/scarlet/Projects/PyEnvs/WebScrapingEnv/geckodriver')

    #  time.sleep(5)
     context.driver.implicitly_wait(10)
     
     print("Before scenario\n")

def after_scenario(context,scenario):
     context.driver.quit()
     print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):
     print("Executing after all")


# Added New
take_screenshot = False 

def after_step(context, step):
     if take_screenshot:
          if step.status == "failed":
               context.driver.save_screenshot(context.scenario.name + " " + step.name + ".png")























def get_clear_cache_button(driver):
    return driver.find_element_by_css_selector('#clearCacheButton')


def get_clear_site_data_button(driver):
    return driver.find_element_by_css_selector('#clearSiteDataButton')


def clear_firefox_cache(driver, timeout=10):
    driver.get('about:preferences#privacy')
    wait = WebDriverWait(driver, timeout)
    # Click the "Clear Now" button under "Cached Web Content"
    wait.until(get_clear_cache_button)
    get_clear_cache_button(driver).click()
    # Click the "Clear All Data" button under "Site Data" and accept the alert
    wait.until(get_clear_site_data_button)
    get_clear_site_data_button(driver).click()
    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()