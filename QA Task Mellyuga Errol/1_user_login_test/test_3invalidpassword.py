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

class Test3invalidpassword():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_3invalidpassword(self):
    # Test name: 3_invalid_password
    # Step # | name | target | value
    # 1 | open | /login?redirect=%2F | 
    self.driver.get("https://brand.netray.id/login?redirect=%2F")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 4 | type | id=username | mellyuga
    self.driver.find_element(By.ID, "username").send_keys("mellyuga")
    # 5 | click | css=form | 
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    # 6 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 7 | type | id=password | qwerty12345
    self.driver.find_element(By.ID, "password").send_keys("qwerty12345")
    # 8 | click | id=loginButton | 
    self.driver.find_element(By.ID, "loginButton").click()
    # 9 | click | css=.close | 
    self.driver.find_element(By.CSS_SELECTOR, ".close").click()
    # 10 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 11 | type | id=password | qwerty1234
    self.driver.find_element(By.ID, "password").send_keys("qwerty1234")
    # 12 | click | id=loginButton | 
    self.driver.find_element(By.ID, "loginButton").click()
    # 13 | mouseOver | id=loginButton | 
    element = self.driver.find_element(By.ID, "loginButton")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | close |  | 
    self.driver.close()
  
