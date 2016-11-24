type(tree)
from lxml.cssselect import CSSSelector
sel=CSSSelector('wikimedia')
results=sel(tree)
import lxml.html
for each in results:
myhtml="""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My Home Page</title>
</head>
<body>
<h1>안녕하십니까</h1>
<p>오늘은 프로그래밍 하는 날...</p>
<p>Today we do programming...</p>
</body>
</html>"""
_html=lxml.html.fromstring(myhtml)
sel=CSSSelector('body > p')
results=sel(_html)
for result in results:
import urllib
response=urllib.urlopen('https://www.python.org/')
_html=response.read()
import re
# http:// 뒤에 아무내용이 없든 여러개 있든 가져와라-meta character 정규식 
p=re.compile('href="(http://.*?)"')
res=p.findall(_html)
for item in res:
p=re.compile('<h1>(.*?)</h1>')
h1tags=p.findall(_html)
for i in h1tags:
p=re.compile('<p>(.*?)</p>')
p_tags=p.findall(_html)
for x in p_tags: