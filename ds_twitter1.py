from pymongo import MongoClient
_mclient=MongoClient()
_mclient['ds_twutter']
_db=_mclient.ds_twitter
_col=_db.home_timeline
url="https://api.twitter.com/1.1/statuses/home_timeline.json"
response,content=client.request(url)
home_timeline=json.loads(content)
len(home_timeline)
home_timeline
for tweet in home_timeline:
    print tweet['id'],tweet['text']
    