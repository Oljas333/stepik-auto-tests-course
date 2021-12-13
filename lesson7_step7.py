from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_class_name("nowrap")
    x_element = x_element.get_attribute("input_value")
    
   
    x = x_element
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()
finally:
    time.sleep(20)
    browser.quit()