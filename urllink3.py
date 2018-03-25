# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = 'http://py4e-data.dr-chuck.net/comments_42.html'
url2 = 'http://py4e-data.dr-chuck.net/comments_81416.html'
html = urlopen(url2, context=ctx).read()
# print(html)
# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

total = 0

# Retrieve all of the anchor tags
for tags in soup.findAll('span'):
    val = int(tags.contents[0].encode('UTF-8'))
    total = total + val

print(total)

