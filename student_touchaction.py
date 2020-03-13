import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#desired capabilities
def capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Nexus_5X_API_25'
    desired_caps['appPackage'] = 'com.google.android.youtube'
    desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.application.Shell$HomeActivity'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver = capabilities()
wait = WebDriverWait(driver, 20)

title_id = "com.google.android.youtube:id/title"

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, title_id)))

action = TouchAction(driver)
action.press(None, 0, 1700, None).wait(None).move_to(None, 0, 50).release().perform()


#quit
time.sleep(10)
driver.quit()
