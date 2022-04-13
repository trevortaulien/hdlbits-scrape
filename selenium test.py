print("I'm running :)")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Vector100r")
driver.implicitly_wait(1)
line = driver.find_element(By.CLASS_NAME, "CodeMirror-line")
# print(driver.page_source)
driver.close()

###
### CodeMirror-line appears to be the class name that contains the information for each line of code
### may also have to loop off of the class CodeMirror-code as it is the class(?) that contains all
### of the CodeMirror-line elements
###

### driver.page_source can be used to get all html info that can be seen with chrome inspection!!!

print("I'm done :)")