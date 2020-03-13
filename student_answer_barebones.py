import unittest
import time
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from LOCELEMENT import LOCELEMENT;




def capabilities ():
    PATH = "/Users/ivantay/Automation/Appium/helomaven/PythonAppiumHello/apk/selendroid-test-app.apk"
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Nexus_5X_API_25'
    desired_caps['appPackage'] = 'com.google.android.youtube'
    desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'
    desired_caps['noReset'] = 'true'
    desired_caps['forceMjsonwp'] = 'true'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver = capabilities()
wait = WebDriverWait(driver, 20)
LOCELEMENT = LOCELEMENT()

#search text
text ="Ivan Tay Selenium Automation"


driver.find_element_by_accessibility_id(LOCELEMENT.LOC_NAV_SEARCH_ACC).click()
driver.find_element_by_id(LOCELEMENT.LOC_SEARCH_INPUT_ID).send_keys(text + "\n")
driver.press_keycode(66)


#click on 2nd video
xpath1 = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/results']/android.view.ViewGroup";

try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath1))
    )
except TimeoutException:
    print("Time out. Cannot find list in here ")
    driver.quit()

elements=driver.find_elements_by_xpath(xpath1)

#Click pause and play
elements[2].click()
time.sleep(4)
driver.find_element_by_xpath(LOCELEMENT.LOC_VIEWER_VIEWER_XPATH).click()
driver.find_element_by_xpath(LOCELEMENT.LOC_VIEWER_VIEWER_XPATH).click()
time.sleep(10)
driver.find_element_by_id(LOCELEMENT.LOC_VIEWER_PLAY_ID).click()
time.sleep(4)

#quit
driver.quit()
