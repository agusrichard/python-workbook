import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

base_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_path, 'driver')
print(driver_path)
os.environ['PATH'] += f':{driver_path}'
print(os.environ.get('PATH'))

driver = webdriver.Chrome()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.implicitly_wait(10)

title_element = driver.find_element_by_class_name('post-title')
assert title_element.text == 'Automate Selenium Practice Form'

firstname_input_element = driver.find_element_by_name('firstname')
firstname_input_element.send_keys('Sherlock')

lastname_input_element = driver.find_element_by_name('lastname')
lastname_input_element.send_keys('Holmes')

male_radiobutton = driver.find_element_by_id('sex-0')
male_radiobutton.click()

years_of_experience_radiobutton = driver.find_element_by_id('exp-6')
years_of_experience_radiobutton.click()

date_input = driver.find_element_by_id('datepicker')
date_input.send_keys('21/09/1997')

profession_checkbox_manual_tester = driver.find_element_by_id('profession-0')
profession_checkbox_manual_tester.click()

profession_checkbox_automation_tester = driver.find_element_by_id('profession-1')
profession_checkbox_automation_tester.click()

automation_tools_checkbox_selenium_driver = driver.find_element_by_id('tool-2')
automation_tools_checkbox_selenium_driver.click()

continents_dropdown_element = Select(driver.find_element_by_id('continents'))
continents_dropdown_element.select_by_visible_text('Europe')

selenium_commands_dropdown_element = Select(driver.find_element_by_id('selenium_commands'))
for elem in selenium_commands_dropdown_element.options:
    ActionChains(driver).key_down(Keys.CONTROL).click(elem).key_up(Keys.CONTROL).perform()

images_path = os.path.join(base_path, 'images', 'image.jpg')
upload_file_element = driver.find_element_by_id('photo')
upload_file_element.send_keys(images_path)

submit_button = driver.find_element_by_id('submit')
submit_button.click()