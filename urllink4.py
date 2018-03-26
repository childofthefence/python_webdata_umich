# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url_test = 'http://py4e-data.dr-chuck.net/known_by_Malikye.html'
html = urllib.request.urlopen(url_test, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter count: "))
position = int(input("Enter position: "))
# Retrieve all of the anchor tags


for value in range(count):
    
    url = soup.find_all('a')[position-1]['href']
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(url)