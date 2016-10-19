import os
keyPath=os.path.join(os.getcwd(), 'src','key.properties' )
f=open(keyPath,'r')
lines=f.readlines()
d=dict()
d['a']=1
for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()
def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in lines:
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d
import os
keyPath=os.path.join(os.getcwd(), 'src','key.properties' )

key=getKey(keyPath)
key['dataseoul']

#대기오염정보
SERVICE='ArpltnInforInqireSvc'
OPERATION_NAME='getMinuDustFrcstDspth'
#param1=os.path.join(SERVICE,OPERATION_NAME)
param1=SERVICE+'/'+OPERATION_NAME
import urllib
d=dict()
d['dataTerm']='month'
param2=urllib.urlencode(d)
params=param1+'?'+'servicekey='+key['gokr']+'&'+param2
import urlparse
url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
myurl=urlparse.urljoin(url,params)