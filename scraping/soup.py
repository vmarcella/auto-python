import requests
from bs4 import BeautifulSoup

URL = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(URL)

page = BeautifulSoup(response.text, "html.parser")

# print out the title tag and then all of it's contents
print(page.title)
print(page.title.string)

# Find all h3 elements
print(page.find_all("h3"))

# Find a link that has the name attribute, links
link_section = page.find("a", attrs={"name": "links"})
section = []
print(link_section)

# Iterate over the next couple of elements and append their string
# contents into our section if the element isn't an h3 tag (the next section)
for element in link_section.next_elements:
    if element.name == "h3":
        break
    section.append(element.string or "")

result = "".join(section)
print("--Printing the result of the link section--")
print(result)
