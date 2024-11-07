import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"

## 1. Define a function that stores the entire page source data in a variable from a URL
def scrape(url):
    response = requests.get(url)
    source_data = response.text
    return source_data

if __name__ == "__main__":
    content = scrape(URL)
    print(content)