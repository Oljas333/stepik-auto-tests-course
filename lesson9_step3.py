from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    pushbutton = browser.find_element(By.CSS_SELECTOR, ".btn") 
    pushbutton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    x=int(x)
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

        
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()
finally:
    time.sleep(10)
    browser.quit()
