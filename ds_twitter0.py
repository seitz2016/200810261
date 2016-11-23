import oauth2
import os
def getKey(KeyPath):
    d=dict()
    f=open(KeyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0] =row[1].strip()
    return d

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')

key=getKey(keyPath)
key
import oauth2 as oauth
import json
consumer = oauth.Consumer(key=key['Consumer Key'], secret=key['Consumer Secret'])
token=oauth.Token(key=key['Access Token'], secret=key['Access Token Secret'])
client = oauth.Client(consumer, token)
import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 160924'})
response,content=client.request(url,method='POST',body=mybody)
import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)
import json
json.dumps(content)
import io
import json
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)
pwd