import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['Consumer Key'], secret=key['Consumer Secret'])
token=oauth.Token(key=key['Access Token'], secret=key['Access Token Secret'])
client = oauth.Client(consumer, token)
import urllib
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)
len(tsearch_json['statuses'][0])
for i,tweet in enumerate(tsearch_json['statuses']):
    #print tweet[u'user'][u'name']
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])