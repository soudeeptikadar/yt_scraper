# run_scraper.py

import os
from src.scraper import get_channel_data, save_data_to_csv
from src.google_sheets import append_to_google_sheets
from src.fetch_channels import get_channel_list
from config import SHEET_ID as GOOGLE_SHEET_ID, SHEET_NAME

def run_scraper():
    # Fetch the list of channels
    channels = get_channel_list()

    for channel in channels:
        channel_id = channel['channel_id']
        channel_name = channel['channel_name']

        print(f"Scraping data for {channel_name} (ID: {channel_id})...")
        video_data = get_channel_data(channel_id)

        if video_data:
            # Add channel name to each video data entry for clarity
            for video in video_data:
                video['channel_name'] = channel_name

            # Save data to CSV
            save_data_to_csv(video_data)
            
            # Append data to Google Sheets
            try:
                append_to_google_sheets(
                    data=video_data,
                    sheet_id=GOOGLE_SHEET_ID,
                    sheet_name=channel_name  # Pass channel name as sheet name
                )
                print(f"Data for {channel_name} appended to Google Sheets successfully.")
            except Exception as e:
                print(f"Failed to append data for {channel_name} to Google Sheets: {e}")

if __name__ == "__main__":
    run_scraper()


'''
import os
from src.scraper import get_channel_data, save_data_to_csv
from src.google_sheets import append_to_google_sheets
from src.fetch_channels import get_channel_list
from config import SHEET_ID as GOOGLE_SHEET_ID

def run_scraper():
    # Fetch the list of channels
    channels = get_channel_list()

    for channel in channels:
        channel_id = channel['channel_id']
        channel_name = channel['channel_name']
        
        print(f"Scraping data for {channel_name} (ID: {channel_id})...")
        video_data = get_channel_data(channel_id)
        
        if video_data:
            # Add channel name to each video data entry for clarity
            for video in video_data:
                video['channel_name'] = channel_name
            
            # Save data to CSV
            save_data_to_csv(video_data)
            
            # Append data to Google Sheets
            append_to_google_sheets(video_data, GOOGLE_SHEET_ID)

if __name__ == "__main__":
    run_scraper()
'''