print("I'm runnning")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Special:VlgLogin")

username_element = driver.find_element_by_name("vlg_username")
password_element = driver.find_element_by_name("password")
login_element = driver.find_element_by_name("login")

username = "trevortaulien"
password = "trevor_bits_taulien"

username_element.send_keys(username)
password_element.send_keys(password)
login_element.send_keys(Keys.RETURN)

print("I'm done :)")