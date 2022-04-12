print("I'm running!:)")

from urllib import request
from bs4 import BeautifulSoup
import requests

url = "https://hdlbits.01xz.net/wiki/Special:VlgStats/D0E6464FFD2689EF"

requested_result = requests.get(url)

website = BeautifulSoup(requested_result.text, "html.parser")

### Uncomment me to output the prettified HTML output to a file ###
# with open("Backup Html Scrapes/body-scrape-html.txt", "w") as f:
#    f.writelines(website.prettify())
###################################################################

### Uncomment me to output the HTML text only(no tags) to output to a file ###
# with open("Backup Html Scrapes/body-scrape-html-text-only.txt", "w") as f:
#    f.writelines(website.get_text())
##############################################################################

print("I'm Done :)")