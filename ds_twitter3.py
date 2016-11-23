import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul', 'count':200, 'since_id':'754295227351871489'}
mybody=urllib.urlencode(myparam)
response, content=client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
tsearch_json
len(tsearch_json['statuses'])
tsearch_json['statuses'][-1]['id']-1
f=open('ds_twitter_3.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()
None
prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    myparam={'q':'seoul','count':10,'max_id':prev_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()