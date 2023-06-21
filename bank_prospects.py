from pyspark.sql import SparkSession

from pyspark.sql.functions import col,mean

spark=SparkSession.builder.appName("rohit").getOrCreate()

df1=spark.read.csv("/userretailstore.csv",header=True,inferSchema=True)

df2=df1.filter(col("Country")!="unknown")

age1=df2.select(mean("Age").cast("integer")).collect()

age2=age1[0][0]

df4=df2.na.fill(age2,["age"])

salary=df2.select(mean("Salary").cast("integer")).collect()

salary2=salary[0][0]

df5=df4.na.fill(salary2,["Salary"])

df5.write.format("csv").save("bank3.py")