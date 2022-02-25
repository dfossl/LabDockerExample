
from sklearn import linear_model
from sklearn import datasets
import pickle as pl
import numpy as np

# """
# makes a container for generic entry
# docker create --name python_interactive -v C:\Users\dfoss\Documents\Projects\LabDockerExample\example_genericpython\code:/code -it generic_python

# makes a generic training container
# docker create --name train_model -v C:\Users\dfoss\Documents\Projects\LabDockerExample\example_genericpython\code:/code generic_python python train.py
# """

print("Hello world")

diabetes = datasets.load_diabetes()

# Pick just one feature 
X = diabetes.data[:, np.newaxis, 2]

# creating and saving some model
regr = linear_model.LinearRegression()
regr.fit(X, diabetes.target)
pl.dump(regr, open('modle2.pl', 'wb'))

