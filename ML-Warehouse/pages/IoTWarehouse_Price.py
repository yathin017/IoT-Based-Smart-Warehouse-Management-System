import pandas as pd
import numpy as np
import streamlit as st
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor

def app():
    st.title("_Smart Fruit Warehouse Control System_")
    html_temp = """
    <div style="background-color:#E9AF6F;padding:10px;border-bottom-left-radius:50%;border-bottom-right-radius:50%;">
    <h1 style="color:black;text-align:center;">Fruit Price Prediction</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write("##")
    st.write("### Unique codes:")
    st.write("#### Sunday -> 3, Monday -> 1, Tuesday -> 5, ")
    st.write("#### Wednesday -> 6, Thursday -> 4, Friday -> 0, Saturday -> 2 ")
    st.write("##")
    i = st.number_input("Enter the unique code to select a day: ", min_value=1, max_value=70, value=1, step=1)
    j = st.number_input("Enter quantity sold:", min_value=1, max_value=70, value=1, step=1)
    k = st.number_input("Enter number of customers:", min_value=1, max_value=70, value=1, step=1)
    result=""
    if st.button("Predict"):
        result=main(i,j,k)
        st.warning('Predicted price for the day is  ₹{}'.format(result))

def main(i,j,k):
    df = pd.read_csv('Warehouse.csv')
    label_encoder = preprocessing.LabelEncoder()
    df['Day']= label_encoder.fit_transform(df['Day'])

    w = df.drop('Price',axis='columns')
    z = df.Price
    reg = GradientBoostingRegressor(random_state=0)
    reg.fit(w, z)

    result = int(reg.predict([[i,j,k]]))
    return result