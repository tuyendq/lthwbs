import requests
from bs4 import BeautifulSoup
import requests
import re
# print(requests.__version__)

# url = "https://youtube.com/@summaryversion/videos"
url = "https://youtube.com/@betterversion/videos"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
title = soup.title.string.lower().strip().replace(" - youtube", "")
title = re.sub(r"[^a-z0-9\s-]", "", title) 
title = re.sub(r"\s+", "_", title)   
print(f"Title: {title}")

# Find the <script> tag containing "ytInitialData"
pattern = re.compile(r"var ytInitialData = ")
script_tags = soup.find("script", string=pattern)
# script_tags = soup.find("script", string=re.compile("var ytInitialData = "))

# Extract content
file_path = "./data/" + title + ".json"
with open(file_path, "w", encoding="utf-8") as file:
    if script_tags:
        # Extract the text content of the <script> tag
        script_content = script_tags.string
        # Write to file
        file.write(script_content)
    else:
        print("No <script> tag found with 'ytInitialData'")


