#!/usr/local/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_scores_service():
  browser = webdriver.Firefox(executable_path="/training/devops/geckodriver")
  browser.get('http://10.97.3.235:5000')
  elem = browser.find_element_by_id("score")
  score = elem.text
  print(score)
  browser.close()
  return score

def main_function():
   score  = int(test_scores_service())
   if score > 1 and score < 1000:
      print(f'you score is true')
   else:
      print(f'you score is false') 
 

if __name__ == '__main__':
 main_function()
