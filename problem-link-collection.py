print("I'm runnning")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
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
    stats = driver.find_element(By.ID,'n-My-Stats')

    action = ActionChains(driver)
    action.move_to_element(name_dropdown).perform()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'n-My-Stats')))
    action.move_to_element(stats).click().perform()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')))

def make_code_visible(driver):

    load_button = driver.find_element(By.ID,'uiload_load')
    
    select = Select(driver.find_element(By.ID,'uiload_select'))
    action = ActionChains(driver)

    load_button.location_once_scrolled_into_view
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'uiload_load')))
    select.select_by_value('0')
    action.move_to_element(load_button).click().perform()
    time.sleep(2) # This sleep is gross but not easy to defeat. Leaving as is for now because I cannot find consistent way to trigger if my HDL is loaded. I THINK to fix I would need to use beautifulsoup to extract code in beginning and then do it again after hitting load button then compare in a whiiile loop.
    

#WebDriverWait(driver,10).until(EC.url_matches(('www.pausethescriptrighthereanddontgoanywhere.com')))

def gather_code(driver):
    
    with open("VHDL-HTML/temp.html", "w") as temp_get:
        temp_get.writelines(driver.page_source)

    with open("VHDL-HTML/temp.html", "r") as temp_read:
        soup = BeautifulSoup(temp_read, "html.parser")
        
    CodeMirrorLines = soup.find_all("pre", class_="CodeMirror-line")

    for line in CodeMirrorLines:
        for text in line.next_element.contents:
            print(text.string, end="")
        print()

    print()

def scrape(driver):
    links = driver.find_elements(By.CLASS_NAME,"vlgstat_link")
    action = ActionChains(driver)

    for link in links[0:5]:
        link.location_once_scrolled_into_view
        WebDriverWait(driver,10).until(EC.visibility_of(link))
        action.move_to_element(link).click().perform()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'hb-box')))
        make_code_visible(driver)
        #gathered_code =
        gather_code(driver)
        #store_code(gathered_code)
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')))

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Special:VlgLogin")

login(driver)

go_to_stats(driver)

scrape(driver)

# driver.close()
 
print("I'm done :)")