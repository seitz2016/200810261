import urllib
url = "https://api.twitter.com/1.1/followers/list.json"

response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)
for i in tfollower_json['users']: