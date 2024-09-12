# import the necessary modules

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


# Loading and Prepareing the data
iris = load_iris()
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)

df['Species'] = iris.target
df['Species'] = df['Species'].map({0:'Setosa', 1:"Versicolor", 2:'Virginica'})

# side bar for user input
st.sidebar.header('input the features')


def user_input_features():
    sepal_length = st.sidebar.slider('sepal length (cm))', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))

    sepal_width= st.sidebar.slider('sepal width (cm)', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))

    petel_length= st.sidebar.slider('petal length (cm)', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))

    sepal_width= st.sidebar.slider('petal width (cm)', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

    data = {
        'sepal Length(cm)' :sepal_length,
        'sepal width (cm)' :sepal_width,
        'petel length (cm)':petel_length,
        'petel width (cm)'  :sepal_width
    }

    features = pd.DataFrame(data,index=[0])
    return features

input_df = user_input_features()

# Main panel
st.write("# Iris Flower Predication")

# Combine the input Features with Entire Dataset

iris_raw = df.drop(columns=['Species'])
iris_raw = pd.concat([input_df, iris_raw], axis = 0)

# standerized a input features 
scaler = StandardScaler()
iris_raw_scaled= scaler.fit_transform(iris_raw)
input_scaled = iris_raw_scaled[:1]# Let only the input user

# Train the models

model =RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris_raw_scaled[1:], df['Species'])

# make a predication
prediction = model.predict(input_scaled)
prediction_proba = model.predict_proba(input_scaled)

st.subheader('predication')
# st.write(iris.target_names[prediction])

st.subheader("predication probability")
st.write(prediction_proba)
