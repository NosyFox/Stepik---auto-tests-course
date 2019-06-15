from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

#x_element = browser.find_element_by_xpath('//img["valuex"]')
x_element = browser.find_element_by_tag_name('img')
x_element_valuex = x_element.get_attribute('valuex')
#x = x_element_valuex
y = calc(x_element_valuex)

input = browser.find_element_by_id('answer')
input.send_keys(y)

option1 = browser.find_element_by_id('robotCheckbox')
option1.click()

option2 = browser.find_element_by_id('robotsRule')
option2.click()

button = browser.find_element_by_css_selector('button.btn')
button.click()
