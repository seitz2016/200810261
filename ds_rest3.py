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
