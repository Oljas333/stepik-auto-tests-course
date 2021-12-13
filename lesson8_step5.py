from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
       
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Oljas")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kussainov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname('C:\\Users\\1\\selenium_course_'))    
    file_path = os.path.join(current_dir, 'new.txt') 
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()
finally:
    time.sleep(10)
    browser.quit()
