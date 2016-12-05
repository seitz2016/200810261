%%writefile ./data/ds_spark_2cols.csv
35, 2
40, 27
12, 38
15, 31
21, 1
14, 19
46, 1
10, 34
28, 3
48, 1
16, 2
30, 3
32, 2
48, 1
31, 2
22, 1
12, 3
39, 29
19, 37
25, 2
f=sc.textFile("data/ds_spark_2cols.csv")
csvRdd=f.map(lambda x:x.split(','))
csvRdd.collect()
from pyspark.mllib.linalg import Vectors
dv1=Vectors.dense([1,2,3])
import numpy as np
dv2=np.array([1,2,3])
Vectors.dense(dv2)
sv1=Vectors.sparse(3,[1,2],[1.0,3.0])
sv1.toArray()
from pyspark.mllib.regression import LabeledPoint
LabeledPoint(1.0, Vectors.dense([1.0,2.0,3.0]))
from pyspark.sql import SQLContext
sqlCtx=SQLContext(sc)
trainDf=sqlCtx.createDataFrame([
        (1.0, Vectors.dense([0.0,1.1,0.1])),
        (1.0, Vectors.dense([0.0,1.1,0.1])),
        (1.0, Vectors.dense([0.0,1.1,0.1])),
    ],["label", "features"])
trainDf.show()
trainDf.printSchema()
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector, VectorUDT
from pyspark.sql.types import StructType, StructField, DoubleType
_rdd = sc.parallelize([
    (0.0, SparseVector(4, {1: 1.0, 3: 5.5})),
    (1.0, SparseVector(4, {0: -1.0, 2: 0.5}))])
schema = StructType([
    StructField("label", DoubleType(), True),
    StructField("features", VectorUDT(), True)
])
trainDf=_rdd.toDF(schema)
trainDf.printSchema()
sqlCtx
svmfn="C:\Users\DB400T2A\Downloads\spark-1.6.0-bin-hadoop2.6\data\mllib\sample_libsvm_data.txt"
svmDf = sqlCtx.read.format("libsvm").load(svmfn)
type(svmDf)
svmDf.printSchema()
svmDf.take(1)
%%writefile data/ds_spark_wiki.txt
Wikipedia
Apache Spark is an open source cluster computing framework.
아파치 스파크는 오픈소스 클러스터 컴퓨팅 프레임워크 이다.
Originally developed at the University of California, Berkeley's AMPLab, 
the Spark codebase was later donated to the Apache Software Foundation, 
which has maintained it since. 
Spark provides an interface for programming entire clusters with 
implicit data parallelism and fault-tolerance.
lines =  sc.textFile("data/ds_spark_wiki.txt")
wc=lines.flatMap(lambda x:x.split())
wc.collect()
from operator import add
wc = sc.textFile("data/ds_spark_wiki.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])
wc.collect()
for e in wc.collect():
    print e
pDf=sqlCtx.read.json("C:/Users/DB400T2A/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")
type(pDf)
pDf.show()
pDf.filter(pDf['age'] > 21).show()
pDf.registerTempTable("people")
sqlCtx.sql("select name from people").show()
import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")
wc=r.json()
type(wc)
help(sqlCtx.createDataFrame)
wcDf=sqlCtx.createDataFrame(wc)
wcDf.printSchema()
wcDf.registerTempTable('wc')
sqlCtx.sql("select Club,Team,Year from wc").show(1)