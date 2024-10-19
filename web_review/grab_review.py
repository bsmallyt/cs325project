from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

def startDriver() :
  opt = ChromiumOptions()
  opt.add_experimental_option("detach", True)
  opt.add_argument('--disable-gpu')
  #opt.add_argument('--headless=new')

  driver = webdriver.Chrome(options=opt)
  driver.get("https://youtube.com")

  wait = WebDriverWait(driver, 30)
  wait.until(EC.presence_of_element_located((By.ID, "logo-icon")))

  driver.quit()

startDriver()