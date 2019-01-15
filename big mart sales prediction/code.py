import pandas as pd
import numpy as np 

#read files
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
train['source']='train'
test['spurce']='test'
#ignore_index set to true gives total rows continuous indexing in merged dataset
data=pd.concat([train,test],ignore_index=True)
#Dimension of dataset
print data.shape,train.shape,test.shape

#print 20 rows of
print data.head(20)

#finding the missing entries in dataset
print data.apply(lambda x: sum(x.isnull()))

#description/statistics of dataset
print data.describe()
