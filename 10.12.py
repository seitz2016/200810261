import os
KEY="77796776467365693131364c4c494552"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'
url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM
import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
import requests
data=requests.get(url)