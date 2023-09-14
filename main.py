from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.get("https://mresearchsurveyengine.modernsurvey.com/Survey.aspx?cc=en-US&cid=F70C1DCB-EDB2-49D5-9AF6-05840A2B3105&Page=2")

# Click the continue button on the first page
continue_button = driver.find_element(By.XPATH, value='//*[@id="ctl00_body_p_SaveAndContinueButton"]')
continue_button.click()

time.sleep(2)

def click_radiobutton(driver, row, clicked):
    while True:
        try:
            point = random.randint(2, 6)
            xpath = f'//*[@id="ctl00_body_F70C1DCB-EDB2-49D5-9AF6-05840A2B3105_{row}_{point}"]'
            radio_button = driver.find_element(By.XPATH, xpath)
            radio_button.click()
            print(f'Clicking row number {row}, It was clicked {clicked + 1} times.')
            return True
        except NoSuchElementException:
            print(f'Row {row} not found, trying again.')
            time.sleep(0.1)

def click_next():
    while True:
        try:
            next_button = driver.find_element(By.XPATH, value='//*[@id="ctl00_body_p_SaveAndContinueButton"]')
            next_button.click()
            print('Next button clicked')
            return True
        except NoSuchElementException:
            time.sleep(0.2)

row = 4
clicked = 0

while True:
    time.sleep(0.1)
    if click_radiobutton(driver, row, clicked):
        row += 1
        clicked += 1

    if clicked % 6 == 0:
        if click_next():
            pass
    elif clicked == 47:
        click_next()
        break
click_next()

row = 138
while True:
    if click_radiobutton(driver, row, clicked):
        row += 1
        clicked += 1
    if clicked == 52:
        click_next()
        break

# Close the browser window when done
#driver.quit()