print("I'm runnning")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

def login(driver):
    username_element = driver.find_element(By.NAME,"vlg_username")
    password_element = driver.find_element(By.NAME,"password")
    login_element = driver.find_element(By.NAME,"login")

    username = "trevortaulien"
    password = "trevor_bits_taulien"

    username_element.send_keys(username)
    password_element.send_keys(password)
    login_element.send_keys(Keys.RETURN)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="hcuser"]')))

def go_to_stats(driver):
    name_dropdown = driver.find_element(By.XPATH,'/html/body/div[1]/nav/section/ul[1]/li[4]/a') 
    stats = driver.find_element(By.XPATH,'/html/body/div[1]/nav/section/ul[1]/li[4]/ul/li[4]/a')

    action = ActionChains(driver)
    action.move_to_element(name_dropdown).perform()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/section/ul[1]/li[4]/ul/li[4]/a')))
    action.move_to_element(stats).click().perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')))

def travel_to_each_problem(driver):
    links = driver.find_elements(By.CLASS_NAME,"vlgstat_link")
    action = ActionChains(driver)

    for link in links:
        link.location_once_scrolled_into_view
        action.move_to_element(link).click().perform()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'hb-box')))
        print(link)    
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')))

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Special:VlgLogin")

login(driver)

go_to_stats(driver)

travel_to_each_problem(driver)

# driver.close()
 
print("I'm done :)")