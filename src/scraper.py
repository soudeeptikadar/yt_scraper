import pandas as pd
from googleapiclient.errors import HttpError
from src.utils import authenticate_youtube_api, clean_data_for_csv
import datetime

def get_channel_data(channel_id):
    """Fetches channel's videos and metrics using the YouTube API."""
    youtube = authenticate_youtube_api()
    
    try:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            publishedAfter=(datetime.datetime.now() - datetime.timedelta(days=15)).isoformat() + "Z",
            maxResults=50
        )
        response = request.execute()

        video_data = []
        for item in response.get("items", []):
            if "id" in item and "videoId" in item["id"]:
                video_id = item["id"]["videoId"]
                video_info = get_video_metrics(youtube, video_id)
                cleaned_data = clean_data_for_csv(video_info)
                video_data.append(cleaned_data)
            else:
                print(f"Skipping item with no videoId: {item}")
        
        print(f"Scraped data for {channel_id}: {video_data}")  # Added debug print
        return video_data
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []
    
def get_video_metrics(youtube, video_id):
    """Fetch video metrics (views, likes, comments) using the YouTube API."""
    request = youtube.videos().list(part="snippet,statistics", id=video_id)
    response = request.execute()

    print(f"Video ID: {video_id}")
    print(f"API Response: {response}")

    if not response.get("items"):
        return {
            "title": "N/A",
            "date": "N/A",
            "views": "0",
            "likes": "0",
            "comments": "0",
        }
    
    video_info = response["items"][0]
    snippet = video_info.get("snippet", {})
    statistics = video_info.get("statistics", {})

    return {
        "title": snippet.get("title", "N/A"),
        "date": snippet.get("publishedAt", "N/A"),
        "views": statistics.get("viewCount", "0"),
        "likes": statistics.get("likeCount", "0"),
        "comments": statistics.get("commentCount", "0"),
    }


def save_data_to_csv(data, filename="data/youtube_data.csv"):
    """Save scraped data to CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
