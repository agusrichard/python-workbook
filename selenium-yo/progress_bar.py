import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


base_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_path, 'driver')
print(driver_path)
os.environ['PATH'] += f':{driver_path}'
print(os.environ.get('PATH'))

driver = webdriver.Chrome()
driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(10)

download_button = driver.find_element_by_id('downloadButton')
download_button.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)

print('Achieved')