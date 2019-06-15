from selenium import webdriver
import math
import time

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

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)

link = "https://stepik.org/catalog?auth=login&language=ru"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)
login = browser.find_element_by_xpath('//input[@id="id_login_email"]')
login.send_keys('9164455761@mail.ru')
password = browser.find_element_by_xpath('//input[@id="id_login_password"]')
password.send_keys('Aa15280323')
button = browser.find_element_by_tag_name('button')
button.click()
