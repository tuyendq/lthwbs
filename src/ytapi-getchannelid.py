import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

channel_id = None
# channel_name = "@betterversionvn"  # Replace with the desired channel name
channel_handle = "@betterversionvn"  # Replace with the desired channel handle

api_key = os.getenv("YOUTUBE_API_KEY")  # Set your YouTube Data API key as an environment variable
if not api_key:
    raise ValueError("YouTube API key not found. Please set it as an environment variable.")

youtube = build('youtube', 'v3', developerKey=api_key)

try:
    response = youtube.channels().list(
        # forUsername=channel_name,
        forHandle=channel_handle,  # Replace with the actual handle
        part='id'
    ).execute()

    if 'items' in response and len(response['items']) > 0:
        channel_id = response['items'][0]['id']
        print(f"Channel ID: {channel_id}")
    else:
        print("Channel ID not found for the given channel name.")
except Exception as e:
    print(f"An error occurred: {e}")
