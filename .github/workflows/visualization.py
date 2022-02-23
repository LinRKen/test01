#!/usr/bin/python3
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white")
fpath = './tmp_data.txt'
iris = pd.read_csv(fpath,names = ['sepal length','sepal width','petal length','petal width','class'])
iris.plot(kind = "scatter", x = "sepal length", y = "sepal width")

plt.show()
plt.savefig("matplotlib.png")

