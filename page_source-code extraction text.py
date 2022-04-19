print("I'm running :)")

from bs4 import BeautifulSoup

with open("Selenium Testing/seleniumPageSourcePretty.txt", "r") as w:
    website = BeautifulSoup(w, "html.parser")

#CodeMirrorLines = website.select(".CodeMirror-line")

CodeMirrorLines = website.find_all("pre", class_="CodeMirror-line")

line_list = []

for line in CodeMirrorLines:
    for text in line.next_element.contents:
        print(text.string, end="")
        line_list.append(text.string)
    print()
    line_list.append("\n")

print(line_list)

file_name = website.find("h2").string
print(file_name)
file_name_stripped = file_name.strip()
print(file_name_stripped)

with open("Selenium Testing/" + file_name.strip() + ".v", "w") as t:
    for element in line_list:
        t.write(element)

print("\nI'm done :)")