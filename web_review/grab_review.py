'''
Name: grab_review.py
Description: Takes an input file with urls to the item page of amazon, grabs the reviews of each item and 
puts them in a seperate file: output<# of url line>.txt
Author: Benjamin Small
Date: 10/20/24
'''

#Selenium tools used
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

import threading          #for making thread for each url
import json               #for text conversion
import argparse           #for inputs                   


# ------------------------------------------------------------------------------------
# grabContents: creates a webdriver with selenium, waits for the review list to ------
# appear, then cycles through each review element grabbing the content and outputing -
# to given file destination. output<# of url>.txt ------------------------------------
# ------------------------------------------------------------------------------------
def grabContents(url, output) :
  opt = ChromiumOptions()
  opt.add_argument('--disable-gpu')
  #opt.add_experimental_option("detach", True) - makes the driver stay after finish unless .quit() called
  #opt.add_argument('--headless=new') - makes the contents of the webpage not interactable by user
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
    out_file = open(output, "w") # open file location

    #grab a list of all the review elements
    reviews = driver.find_elements(By.XPATH, "//span[@data-hook='review-body']")

    #cycle through list, grabs the text, then outputs to file, making sure its of json type
    for div in reviews :
      content = div.find_element(By.TAG_NAME, "span").text
      out_file.write(json.dumps(content) + "\n\n")
    
  driver.quit()


# ------------------------------------------------------------------------------------
# readReviews: takes an input file and reads the urls listed by line. Makes a thread -
# for each url and calls grabContents ------------------------------------------------
# ------------------------------------------------------------------------------------
def readReviews(input) :
  in_file = open(input, "r")
  i = 0
  threads = []

  for x in in_file :
    t = threading.Thread(target=grabContents, args=(x.strip(), ("output" + str(i) + ".txt")))
    threads.append(t)
    t.start()
    i+=1

  for t in threads:
    t.join()


# ------------------------------------------------------------------------------------
# Main function: uses argparser for input, calls readReviews -------------------------
# ------------------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(help="Enter filename for input urls", dest="input_dest", type=str)
  args = parser.parse_args()

  readReviews(args.input_dest)


# ------------------------------------------------------------------------------------
# Run the program --------------------------------------------------------------------
# ------------------------------------------------------------------------------------
if __name__=="__main__" :
  main()
