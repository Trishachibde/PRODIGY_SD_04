import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# get website data
response = requests.get(url)

# parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# get title
title = soup.find("h1").text

# get first paragraph
paragraph = soup.find("p").text

# store data in list
data = [[title, paragraph]]

# convert to DataFrame
df = pd.DataFrame(data, columns=["Title", "Intro Paragraph"])

# save to CSV
df.to_csv("wikipedia_data.csv", index=False)

print("Data saved successfully!")
