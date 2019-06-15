from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

wait = WebDriverWait(browser, 14)
price = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))

b = browser.find_element_by_id('book')
b.click()

def calc(x):
	return str(math.log(abs(12*math.sin(x))))
x = int(browser.find_element_by_id('input_value').text)
res = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(res)

button = browser.find_element_by_id('solve')
button.click()