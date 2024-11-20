# Webscraping and SQLite

I scraped music event data from a website using selectorlib and YAML, it checks the website every 2 minutes for change in element that contains details of the concert.

It then cleans the data and matches those details with data in sql database, if the event already exists, it ignores it. If it does not exist in the database, it adds it and sends me an email notifaction for the new event. 