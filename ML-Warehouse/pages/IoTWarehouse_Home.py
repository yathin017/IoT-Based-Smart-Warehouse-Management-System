import pandas as pd
import numpy as np
import streamlit as st
import plotly
import plotly.express as plt

#from sklearn import linear_model
#from sklearn import preprocessing
#from sklearn.ensemble import GradientBoostingRegressor

def app():
    st.title("_Smart Fruit Warehouse Control System_")
    st.write("### Understanding Data:")
    df = pd.read_csv('Warehouse.csv')

    x_axis = st.selectbox(
        'Select X-axis:',
        ('Price','Quantity','Customers')
    )
    y_axis = st.selectbox(
        'Select Y-axis:',
        ('Customers','Quantity','Price')
    )

    

    if(x_axis=='Price' and y_axis=='Customers'):
        plot1 = plt.scatter(x=df['Price'],y=df['Customers'],title="Price vs Customers")
        plot2 = plt.scatter(x=df['Day'],y=df['Price'],title="Day vs Price")
        plot3 = plt.scatter(x=df['Day'],y=df['Customers'],title="Day vs Customers")

    if(x_axis=='Price' and y_axis=='Quantity'):
        plot1 = plt.scatter(x=df['Price'],y=df['Sold'],title="Price vs Quantity")
        plot2 = plt.scatter(x=df['Day'],y=df['Price'],title="Day vs Price")
        plot3 = plt.scatter(x=df['Day'],y=df['Sold'],title="Day vs Quantity")

    if(x_axis=='Price' and y_axis=='Price'):
        st.error("X-axis and Y-axis cannot be same")

    if(x_axis=='Quantity' and y_axis=='Customers'):
        plot1 = plt.scatter(x=df['Sold'],y=df['Customers'],title="Quantity vs Customers")
        plot2 = plt.scatter(x=df['Day'],y=df['Sold'],title="Day vs Quantity")
        plot3 = plt.scatter(x=df['Day'],y=df['Customers'],title="Day vs Customers")

    if(x_axis=='Quantity' and y_axis=='Price'):
        plot1 = plt.scatter(x=df['Sold'],y=df['Price'],title="Quantity vs Price")
        plot2 = plt.scatter(x=df['Day'],y=df['Sold'],title="Day vs Quantity")
        plot3 = plt.scatter(x=df['Day'],y=df['Price'],title="Day vs Price")

    if(x_axis=='Quantity' and y_axis=='Quantity'):
        st.error("X-axis and Y-axis cannot be same")

    if(x_axis=='Customers' and y_axis=='Quantity'):
        plot1 = plt.scatter(x=df['Customers'],y=df['Sold'],title="Customers vs Quantity")
        plot2 = plt.scatter(x=df['Day'],y=df['Customers'],title="Day vs Customers")
        plot3 = plt.scatter(x=df['Day'],y=df['Sold'],title="Day vs Quantity")

    if(x_axis=='Customers' and y_axis=='Price'):
        plot1 = plt.scatter(x=df['Customers'],y=df['Price'],title="Customers vs Price")
        plot2 = plt.scatter(x=df['Day'],y=df['Customers'],title="Day vs Customers")
        plot3 = plt.scatter(x=df['Day'],y=df['Price'],title="Day vs Price")

    if(x_axis=='Customers' and y_axis=='Customers'):
        st.error("X-axis and Y-axis cannot be same")
    
    if st.button("Plot"):
        st.plotly_chart(plot1)
        st.plotly_chart(plot2)
        st.plotly_chart(plot3)
