import requests
import re

channel_id = None
channel_name = "betterversionvn"

url = "https://youtube.com/@" + channel_name
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
    html_content = ""

pattern = re.compile(r"browseId\":\"UC[^\"]+\"")
match = pattern.search(html_content)
if match:
    channel_id = match.group(0).split(":")[1].replace("\"", "").strip()
    print(f"Channel ID: {channel_id}")
else:
    print("Channel ID not found in the HTML content.")

