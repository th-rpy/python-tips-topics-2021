# For this tip, we will need to use the following library:
# - scikit-learn 0.20+
# - pandas 0.20+
#########################################################

# Tip #1 : We'll use ColumnTransformer to apply different preprocessing to different columns.

# Example :

# Import the necessary libraries
import pandas as pd  # For dataframes
from sklearn.compose import make_column_transformer  # For ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler  # For preprocessing


# Read the data from the file
df = pd.read_csv("data/data.csv")
df.info()  # To see the dataframe info
print(df.columns)  # To see the dataframe columns names :

""" Output: Index(['ml_experience', 'major', 'class_attendance',
       'university_years', 'lab1', 'lab2', 'lab3', 'lab4', 'quiz1', 'quiz2'],
      dtype='object')"""

X = df.drop(columns=["quiz2"])  # Drop the quiz2 column from the dataframe
y = df["quiz2"]  # We'll use the quiz2 column as the target

# Create a ColumnTransformer object
numeric_cols = ["university_years", "lab1", "lab3", "lab4", "quiz1"]  # apply scaling
categorical_cols = ["major"]  # apply one-hot encoding
passthrough_cols = ["ml_experience"]  # do not apply any transformation
drop_cols = [
    "lab2",
    "class_attendance",
]  # do not include these features in modeling

ct = make_column_transformer(
    (StandardScaler(), numeric_cols),  # scaling on numeric features
    (OneHotEncoder(), categorical_cols),  # OHE on categorical features
    ("passthrough", passthrough_cols),  # no transformations on the binary features
    ("drop", drop_cols),  # drop the drop features
)

# Transform the data using the ColumnTransformer object. 
X_transformed = ct.fit_transform(X)
type(X_transformed[:2])  # Check the type of the transformed data 

"""Output: <class 'numpy.ndarray'>"""