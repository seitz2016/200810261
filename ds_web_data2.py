from bs4 import BeautifulSoup
soup=BeautifulSoup(_html)
len(_html)
len(soup) 
strongtags=soup('strong')
for i in strongtags:
atags=soup.findAll('a')
for tag in atags:
#xpath
from lxml import etree
tree=etree.HTML(_html)
nodes=tree.xpath('//*[@href]') # (//)어디에서든지 (*)모든 태그  ([])속성
for node in nodes:
#cssselector
import lxml.html
from lxml.cssselect import CSSSelector
import requests
r=requests.get('http://python.org')
_html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
results=sel(_html)
for result in results: