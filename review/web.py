from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

from abc import ABC, abstractmethod
import json

import argparse

# ----------------------------------------------------------------------------------------------------
# Basic Class for any webscrapper to have, incase change to new scapper besides Selenium -------------
# ----------------------------------------------------------------------------------------------------
class WebScrapper:
  @abstractmethod
  def __init__(self):
    pass
  def grab_contents(self, url):
    pass
  def return_contents(self):
    pass
  def write_to_file(self, output_path):
    pass

# ----------------------------------------------------------------------------------------------------
# Selenium Class: grab_contents, return_contents, and write_to_file ----------------------------------
# ----------------------------------------------------------------------------------------------------
class Selenium(WebScrapper) :
  def __init__(self):
    self.review_list = []

  # Grab contents takes an amazon url specifically and grabs the reviews, it returns a list of each
  # review. The review_list is also saved for looking at later
  def grab_contents(self, url) :
    opt = ChromiumOptions()
    opt.add_argument('--disable-gpu')
    opt.add_argument('--headless=new')
    driver = webdriver.Chrome(options=opt)

    driver.get(url) 
    wait = WebDriverWait(driver, 10) # defines the time to wait for

    try :
      # if the page asking for identification of not being a robot shows up
      wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Try different image"))).click() 
    except :
      pass
    finally :
      # wait until review list appears
      wait.until(EC.presence_of_element_located((By.ID, "cm-cr-dp-review-list")))

      #grab a list of all the review elements
      reviews = driver.find_elements(By.XPATH, "//span[@data-hook='review-body']")

      #cycle through list, grabs the text, then outputs to file, making sure its of json type
      for div in reviews :
        content = div.find_element(By.TAG_NAME, "span").text
        self.review_list.append(json.dumps(content).strip())
    
      driver.quit()
      return self.review_list
  
  # Returns the list of reviews, returns empty list if grab_contents hasn't been run
  def return_contents(self):
    return self.review_list

  #Takes a file path as input and writes the review_list to the file, line by line.
  def write_to_file(self, output_path):
    outfile = open(output_path, "w")
    for item in self.review_list :
      outfile.write(item + "\n")
    outfile.close()





# ----------------------------------------------------------------------------------------------------
# Main Function: takes file path as input and reads through urls one by one, using previous class it
# creates files for each url with its reviews ----------------------------------
# ----------------------------------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(help="Enter filename for input urls", dest="input_dest", type=str)
  args = parser.parse_args()


  input_file = open(args.input_dest, "r")
  i=0
  for url in input_file:
    sel = Selenium()
    sel.grab_contents(url)
    sel.write_to_file(("sel_out" + str(i) + ".txt"))
    i+=1
  input_file.close()


# ------------------------------------------------------------------------------------
# Run main ---------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
if __name__=="__main__" :
  main()