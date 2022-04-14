print("I'm running :)")

from bs4 import BeautifulSoup

with open("seleniumPageSourcePretty.txt", "r") as w:
    website = BeautifulSoup(w, "html.parser")

#CodeMirrorLines = website.select(".CodeMirror-line")

CodeMirrorLines = website.find_all("pre", class_="CodeMirror-line")

for item in CodeMirrorLines[2].next.contents:
    print(item.string, end="")

print() # The purpose of this print is just to make the terminal output look cleaner
print("I'm done :)")