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

class Test4mostliked():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_4mostliked(self):
    # Test name: 4_most_liked
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://brand.netray.id/")
    # 2 | setWindowSize | 1050x708 | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | css=.card-body > .justify-content-between | 
    self.driver.find_element(By.CSS_SELECTOR, ".card-body > .justify-content-between").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | runScript | window.scrollTo(0,1310) | 
    self.driver.execute_script("window.scrollTo(0,1310)")
    # 6 | click | css=.section:nth-child(7) .list-group-item:nth-child(6) .text-truncate | 
    self.driver.find_element(By.CSS_SELECTOR, ".section:nth-child(7) .list-group-item:nth-child(6) .text-truncate").click()
    # 7 | click | css=div:nth-child(2) > div > .d-flex > .custom-select | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > .d-flex > .custom-select").click()
    # 8 | select | css=div:nth-child(2) > div > .d-flex > .custom-select | label=Most Liked
    dropdown = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > .d-flex > .custom-select")
    dropdown.find_element(By.XPATH, "//option[. = 'Most Liked']").click()
    # 9 | click | css=.p-2 | 
    self.driver.find_element(By.CSS_SELECTOR, ".p-2").click()
    # 10 | close |  | 
    self.driver.close()
  
