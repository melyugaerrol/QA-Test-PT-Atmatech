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

class Test5signupemptytextbox():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_5signupemptytextbox(self):
    # Test name: 5_sign_up_empty_text_box
    # Step # | name | target | value
    # 1 | open | /login?redirect=%2F | 
    self.driver.get("https://brand.netray.id/login?redirect=%2F")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | id=signupButton | 
    self.driver.find_element(By.ID, "signupButton").click()
    # 4 | click | id=fullnameField | 
    self.driver.find_element(By.ID, "fullnameField").click()
    # 5 | click | id=usernameField | 
    self.driver.find_element(By.ID, "usernameField").click()
    # 6 | click | id=emailField | 
    self.driver.find_element(By.ID, "emailField").click()
    # 7 | click | id=passwordField | 
    self.driver.find_element(By.ID, "passwordField").click()
    # 8 | click | id=confirmPasswordField | 
    self.driver.find_element(By.ID, "confirmPasswordField").click()
    # 9 | click | id=phoneField | 
    self.driver.find_element(By.ID, "phoneField").click()
    # 10 | click | css=.card-body | 
    self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
    # 11 | click | css=.mb-3 > .custom-control-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".mb-3 > .custom-control-label").click()
    # 12 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 13 | click | css=.recaptcha-checkbox-border | 
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    # 14 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 15 | mouseOver | id=registerButton | 
    element = self.driver.find_element(By.ID, "registerButton")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 16 | click | id=registerButton | 
    self.driver.find_element(By.ID, "registerButton").click()
    # 17 | mouseOut | id=registerButton | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 18 | runScript | window.scrollTo(0,155) | 
    self.driver.execute_script("window.scrollTo(0,155)")
    # 19 | close |  | 
    self.driver.close()
  
