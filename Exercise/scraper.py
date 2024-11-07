import requests
from datetime import datetime
import selectorlib


def store_data(path, data):
    with open(path,"a") as file:
        file.write(data + "\n")


def read_data(path):
    with open(path, "r")as file:
        return file.read()


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
    print("done")
