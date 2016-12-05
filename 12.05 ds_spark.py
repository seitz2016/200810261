df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)
df.printSchema()
from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)
df1=model.transform(df)
df1.printSchema()
df1.show()
labelIndexer = StringIndexer(inputCol="age", outputCol="att1")
model=labelIndexer.fit(df1)
df2=model.transform(df1)
labelIndexer = StringIndexer(inputCol="f1", outputCol="att2")
model=labelIndexer.fit(df2)
df3=model.transform(df2)
labelIndexer = StringIndexer(inputCol="f2", outputCol="att3")
model=labelIndexer.fit(df3)
df4=model.transform(df3)
labelIndexer = StringIndexer(inputCol="f3", outputCol="att4")
model=labelIndexer.fit(df4)
df5=model.transform(df4)
df5.printSchema()
df5.show()
from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

va = VectorAssembler(inputCols=["att1","att2","att3","att4"],outputCol="features")
df6 = va.transform(df5)
df7=df6.withColumnRenamed('labels','label')
df7.printSchema()
trainDf=df7.select('label','features')
trainDf.printSchema()
trainDf.show()