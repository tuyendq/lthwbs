import json

def validate_json(file_path):
    try:
        with open(file_path, "r") as file:
            json.load(file)  # Attempt to load JSON
        print("✅ JSON file is properly structured!")
    except json.JSONDecodeError as e:
        print(f"❌ JSON structure is invalid: {e}")

# json_file_path = "D:\projects\lthwbs\ytInitialData.json"
json_file_path = "./data/ytInitialData.json"
validate_json(json_file_path)
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

    contents = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"]["richGridRenderer"]["contents"]
    print(f"Number of contents: {len(contents)}")
    # for content in contents:
    #     print(content["richItemRenderer"]["content"]["videoRenderer"]["title"])
  
    count = 0
    for content in contents:
        if "richItemRenderer" in content:
            rich_item = content["richItemRenderer"]
            if "content" in rich_item and "videoRenderer" in rich_item["content"]:
                video_renderer = rich_item["content"]["videoRenderer"]
                if "title" in video_renderer and "videoId" in video_renderer and "text" in video_renderer["title"]["runs"][0]:
                    videoId = video_renderer["videoId"]
                    title = video_renderer["title"]["runs"][0]["text"]
                    count += 1
                    print(f"Video {count}: {title} - {videoId}")
                else:
                    print("Title not found")
            else:
                print("Video renderer not found")
        else:
            print("Rich item renderer not found")