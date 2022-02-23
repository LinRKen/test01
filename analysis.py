#!/usr/bin/python3
import numpy as np
import pandas as pd

fpath = './tmp_data.txt'
df = pd.read_csv(fpath,names = ['sepal length','sepal width','petal length','petal width','class'])
print(df.describe())
