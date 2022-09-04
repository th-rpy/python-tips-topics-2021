# For this tip, we will need to use the following library:
# - pandas 0.20+
#########################################################

# Tip #2: Filters & Multivalue using Pandas.

# Example :

# Import the necessary libraries
import pandas as pd  # For dataframes

# Read the data from the file
df = pd.read_csv("data/data.csv")
df.info()  # To see the dataframe info
print(df.columns)  # To see the dataframe columns names :

""" Output: Index(['ml_experience', 'major', 'class_attendance',
       'university_years', 'lab1', 'lab2', 'lab3', 'lab4', 'quiz1', 'quiz2'],
      dtype='object')"""


# Filter column
df_1 = df.filter(items=["lab2", "lab5"]).head()
print(df_1.columns)  # To see the dataframe columns names

"""Output: Index(['lab2'], dtype='object')"""

# Filter column using regex
df_2 = df.filter(regex="lab").head()
print(df_2.columns)  # To see the dataframe columns names
"""Output: Index(['lab1', 'lab2', 'lab3', 'lab4'], dtype='object')"""

# Filter column using like
df_3 = df.filter(like="en").head()
print(df_3.columns)  # To see the dataframe columns names
"""Output: Index(['ml_experience', 'class_attendance'], dtype='object')"""
