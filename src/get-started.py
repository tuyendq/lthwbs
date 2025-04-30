import requests
from bs4 import BeautifulSoup
import requests
import re
# print(requests.__version__)

import requests

url = "https://youtube.com/@summaryversion/videos"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
# print(soup.title.string)

# Find the <script> tag containing "ytInitialData"
script_tags = soup.find("script", string=re.compile("var ytInitialData"))

# Extract content
with open("ytInitialData.txt", "w", encoding="utf-8") as file:
    if script_tags:
        # Extract the text content of the <script> tag
        script_content = script_tags.string
        # Write to file
        file.write(script_content)
    else:
        print("No <script> tag found with 'ytInitialData'")


