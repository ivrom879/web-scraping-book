from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')