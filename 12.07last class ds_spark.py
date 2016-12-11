from pyspark.mllib.regression import LabeledPoint
trainRdd = trainDf.map(lambda row: LabeledPoint(row.label,row.features))
trainRdd.first()
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(maxIter=10, regParam=0.01)
model1 = lr.fit(trainDf)
print model1.coefficients
print model1.intercept
from pyspark.sql import Row
test0 = sc.parallelize([Row(features=Vectors.dense(2,0,0,1))]).toDF()
result = model1.transform(test0).head()
result.prediction
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, RegexTokenizer
from pyspark.sql import SQLContext

sqlCtx = SQLContext(sc)
df = sqlCtx.createDataFrame(
    [
        [0,'my dog has flea problems. help please.'],
        [1,'maybe not take him to dog park stupid'],
        [0,'my dalmation is so cute. I love him'],
        [1,'stop posting stupid worthless garbage'],
        [0,'mr licks ate my steak how to stop him'],
        [1,'quit buying worthless dog food stupid'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이']
    ],
    ['cls','sent']
)
df.printSchema()
tokenizer = Tokenizer(inputCol="sent", outputCol="words")
tokDf = tokenizer.transform(df)
tokDf.printSchema()
for r in tokDf.select("cls", "sent").take(3):
    print(r)
tokDf.show()
re = RegexTokenizer(inputCol="sent", outputCol="wordsReg", pattern="\\s+")
regDf=re.transform(df)
regDf.show()
from pyspark.ml.feature import StopWordsRemover
stop = StopWordsRemover(inputCol="words", outputCol="nostops")
stopwords=list()

_stopwords=stop.getStopWords()
for e in _stopwords:
    stopwords.append(e)
_mystopwords=[u"나",u"너", u"우리"]
for e in _mystopwords:
    stopwords.append(e)
stop.setStopWords(stopwords)
for e in stop.getStopWords():
    print e,
stopDf=stop.transform(tokDf)
stopDf.show()
from pyspark.ml.feature import CountVectorizer
cv = CountVectorizer(inputCol="nostops", outputCol="cv", vocabSize=30,minDF=1.0)
cvModel = cv.fit(stopDf)
cvDf = cvModel.transform(stopDf)

cvDf.collect()
cvDf.select('words','nostops','cv').show()
cvDf.select('cv').take(13)
for v in cvModel.vocabulary:
    print v,
from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(cvDf)
trainDf2=model.transform(cvDf)
trainDf2.printSchema()
from pyspark.sql.functions import udf

toDoublefunc = udf(lambda x: x.DoubleType())
trainDf3 = trainDf2.withColumn("_label",toDoublefunc(trainDf2.cls))
trainDf3.printSchema()
%%writefile src/ds_spark_hello.py
print "---------BEGIN-----------"
import pyspark
conf = pyspark.SparkConf().setAppName("myAppName1")
sc   = pyspark.SparkContext(conf=conf)
sc.setLogLevel("ERROR")
print "---------RESULT-----------"
print sc
rdd = sc.parallelize(range(1000), 10)
print "mean=",rdd.mean()
nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
for num in squared:
    print "%i " % (num)