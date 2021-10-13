# Learn Selenium

## Contents:
- `click`: To click (obviously, duh!)
  ```python
  male_radiobutton = driver.find_element_by_id('sex-0')
  male_radiobutton.click()
  ```
- `send_keys`: To type / fill in some input text
  ```python
  firstname_input_element = driver.find_element_by_name('firstname')
  firstname_input_element.send_keys('Sherlock')
  ```
- Select dropdown:
  ```python
  continents_dropdown_element = Select(driver.find_element_by_id('continents'))
  continents_dropdown_element.select_by_visible_text('Europe')
  ```
- Multiple select:
  ```python
  selenium_commands_dropdown_element = Select(driver.find_element_by_id('selenium_commands'))
  for elem in selenium_commands_dropdown_element.options:
      ActionChains(driver).key_down(Keys.CONTROL).click(elem).key_up(Keys.CONTROL).perform()
  ```
- Upload file:
  ```python
  images_path = os.path.join(base_path, 'images', 'image.jpg')
  upload_file_element = driver.find_element_by_id('photo')
  upload_file_element.send_keys(images_path)
  ```
- Implicit wait:
  ```python
  driver.implicitly_wait(10)
  ```
- Explicit wait:
  ```python
  WebDriverWait(driver, 30).until(
      EC.text_to_be_present_in_element(
          (By.CLASS_NAME, 'progress-label'),
          'Complete!'
      )
  )
  ```
- Typing keys with keyboard:
  ```python
  sum1.send_keys(Keys.NUMPAD2, Keys.NUMPAD1)
  ```

## References:
- https://www.techlistic.com/p/selenium-practice-form.html