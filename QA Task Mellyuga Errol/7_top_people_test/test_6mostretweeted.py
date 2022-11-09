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

class Test6mostretweeted():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_6mostretweeted(self):
    # Test name: 6_most_retweeted
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://brand.netray.id/")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | css=.topic-card-wrapper > .card-body | 
    self.driver.find_element(By.CSS_SELECTOR, ".topic-card-wrapper > .card-body").click()
    # 4 | runScript | window.scrollTo(0,24) | 
    self.driver.execute_script("window.scrollTo(0,24)")
    # 5 | runScript | window.scrollTo(0,2100) | 
    self.driver.execute_script("window.scrollTo(0,2100)")
    # 6 | click | css=.section:nth-child(4) .list-group-item:nth-child(6) .text-truncate | 
    self.driver.find_element(By.CSS_SELECTOR, ".section:nth-child(4) .list-group-item:nth-child(6) .text-truncate").click()
    # 7 | click | css=div:nth-child(2) > div > .d-flex > .custom-select | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > .d-flex > .custom-select").click()
    # 8 | select | css=div:nth-child(2) > div > .d-flex > .custom-select | label=Most Retweeted
    dropdown = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > .d-flex > .custom-select")
    dropdown.find_element(By.XPATH, "//option[. = 'Most Retweeted']").click()
    # 9 | click | css=.p-2 | 
    self.driver.find_element(By.CSS_SELECTOR, ".p-2").click()
    # 10 | close |  | 
    self.driver.close()
  
