import unittest
import time
from appium import webdriver
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


def IsPresence (by, elementid):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((by, elementid)))

    return element

def click (by, elementid):
    element = IsPresence(by, elementid)
    element.click();
    return element

def sendKeys (by, elementid, text):
    element = IsPresence(by,elementid)
    element.clear();
    element.send_keys (text + " \n")
    driver.press_keycode(66)



driver = capabilities()
wait = WebDriverWait(driver, 20)
LOCELEMENT = LOCELEMENT ();

#search text
text ="Ivan Tay Selenium Automation"



click(MobileBy.ACCESSIBILITY_ID,LOCELEMENT.LOC_NAV_SEARCH_ACC)
sendKeys(By.ID,LOCELEMENT.LOC_SEARCH_INPUT_ID,text)

#click on 2nd video
xpath1 = "//android.support.v7.widget.RecyclerView[@resource-id='com.google.android.youtube:id/results']/android.view.ViewGroup";
IsPresence(By.XPATH,xpath1);
elements=driver.find_elements_by_xpath(xpath1)

#Click pause and play
elements[2].click()
time.sleep(4)
click(By.XPATH , LOCELEMENT.LOC_VIEWER_VIEWER_XPATH)
click(By.XPATH , LOCELEMENT.LOC_VIEWER_VIEWER_XPATH)
time.sleep(10)
click(By.ID , LOCELEMENT.LOC_VIEWER_PLAY_ID)
time.sleep(4)

#quit
driver.quit()
