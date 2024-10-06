#!/bin/python3


import pandas as pd


# library is a collection of functions & methods
# pandas is used for data manipulation & analysis & uses 2D tables / columns & rows called a 'dataframe'

# numPy uses arrays for its inputs & outputs

# SciPy has functions for some adv. math problems, & does data visualization

# Matplotlib is a well known for graphs & plots

# Seaborn makes heat maps, time series and violin plots

# Scikit-learn has tools for statistical models, ML,  regression, classification, clusters, etc...

# StatsModels allows users to explore data, estimate statistical models, perform statistical test

str1 = ("Data acquisition --process of reading data into python from various sources",
        "Uses 2 properties:",
        "Format --way data is encoded",
        "File path of dataset",
        )

# print(str1)

# steps to import pandas and use the csv reader

# step1 import pandas
# import pandas as pd

# step 2 define a variable w/ the file path of the data wanted

url_path = "https://archieve.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

# step 3 use the read_csv method to import the data
# read_csv assumes that the data will have a header, the data on used cars contains no column headers,
# will need to specify 'read_csv' to not assign headers by setting header to 'none'


df_dataframe = pd.read_csv(url_path, header=None)

print(df_dataframe.head(5))  # to show the first n rows of data frame
print(df_dataframe.tail(5))  # to show the bottom n rows of df

# replace the default header by using a variable found in seperate file or create your own

# example of own header..
headers = [
        "symboling", "normalized-losses", "make", "fuel-type", "aspiration",
]

# export your pandas df to a new csv file location
path_new = "C:\Windows\...\new_file2.csv"

# use the to_csv() method from pandas

df.to_csv(path_new, header=headers)

# exporting different formats in python

# Read                Save
pd.read_csv()           df.to_csv()
pd.read_json()          df.to_json()
pd.read_excel()         df.to_excel()
pd.read_sql()           df.to_sql()
pd.read_html()          df.to_html()
pd.read_xml()           df.to_xml()

