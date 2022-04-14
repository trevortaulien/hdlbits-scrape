print("I'm running :)")

from bs4 import BeautifulSoup

with open("seleniumPageSourcePretty.txt", "r") as w:
    website = BeautifulSoup(w, "html.parser")

#CodeMirrorLines = website.select(".CodeMirror-line")

CodeMirrorLines = website.find_all("pre", class_="CodeMirror-line")

for line in CodeMirrorLines:
    for text in line.next_element.contents:
        print(text.string, end="")
    print()

print("\nI'm done :)")