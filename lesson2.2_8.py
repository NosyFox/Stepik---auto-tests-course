from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys('Александр')
input2 = browser.find_element_by_name('lastname')
input2.send_keys('Барышев')
input3 = browser.find_element_by_name('email')
input3.send_keys('sashok@stepik.org')

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__)) 
# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_tag_name('button')
button.click()