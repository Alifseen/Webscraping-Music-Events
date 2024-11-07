import streamlit as st
import scraper
import pandas as pd
import os
import plotly.express as px

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


URL = "https://programmer100.pythonanywhere.com/"
TEXT_FILE = "temp_data.txt"

all_content = scraper.scrape_data(URL)
temp_content = scraper.extract_data(all_content)
scraper.store_data(TEXT_FILE, scraper.time_now()+ ","+ temp_content)

df = pd.read_csv(TEXT_FILE)

figure = px.line(x=df["date"], y=df["temperature"])

st.plotly_chart(figure)