#!/usr/bin/python3
import requests
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
myfile = requests.get(url)
open('./tmp_data.txt','wb').write(myfile.content)
