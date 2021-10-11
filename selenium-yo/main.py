import os
from selenium import webdriver

base_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_path, 'driver')
print(driver_path)
os.environ['PATH'] += f':{driver_path}'
print(os.environ.get('PATH'))

driver = webdriver.Chrome()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.implicitly_wait(10)