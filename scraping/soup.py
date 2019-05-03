import requests
from bs4 import BeautifulSoup

URL = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(URL)

page = BeautifulSoup(response.text, "html.parser")

print(page.title)
