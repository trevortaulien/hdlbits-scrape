print("I'm running :)")

#############################################################################################################
# The purpose of this .py is to get the html from hdlbits as it is seen from the Chrome inspector           #
# this is necessary because hdlbits uses CodeMirror which is a javascript text editor that the user         #
# types verilog into. When using beautifulsoup to gather the html the only thing returned is CodeMirror.js  #
# Selenium returns the html as seen in the Chrome inspector.                                                #
# This .py file gets the html as seen in Chrome inspector using selenium then opens the html as a           #
# beautiful soup object to be prettified because selenium returns a lot of the html inline, and so that     #
# further operations can be preformed using beautifulsoup.                                                  #
#############################################################################################################

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://hdlbits.01xz.net/wiki/Vector100r")
driver.implicitly_wait(1)

with open("Selenium Testing/seleniumPageSourceTest.html", "w") as s:
    s.writelines(driver.page_source)

driver.close()

with open("Selenium Testing/seleniumPageSourceTest.html", "r") as r:
    website = BeautifulSoup(r,"html.parser")

with open("Selenium Testing/seleniumPageSourcePretty.txt","w") as p:
    p.writelines(website.prettify())

###
### CodeMirror-line appears to be the class name that contains the information for each line of code
### may also have to loop off of the class CodeMirror-code as it is the class(?) that contains all
### of the CodeMirror-line elements
###

### driver.page_source can be used to get all html info that can be seen with chrome inspection!!!

print("I'm done :)")