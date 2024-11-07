import time
import sqlite3
import requests
import selectorlib
from EmailSender import send_email

URL = "https://programmer100.pythonanywhere.com/tours/"
TEXT_FILE = "files/data.txt"  ## A path that stores the data

## 9. Establsih a connection with SQL DB
connection = sqlite3.connect("files/data.db")

## 1. Define a function that stores the entire page source data in a variable from a URL
def scrape(url):
    response = requests.get(url)
    source_data = response.text
    return source_data


## 2. Extract data from the entire page source using YAML and CSS ID Selector
def specific_data(source):
    extractor = selectorlib.Extractor.from_yaml_file("files/extract.yaml")  ## Take the source and only store the data that matches the CSS Selector as dictionary
    value = extractor.extract(source)["data"]  ## Return the value of data store using the key.
    return value


## 10. Store the data in a Database file
def store_data(data):
    cleaned_data = data.split(",")  ## Split the extracted data from comma
    cleaned_data = [item.strip() for item in cleaned_data]  ## Remove white spaces
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", cleaned_data)  ## Add to the database using ? placeholders
    connection.commit()  ## Save database


## 11. fetch data from database if it exists there
def read_data(data):
    cleaned_data = data.split(",")
    cleaned_data = [item.strip() for item in cleaned_data]
    band, city, date = cleaned_data  ## Separate the extracted data to check against values in database columns
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band,city,date))  ## Using AND conditional to check values from extracted data using placeholder
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    ## 7. Add a while lopp to run continuously
    while True:
        all_content = scrape(URL)
        extracted_content = specific_data(all_content)

        ## 5. Add Conditionals to ensure that "no upcoming tours" and duplicate events are not stored in the text file
        if extracted_content != "No upcoming tours":
            ## 13. Check database if values exist.
            row = read_data(extracted_content)
            if not row:  ## If not, add to the database and send email
                store_data(extracted_content)

                ## 6. Send an email if new event is found in text file
                send_email("New Event Happening", extracted_content)

        ## 8. Add a 2 second delay
        time.sleep(2)