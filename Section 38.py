import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"

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

if __name__ == "__main__":
    all_content = scrape(URL)
    extracted_content = specific_data(all_content)
    print(extracted_content)