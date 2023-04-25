# python -m pip install requests
# python -m pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = "https://regatta.appcreation.de/frgle/vpfzvejd/races"
page = requests.get(URL)
print(page.text + "\n")

print("\n******************************************\n")

soup = BeautifulSoup(page.content, "html5lib")
print(soup.prettify() + "\n")