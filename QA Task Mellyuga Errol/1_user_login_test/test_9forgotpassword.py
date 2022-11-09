# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test9forgotpassword():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_9forgotpassword(self):
    # Test name: 9_forgot_password
    # Step # | name | target | value
    # 1 | open | /login?redirect=%2F | 
    self.driver.get("https://brand.netray.id/login?redirect=%2F")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 4 | type | id=username | mellyuga
    self.driver.find_element(By.ID, "username").send_keys("mellyuga")
    # 5 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | type | id=password | 12345
    self.driver.find_element(By.ID, "password").send_keys("12345")
    # 7 | click | id=loginButton | 
    self.driver.find_element(By.ID, "loginButton").click()
    # 8 | mouseOver | id=loginButton | 
    element = self.driver.find_element(By.ID, "loginButton")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | click | id=forgotButton | 
    self.driver.find_element(By.ID, "forgotButton").click()
    # 10 | click | id=userFullName | 
    self.driver.find_element(By.ID, "userFullName").click()
    # 11 | type | id=userFullName | mellyuga
    self.driver.find_element(By.ID, "userFullName").send_keys("mellyuga")
    # 12 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 13 | click | css=.recaptcha-checkbox-border | 
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    # 14 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 15 | click | id=sendResetEmailButton | 
    self.driver.find_element(By.ID, "sendResetEmailButton").click()
    # 16 | mouseOver | id=sendResetEmailButton | 
    element = self.driver.find_element(By.ID, "sendResetEmailButton")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 17 | click | css=.notif-alert | 
    self.driver.find_element(By.CSS_SELECTOR, ".notif-alert").click()
    # 18 | click | css=.notif-alert > .close | 
    self.driver.find_element(By.CSS_SELECTOR, ".notif-alert > .close").click()
    # 19 | close |  | 
    self.driver.close()
  
