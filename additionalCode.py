#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Implement additional codes to help explore the Boston data set

@author: ucaiado

Created on Februery 20, 2015
"""
# import libraries
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns
import seaborn as sns
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

# configure charts
sns.set_palette("deep", desat=0.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
sns.set_style("darkgrid")


'''
Begin of Help Functions
'''

'''
End of Help Functions
'''

# implement function to reshape data


def inplitData(df_housing_features, df_housing_prices):
    """
    Return a data frame with all features mearged in a single column and
    calculate how this data it spread out related to their own average
    :param df_housing_features: Data Frame. All features of Boston data set
    :param df_housing_prices: Data Frame. House prices (target) of Boston
    dataset.
    """
    # initiate lists
    l_aux = []
    l_aux2 = []
    l_aux3 = []
    l_aux4 = []
    # merge each list in an unique column and keep the names to identify them
    for s_aux in df_housing_features.columns:
        # normalize the featues values to number of standard deviations
        f_mean = df_housing_features[s_aux].mean()
        df_error = (df_housing_features[s_aux]-f_mean)
        df_error /= df_housing_features[s_aux].std()
        f_correct = 2
        # f_correct = (df_error.max()-df_error.min())/5  # group the data
        df_error = (df_error*f_correct).round()/f_correct
        na_aux2 = np.round(df_error, decimals=1)

        # agregate data
        l_aux += list(df_housing_features[s_aux].values)
        l_aux4 += list(na_aux2)
        l_aux2 += [x[0] for x in df_housing_prices.values]
        l_aux3 += ([s_aux]*df_housing_features.shape[0])

    # create a dataframe with the data agregated
    df_aux = pd.DataFrame([l_aux, l_aux4, l_aux2, l_aux3],
                          index=['FEAT_VAL', 'FEAT_NORML', 'MEDV',
                                 'FEAT_NAME']).T
    return df_aux
