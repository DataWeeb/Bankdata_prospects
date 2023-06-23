# About

I have used gcp dataproc to work on this small project with hive,hdfs and pyspark
it can be done on local windows and linux as well

In this we have two things to do on data

1. remove the rows which have unknown value
2. put mean of data inplace of null values

# steps in project

first load data into gcp home

then create directory in hdfs

put data from local to hdfs

do spark processing on it and load back to hdfs

Note - writing spark code in local is comfortable and then put that .py file to gcp

create hive table on top of that data

