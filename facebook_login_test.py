import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https:www.facebook.com")

user = input("Insert login e-mail: ")

password = input("Insert password: ")

driver.find_element_by_id("email").send_keys(user)

driver.find_element_by_id("pass").send_keys(password)

driver.find_element_by_id('loginbutton').click()