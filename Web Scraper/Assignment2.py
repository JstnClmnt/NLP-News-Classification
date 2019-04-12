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

count=7
position=18
url="http://py4e-data.dr-chuck.net/known_by_Sofia.html"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
print("Retrieved:"+url)
samplepos=1
while count>0:
    for tag in tags:
        if position==samplepos:
            url=tag.get('href', None)
            print("Retrieved:"+tag.get('href', None))
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            count=count-1
            samplepos=1
            break
        samplepos=samplepos+1
    

