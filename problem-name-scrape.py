print("I'm running!:)")

from bs4 import BeautifulSoup
import requests

url = "https://hdlbits.01xz.net/wiki/Special:VlgStats/D0E6464FFD2689EF"

requested_result = requests.get(url)

website = BeautifulSoup(requested_result.text, "html.parser")

vlgstats = website.select(".vlgstat_link")

problems = [None] * len(vlgstats)

for x, data in enumerate(vlgstats):
    problems[x] = data.string

with open("Problems/problems.txt", "w") as f:
    for problem in problems:
        f.write(problem)
        f.write("\n")

###
### vlgstat_link is the unique propery that you can key off of!!! ###
###

### Uncomment me to output the prettified HTML output to a file ###
# with open("Backup Html Scrapes/problem-scrape-html.txt", "w") as f:
#    f.writelines(website.prettify())
###################################################################

### Uncomment me to output the HTML text only(no tags) to output to a file ###
# with open("Backup Html Scrapes/problem-scrape-html-text-only.txt", "w") as f:
#    f.writelines(website.get_text())
##############################################################################

print("I'm Done :)")