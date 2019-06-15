from selenium import webdriver
import math


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_tag_name('button')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
	return str(math.log(abs(12*math.sin(x))))
x = int(browser.find_element_by_id('input_value').text)
res = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(res)

button = browser.find_element_by_tag_name('button')
button.click()