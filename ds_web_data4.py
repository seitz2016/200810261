# regex
import urllib
keyword='비오는'
f= urllib.urlopen('http://music.naver.com/search/search.nhn?query='+keyword+'&x=0&y=0')
mydata= f.read()
len(mydata)
pos=mydata.find('트랙 리스트')  #트랙리스트의 위치
pos1=mydata.find("_title title NPI=", pos)
pos2=mydata.find("title=",pos+20)
import os
os.getcwd()
f=open('mydata.txt','w')
f.write(mydata)
f.close()
import re
p=re.compile('title=".*비.?오는.*"') 
# '비'앞에 다른 문자가 올수 있음. '비'와 '오는 사이에 한글자가 올수도 있음(띄어쓰기)
res=p.findall(mydata)
len(res)
for item in res:
import lxml.html
html=lxml.html.fromstring(mydata)
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
results=sel(html)
sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
results = sel(html)
_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
_name=_selName(results[1])
_artist=_selArtist(results[1])
_album=_selAlbum(results[1])
for item in results:
    #print lxml.html.tostring(item)
    _name=_selName(item)
    _artist=_selArtist(item)
    _album=_selAlbum(item)
    if _name:
import json
import urllib
ipdata=urllib.urlopen('https://freegeoip.net/json/')
ipdata.read()
def getCountry(ipAddress):
    response = urllib.urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")
