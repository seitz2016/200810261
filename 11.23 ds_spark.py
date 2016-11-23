import findspark
import os
spark_home="C:\Users\DB400T2A\Downloads\spark-1.6.0-bin-hadoop2.6"
print spark_home
findspark.init(spark_home)
import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc=pyspark.SparkContext(conf=conf)
sc
sc.version
sc.master
sc._conf.getAll()
c=list([39.2, 36.5,37.3,37.0])
def c2f (c):
    f=list()
    for x in c:
        _c=9./5*x+32;
        f.append(_c)
    return f
map(lambda c:(float(9)/5)*c + 32, c)
%%writefile data/ds_spark_wiki.txt
Wikipedia
Apache Spark is an open source cluster computing framework.
아파치 스파크는 오픈소스 클러스터 컴퓨팅 프레임워크 이다.
Originally developed at the University of California, Berkeley's AMPLab, 
the Spark codebase was later donated to the Apache Software Foundation, 
which has maintained it since. 
Spark provides an interface for programming entire clusters with 
implicit data parallelism and fault-tolerance.
textFile=sc.textFile("data/ds_spark_wiki.txt")
type(textFile)
textFile.take(3)
words=textFile.map(lambda x:x.split(' '))
words.collect()
textFile.map(lambda x:len(x)).collect()
_sparkLine=textFile.filter(lambda line:"Spark" in line)
_sparkLine.count()
_sparkLine=textFile.filter(lambda line:u"스파크"in line)
_sparkLine.count()
a=[1,2,3]
type(a)
myrdd=sc.parallelize(a)
myrdd.take(3)
squared=myrdd.map(lambda x:x*x)
squared.collect()
a=["this is a line","this is another line"]
myrdd=sc.parallelize(a)
words=myrdd.map(lambda x:x.split(' '))
words.collect()
myrdd\
    .map(lambda x:x.split(' '))\
    .collect()
myrdd.map(lambda x:x.replace("a","AA")).collect()