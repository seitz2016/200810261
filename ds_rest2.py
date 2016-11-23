import os
keyPath=os.path.join(os.getcwd(), 'src','key.properties' )
print keyPath
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