from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id('input_value').text
y = calc(x)

input = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)

robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()

robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()

button = browser.find_element_by_tag_name('button')
button.click()
