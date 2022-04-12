print("I'm running!:)")

from urllib import request
from bs4 import BeautifulSoup
import requests

url = "https://hdlbits.01xz.net/wiki/Special:VlgStats/D0E6464FFD2689EF"

requested_result = requests.get(url)

website = BeautifulSoup(requested_result.text, "html.parser")

# This is a test of the body-scrape-code-body-gather branch.

### Uncomment me to output the prettified HTML output to a file ###
# with open("body-scrape-html.txt", "w") as f:
#    f.writelines(website.prettify())
###################################################################

### Uncomment me to output the HTML text only(no tags) to output to a file ###
# with open("body-scrape-html.txt", "w") as f:
#    f.writelines(website.get_text())
##############################################################################

print("I'm Done :)")