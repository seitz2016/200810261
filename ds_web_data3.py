import urllib2
url ='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
res=urllib2.urlopen(url)
html=res.read()
res.close()
type(html)
lines=html.splitlines()
for line in lines[0:10]:
line1=lines[0].split()
line1
data=list() #자료구조
for line in lines:
    lineData=line.split()
    #print lineData
    data.append(lineData)
data[0][0]
for i in data:
sum =0 
for i in data:
    sum += int(i[1])