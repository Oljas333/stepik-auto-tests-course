from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math
def sum(x,y):
      return str(x + y)
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    
    x=int(x)
    y=int(y)
    sum_el = str(x + y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum_el)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click() 
finally:
    time.sleep(5)
    browser.quit()