import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin

 
# Class to calculate the age of a house, using the year sold and the year of the last renovation
class TimeSinceRenovation(BaseEstimator, TransformerMixin):
    def __init__(self, yr_sold, yr_ren):
        self.yr_sold = yr_sold
        self.yr_ren = yr_ren

    # this method is needed for the sklearn pipeline    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X["YearsSinceRenovation"] = X[self.yr_sold] - X[self.yr_ren]
        return X
    
#Class to drop columns after transformation
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables = variables

    # this method is needed for the sklearn pipeline    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        for column in self.variables:
            X.drop(column, axis=1, inplace=True)
        return X