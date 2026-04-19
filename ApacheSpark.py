import pyspark
import pandas as pd
from tkinter import messagebox
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer
from pyspark.ml.feature import VectorAssembler
#from pyspark.sql.group import GroupedData

#from distutils.version import LooseVersion
# print('apache spark')
# messagebox.showinfo("Connpipection okec")

pd.read_csv('testdata.csv')

spark = SparkSession.builder.appName('DataFrame').getOrCreate()
print(spark)
############## below we are creating Data Frame from spark session ##############
df_pyspark = spark.read.csv('testdata.csv')
#print(df_pyspark.show())
#print(type(df_pyspark))
#df_pyspark=spark.read.option('header','true').csv('testdata.csv')
#df_pyspark=spark.read.option('header','true').csv('testdata.csv',inferSchema=True)

############ In below line we are reading data frame from a spark session ###############
df_pyspark=spark.read.csv('testdata.csv',header=True, inferSchema=True)

#df_pyspark.show()
#df_pyspark.printSchema()
listofrows=df_pyspark.head(5)
print(listofrows)

#df_pyspark.select(['Customer Name','Unit']).show()
#df_pyspark.dtypes()
#df_pyspark.describe().show()

############# Adding Columns in Data Frame. Below command will return a new class of DataFrame by adding a new column or replacing if same name column already exist
df_pyspark = df_pyspark.withColumn('Area_Avg', df_pyspark['Area'])
df_pyspark = df_pyspark.withColumnRenamed('Customer Name','Teacher Name')
#df_pyspark.show()

#df_pyspark.drop('columnname')
############ Drop Rows #############3
#df_pyspark.na.drop(how='all').show()
#df_pyspark.na.drop(how='any',thresh=4).show()
#df_pyspark.na.drop(how='any',subset=['Unit']).show()

#################### Fill Rows with specific values  #################################

df_pyspark=df_pyspark.na.fill('NA')
df_pyspark.na.fill(0,['Unit','Area','Rate','Balance','Area_Avg']).show()
df_pyspark.drop('Area_Avg')

#################### Imputer Functions to Fill NULL values with Avg, Mean,Median, Mod etc ####################3
imputer = Imputer(
    inputCols=['Area','Rate','Balance'],
    outputCols=["{}_imputed".format(c) for c in ['Area','Rate','Balance'] ]
).setStrategy("mean")

#df_pyspark = imputer.fit(df_pyspark).transform(df_pyspark).show()

################## Filters #########################
#df_pyspark.filter('Area>=200').select(['Teacher Name','Unit','Area','Rate']).show()
#df_pyspark.filter((df_pyspark['Area']>=200) & (df_pyspark['Rate']>=300)).select(['Teacher Name','Unit','Area','Rate']).show()
#df_pyspark.filter(~((df_pyspark['Area']>=200) & (df_pyspark['Rate']>=300))).select(['Teacher Name','Unit','Area','Rate']).show()

################## Group and Aggregates #############################

df_pyspark.groupby('Area').sum().show()
df_pyspark.groupby('Unit').max('Rate').show()

################ VectorAssembler ###############################

#featureassembler = VectorAssembler(inputCols=["Area","Rate"],outputCol=[""] )
#output = featureassembler.transform(training)

################ Linear Regression for Predictions or Predicted Values ###############################



############### Data Bricks Code ####################################
# CSV options
file_location='testdata.csv'
df = spark.read.csv(file_location, header=True,inferSchema=True)
#df.show()
from pyspark.ml.feature import StringIndexer
# handling categorical features
#indexer = StringIndexer()

from pyspark.ml.feature import StringIndexer

categorical_cols = ["category"]
# handling categorical features
indexer = StringIndexer(inputCols=["category"],outputCols=["category_indexed"])
#indexer = StringIndexer(inputCol=[cols for cols in categorical_cols],
#                              outputCol=[cols + "_index" for cols in categorical_cols])

#df_r = indexer.fit(df).transform(df).schema
df_r = indexer.fit(df).transform(df)
df_r.show()


from pyspark.ml.feature import VectorAssembler
featureAssembler = VectorAssembler(inputCols=['Area','category_indexed'], outputCol="Independent Features")
output= featureAssembler.transform(df_r)
#output.show()
output.select("Independent Features")


from pyspark.ml.regression import LinearRegression
finalized_data = output.select("Independent Features","Rate")
train_data,test_data=finalized_data.randomSplit([.75 , .25])
regressor = LinearRegression(featuresCol='Independent Features',labelCol='Rate')
regressor = regressor.fit(train_data)

regressor.coefficients
regressor.intercept
pred_results= regressor.evaluate(finalized_data)
pred_results.predictions.show()