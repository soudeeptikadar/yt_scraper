# utils.py

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def authenticate_youtube_api():
    api_key = os.getenv("YOUTUBE_API_KEY")  # Fetch the key from the environment variable
    if not api_key:
        raise ValueError("YOUTUBE_API_KEY environment variable is not set.")
    print(f"Using YouTube API Key: {api_key[:5]}...")  # Print part of the key for debugging
    return build("youtube", "v3", developerKey=api_key)

def authenticate_sheets_api():
    """Authenticate to the Google Sheets API using OAuth2.0 credentials."""
    creds_file = os.getenv('GOOGLE_SHEETS_CREDENTIALS_FILE')
    if not creds_file:
        raise ValueError("GOOGLE_SHEETS_CREDENTIALS_FILE environment variable is not set.")
    print(f"Using Google Sheets credentials file: {creds_file}")  # Print credentials file path for debugging
    credentials = service_account.Credentials.from_service_account_file(
        creds_file,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build('sheets', 'v4', credentials=credentials)

def clean_data_for_csv(data):
    """Clean the data before storing it in CSV format."""
    return {
        "title": data.get("title", ""),
        "views": data.get("views", 0),
        "likes": data.get("likes", 0),
        "comments": data.get("comments", 0),
        "date": data.get("date", "")
    }

print("Credentials file path:", os.getenv('GOOGLE_SHEETS_CREDENTIALS_FILE'))

