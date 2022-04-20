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

start_time = time.time()

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

def visible_code_capture(driver):

    with open("temp.html", "w") as temp_write:
        temp_write.writelines(driver.page_source)

    with open("temp.html", "r") as temp_read:
        soup = BeautifulSoup(temp_read, "html.parser")

    CodeMirrorLines = soup.find_all("pre", class_="CodeMirror-line")

    gathered_code = []

    for line in CodeMirrorLines:
        for text in line.next_element.contents:
            gathered_code.append(text.string)
        gathered_code.append('\n')

    return gathered_code

def make_code_visible(driver):

    load_button = driver.find_element(By.ID,'uiload_load')
    select = Select(driver.find_element(By.ID,'uiload_select'))
    action = ActionChains(driver)
    pre_load_capture = visible_code_capture(driver)
    load_button.location_once_scrolled_into_view
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'uiload_load')))
    select.select_by_index('1')
    action.move_to_element(load_button).click().perform()
    while(pre_load_capture == visible_code_capture(driver)):
        pass #should this be a continue?
    #time.sleep(2) # This sleep is gross but not easy to defeat. Leaving as is for now because I cannot find consistent way to trigger if my HDL is loaded. I THINK to fix I would need to use beautifulsoup to extract code in beginning and then do it again after hitting load button then compare in a whiiile loop.
   
def gather_and_store(driver, problem_number):
    
    with open("temp.html", "w") as temp_write:
        temp_write.writelines(driver.page_source)

    with open("temp.html", "r") as temp_read:
        soup = BeautifulSoup(temp_read, "html.parser")
        
    CodeMirrorLines = soup.find_all("pre", class_="CodeMirror-line")

    gathered_code = []

    for line in CodeMirrorLines:
        for text in line.next_element.contents:
            gathered_code.append(text.string)
        gathered_code.append('\n')

    # for i, random_none in enumerate(gathered_code):
    #     if random_none == None:
    #         gathered_code[i] = ""

    problem_name = soup.find("h2").string
    problem_name = problem_name.strip().replace("/","_")

    with open("HDL/" + str(problem_number + 1) + ". " + problem_name + ".v", "w") as file:
        for element in gathered_code:
            file.write(element)

def scrape(driver):
    links = driver.find_elements(By.CLASS_NAME,"vlgstat_link")
    action = ActionChains(driver)

    for problem_number, link in enumerate(links):
        link.location_once_scrolled_into_view
        WebDriverWait(driver,10).until(EC.visibility_of(link))
        action.move_to_element(link).click().perform()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'hb-box')))
        make_code_visible(driver)
        gather_and_store(driver, problem_number)
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')))

#WebDriverWait(driver,10).until(EC.url_matches(('www.pausethescriptrighthereanddontgoanywhere.com')))

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Special:VlgLogin")

login(driver)

go_to_stats(driver)

scrape(driver)

driver.close()

print("%s seconds " %(time.time() - start_time)) # First sucessful run took 748.3380181789398 seconds using sleep()
print("I'm done :)")