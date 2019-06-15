from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

element_x = browser.find_element_by_xpath('//span[@id="num1"]')
x = element_x.text
element_y = browser.find_element_by_xpath('//span[@id="num2"]')
y = element_y.text
sum = int(x) + int(y)

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(str(sum)) # ищем элемент с текстом "sum"

button = browser.find_element_by_tag_name('button')
button.click()
