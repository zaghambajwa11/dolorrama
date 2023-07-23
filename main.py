from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import scrapper

# Set the path to your ChromeDriver executable. Download it from https://sites.google.com/a/chromium.org/chromedriver/downloads


# import get_store_ids function from scrapper.py
from scrapper import get_store_ids
# get matches from scrapper.py
matches = get_store_ids()


# create a function for all below code
def fill_form(store_id):
    chromedriver_path = '/Users/macbookpro/Downloads/chromedriver_mac64/chromedriver'

# Create a new instance of Chrome WebDriver
    driver = webdriver.Chrome()
    url = 'https://www.dollarama.com/en-CA/corp/careers/store-position-application-form?position=SA&storeid='+store_id  # Replace with the URL of the webpage you want to fill data on

    driver.get(url)

# Add a wait to let the page load (you may need to adjust the time based on the page)
    time.sleep(2)

    input_element = driver.find_element("name","firstname")
    text_to_fill = "Zara"  # Replace "John" with the desired first name
    input_element.send_keys(text_to_fill)

    input_element = driver.find_element("name","lastname")
    text_to_fill = "Shahid"  # Replace "Doe" with the desired last name
    input_element.send_keys(text_to_fill)

    input_element = driver.find_element("name","email")
    text_to_fill = "zarashahid149@gmail.com"
    input_element.send_keys(text_to_fill)

    input_element = driver.find_element("name","phone")
    text_to_fill = "306-351-0952"
    input_element.send_keys(text_to_fill)


    language = Select(driver.find_element("name", "plang"))
    language.select_by_value('English')

    job_type= Select(driver.find_element("name", "type"))
    job_type.select_by_value('Full-time')

    radius= Select(driver.find_element("name", "radius"))
    radius.select_by_value('Yes, within a 30km radius')

    legal= Select(driver.find_element("name", "legally-authorized"))
    legal.select_by_value('Yes')

    employed= Select(driver.find_element("name", "previously-employed"))
    employed.select_by_value('Yes')

    exp_retail= Select(driver.find_element("name", "exp_retail"))
    exp_retail.select_by_value('3 years or more')

    ladders= Select(driver.find_element("name", "ladders"))
    ladders.select_by_value('Yes')


    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# write a for loop to iterate over the days list
    for day in days:
    # find element by id
    # Using the 'name' attribute as the locator
        available_work_from_mon = Select(driver.find_element("name", "available_work_from_" + day))
        available_work_to_mon = Select(driver.find_element("name", "available_work_to_" + day))

    # Select an option by its value
        from_value = '6:00 AM'  # Replace 'option_value_to_select' with the value of the option you want to choose
        available_work_from_mon.select_by_value(from_value)
        to_value = '11:00 PM'  # Replace 'option_value_to_select' with the value of the option you want to choose
        available_work_to_mon.select_by_value(to_value)


    file_path = '/Users/macbookpro/Documents/General/Zara_Shahid_Resume.pdf'


# form_input = driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()
    time.sleep(3)

# flie dialog is opened and we need to write the file path and press enter in macos
    form_element = driver.find_element(By.CLASS_NAME, 'form-control')

# Remove the 'disabled' attribute to enable the input element
    driver.execute_script("arguments[0].removeAttribute('disabled')", form_element)

# Set the file path to the input element using execute_script
    driver.execute_script(f"arguments[0].value = '{file_path}';", form_element)

# click on the checkbox with name concent
    checkbox_element = driver.find_element("name","consent").click()


    submit_btn = driver.find_element(By.CLASS_NAME, 'wpcf7-form-control.has-spinner.wpcf7-submit.btn.btn-success.btn-lg').click()


    time.sleep(5)

# Close the browser
    driver.quit()




for match in matches:
    fill_form(match)
    



