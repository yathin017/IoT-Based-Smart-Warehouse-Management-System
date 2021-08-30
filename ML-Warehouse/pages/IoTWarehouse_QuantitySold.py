# importing modules
import pandas as pd
import numpy as np
import streamlit as st
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from pathlib import Path


def app():
    st.title("_Smart Fruit Warehouse Control System_")
    html_temp = """
    <div style="background-color:#E9AF6F;padding:10px;border-bottom-left-radius:50%;border-bottom-right-radius:50%;">
    <h1 style="color:black;text-align:center;">Selling Quantity Prediction</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write("##")
    st.write("### Unique codes:")
    st.write("#### Sunday -> 3, Monday -> 1, Tuesday -> 5, ")
    st.write("#### Wednesday -> 6, Thursday -> 4, Friday -> 0, Saturday -> 2 ")
    st.write("##")
    a = st.number_input("Enter the unique code to select a day:", min_value=1, max_value=70, value=1, step=1)
    b = st.number_input("Enter price of the fruit:", min_value=1, max_value=70, value=1, step=1)
    c = st.number_input("Enter number of customers:", min_value=1, max_value=70, value=1, step=1)
    result=""
    if st.button("Predict"):
        result=main(a,b,c)
        st.warning('Predicted selling quantity for the day is {}kgs'.format(result))
        df = pd.read_csv('Warehouse.csv')
        avg_sold     = int(df['Sold'].iloc[0:364].mean())
        avg_sold_sun = int(df['Sold'].iloc[312:364].mean())
        avg_sold_mon = int(df['Sold'].iloc[0:52].mean())
        avg_sold_tue = int(df['Sold'].iloc[52:104].mean())
        avg_sold_wed = int(df['Sold'].iloc[104:156].mean())
        avg_sold_thu = int(df['Sold'].iloc[156:208].mean())
        avg_sold_fri = int(df['Sold'].iloc[208:260].mean())
        avg_sold_sat = int(df['Sold'].iloc[260:312].mean())
        # Overall average
        st.info("Yearly average = {}kgs ".format(avg_sold))
        sold = result
        if(sold>avg_sold):
            st.success("Profit: The quantity sold is greater than the yearly average")
        else:
            st.error("Loss: The quantity sold is lesser than the yearly average")

        # perday average
        d = a
        if(d==3):
            st.info("Sundays Average = {}kgs".format(avg_sold_sun))
            if(sold>avg_sold_sun):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Sundays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Sundays")
        if(d==1):
            st.info("Mondays Average = {}kgs".format(avg_sold_mon))
            if(sold>avg_sold_mon):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Mondays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Mondays")
        if(d==5):
            st.info("Tuesdays Average = {}kgs".format(avg_sold_tue))
            if(sold>avg_sold_tue):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Tuesdays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Tuesdays")
        if(d==6):
            st.info("Wednesdays Average = {}kgs".format(avg_sold_wed))
            if(sold>avg_sold_wed):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Wednesdays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Wednesdays")
        if(d==4):
            st.info("Thursdays Average = {}kgs".format(avg_sold_thu))
            if(sold>avg_sold_thu):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Thursdays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Thursdays")
        if(d==0):
            st.info("Fridays Average = {}kgs".format(avg_sold_fri))
            if(sold>avg_sold_fri):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Fridays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Fridays")
        if(d==2):
            st.info("Saturdays Average = {}kgs".format(avg_sold_sat))
            if(sold>avg_sold_sat):
                st.success("Profit: Quantity sold is greater than the average quantity sold on Saturdays")

            else:
                st.error("Loss: Quantity sold is lesser than the average quantity sold on Saturdays")
    

def main(a,b,c):
    df = pd.read_csv('Warehouse.csv')
    label_encoder = preprocessing.LabelEncoder()
    df['Day']= label_encoder.fit_transform(df['Day'])
    
    x = df.drop('Sold',axis='columns')
    y = df.Sold
    reg = GradientBoostingRegressor(random_state=0)
    reg.fit(x, y)

    result = int(reg.predict([[a,b,c]]))
    return result


