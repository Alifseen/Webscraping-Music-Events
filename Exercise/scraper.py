import requests
from datetime import datetime
import selectorlib
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

TEXT_FILE = "temp_data.txt"

with sqlite3.connect("temp_data.db") as connection:
    cursor = connection.cursor()

def store_data(data):
    cursor.execute("INSERT INTO date_temp VALUES(?,?)", (time_now(),data))
    connection.commit()


def scrape_data(url):
    response = requests.get(url)
    content = response.text
    return content

def extract_data(content):
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(content)["temp_data"]
    return value


def time_now():
    time_now = datetime.now()
    time_now = time_now.strftime("%d-%m-%y  %H:%M:%S")
    return time_now


if __name__ == "__main__":
    print(cursor.execute("SELECT * FROM date_temp").fetchall())
    source = scrape_data(URL)
    data = extract_data(source)
    store_data(data)
    print(cursor.execute("SELECT * FROM date_temp").fetchall())

