#Exercise one: counting number of rows
#-------------------------------------

# Remarks: The method used is the simplest possible method, direct counting while loading line by line

# Improvement ideas: Alternatively, it is possible to use buf = f.read(buffer_size) and buf.count('\n'). Since the simplest 
# implementation works good enough for the moment, I will not optimize this function now. Furthermore, it is possible to parallelize
# the count by using Spark (see below). Counting in Spark is straightforward.

def countlines (fname):
  """This counts the number of lines in a file the simplest way. 
  Caveat: The buffer (one line at a time) is probably too small to be efficient. """

  f = open(fname)

  n = 0
  for i in f: n += 1

  f.close()
  
  return n


#countlines("/home/jacques/flights/bookings.csv")
#10000011
#countlines("/home/jacques/flights/searches.csv")
#20390199


# Another way:
# ------------

#Using pySpark, there is a direct method .count() 

#Python 2.6.6 (r266:84292, Dec 20 2012, 15:53:42) 
#[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
#Type "help", "copyright", "credits" or "license" for more information.
#/home/jacques/spark/conf/spark-env.sh: line 23: HADOOP_CONF_DIR: command not found
#/home/jacques/spark/conf/spark-env.sh: line 23: HADOOP_CONF_DIR: command not found
#Welcome to
      #____              __
     #/ __/__  ___ _____/ /__
    #_\ \/ _ \/ _ `/ __/  '_/
   #/__ / .__/\_,_/_/ /_/\_\   version 0.9.0
      #/_/

#Using Python version 2.6.6 (r266:84292, Dec 20 2012 15:53:42)
#Spark context available as sc.
#>>> sc
#<pyspark.context.SparkContext object at 0x7fcae447b410>
#>>> tx = sc.textFile("/home/jacques/flights/bookings.csv")
#>>> tx.count()
#10000011
#>>> tx = sc.textFile("/home/jacques/flights/searches.csv")
#>>> tx.count()
#20390199
#>>> 

# Note: Warnings result of Hadoop not being started, since it is not necessary for this test.
