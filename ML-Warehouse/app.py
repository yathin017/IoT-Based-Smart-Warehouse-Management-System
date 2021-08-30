import streamlit as st
from multiapp import MultiPage
from pages import IoTWarehouse_Home, IoTWarehouse_Price, IoTWarehouse_QuantitySold   # import your app modules here
import warnings
warnings.filterwarnings("ignore")

app = MultiPage()

# Add all your application here
app.add_page("Home", IoTWarehouse_Home.app)
app.add_page("Price", IoTWarehouse_Price.app)
app.add_page("Selling Quantity", IoTWarehouse_QuantitySold.app)


# The main app
app.run()