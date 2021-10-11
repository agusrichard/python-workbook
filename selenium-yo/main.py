import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_path, 'driver')
print(driver_path)
os.environ['PATH'] += f':{driver_path}'
print(os.environ.get('PATH'))

driver = webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(10)

try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping...')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')
sum1.send_keys(Keys.NUMPAD2, Keys.NUMPAD1)
sum2.send_keys(69)

get_total_btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
get_total_btn.click()
