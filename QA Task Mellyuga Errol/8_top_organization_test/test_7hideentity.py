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

class Test7hideentity():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_7hideentity(self):
    # Test name: 7_hide_entity
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://brand.netray.id/")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | css=.list-inline | 
    self.driver.find_element(By.CSS_SELECTOR, ".list-inline").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | runScript | window.scrollTo(0,1229) | 
    self.driver.execute_script("window.scrollTo(0,1229)")
    # 6 | click | css=.section:nth-child(5) .list-group-item:nth-child(6) .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".section:nth-child(5) .list-group-item:nth-child(6) .btn").click()
    # 7 | click | css=.text-right > .btn-danger | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-right > .btn-danger").click()
    # 8 | click | css=.branding | 
    self.driver.find_element(By.CSS_SELECTOR, ".branding").click()
    # 9 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 10 | close |  | 
    self.driver.close()
  
