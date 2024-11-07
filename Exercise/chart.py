import streamlit as st
import plotly.express as px
import sqlite3
import os

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

with sqlite3.connect("temp_data.db") as connection:
    cursor = connection.cursor()
    datedb = cursor.execute("SELECT date FROM date_temp").fetchall()
    tempdb = cursor.execute("SELECT temperature FROM date_temp").fetchall()

    datedb = [item[0] for item in datedb]
    tempdb = [item[0] for item in tempdb]

figure = px.line(x=datedb, y=tempdb)

st.plotly_chart(figure)