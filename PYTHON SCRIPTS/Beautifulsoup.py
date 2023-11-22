import urllib.request, urllib.parse, urllib.error
import Beautifulsoup
import ssl

#Ignore all SSL certificate Errors
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context = ctx).read()
soup = Beautifulsoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))