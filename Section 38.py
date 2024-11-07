import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
TEXT_FILE = "files/data.txt"  ## A path that stores the data


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


## 3. Store the data in a text file
def store_data(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")


## 4. Read data from a a text file
def read_data(path):
    with open(path, "r") as file:
        return file.read()


if __name__ == "__main__":
    all_content = scrape(URL)
    extracted_content = specific_data(all_content)
    store_data(TEXT_FILE, extracted_content)
    print(read_data(TEXT_FILE))