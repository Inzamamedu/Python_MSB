# pip install selenium
# pip install webdriver-manager
# abu15-13075@diu.edu.bd
# msbacademywashiarnob7275924@

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

username = input("Enter your username: ")
password = input("Enter your password: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.msbask.com")
sleep(1)

loginbutton = driver.find_element_by_class_name("login")
loginbutton.click()

username_box = driver.find_element_by_id("popupLoginUser")
username_box.send_keys(username)

password_box = driver.find_element_by_id("popupLoginPassword")
username_box.send_keys(password)

fina_login_button = driver.find_element_by_id("popupLoginSubmit")
fina_login_button.click()
