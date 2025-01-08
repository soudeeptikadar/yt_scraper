# google_sheets.py

import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


def authenticate_gspread():
    """Authenticate using gspread and service account credentials."""
    try:
        credentials_file = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE")
        gc = gspread.service_account(filename=credentials_file)
        return gc
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise

def next_letter(letter, steps):
    """Calculate the next column letter dynamically."""
    ascii_value = ord(letter)
    new_ascii_value = ascii_value + (steps - 1)
    
    if letter.islower():
        if new_ascii_value > ord('z'):
            new_ascii_value -= 26
    else:
        if new_ascii_value > ord('Z'):
            new_ascii_value -= 26     
    return chr(new_ascii_value)

def append_to_google_sheets(data, sheet_id, sheet_name):
    """
    Append data to the Google Sheets document.
    Clears the sheet, removes duplicates, and reinserts updated data.
    """
    try:
        # Authenticate and access the sheet
        gc = authenticate_gspread()
        sheet = gc.open_by_key(sheet_id).worksheet(sheet_name)

        # Preprocess data
        values = [list(item.values()) for item in data]

        # Handle nested lists and formatting
        for i, row in enumerate(values):
            for j, val in enumerate(row):
                if isinstance(val, list):
                    values[i][j] = ', '.join(val)  # Flatten lists
                elif isinstance(val, pd.Timestamp):
                    values[i][j] = val.strftime('%Y-%m-%d %H:%M:%S')  # Format timestamps

        # Get existing data and deduplicate
        existing_data = sheet.get_all_values()
        if existing_data:
            existing_df = pd.DataFrame(existing_data[1:], columns=existing_data[0])  # Skip header
            new_df = pd.DataFrame(values, columns=existing_data[0])  # Match existing headers
            combined_df = pd.concat([existing_df, new_df]).drop_duplicates().reset_index(drop=True)
        else:
            # If the sheet is empty
            combined_df = pd.DataFrame(values, columns=[f"Col{i+1}" for i in range(len(values[0]))])

        # Clear sheet and update with deduplicated data
        sheet.clear()
        sheet.update([combined_df.columns.tolist()] + combined_df.values.tolist())
        
        print(f"Data successfully updated in sheet: {sheet_name}")

    except Exception as e:
        print(f"Error appending to Google Sheets: {e}")
        raise

def insert_empty_row(spreadsheet_id, sheet_name, start_index, end_index):
    """Insert empty rows in the Google Sheets document."""
    try:
        gc = authenticate_gspread()
        sheet = gc.open_by_key(spreadsheet_id).worksheet(sheet_name)
        
        # Insert empty rows
        body = {
            'requests': [
                {
                    "insertDimension": {
                        "range": {
                            "sheetId": sheet.id,
                            "dimension": "ROWS",
                            "startIndex": start_index,
                            "endIndex": end_index
                        },
                        "inheritFromBefore": True
                    }
                },
            ]
        }

        gc.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        print(f"Empty rows inserted from {start_index} to {end_index} in {sheet_name}.")
    except Exception as e:
        print(f"Error inserting empty rows: {e}")
        raise



'''
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import os

def authenticate_sheets_api():
    """Authenticate to the Google Sheets API using service account credentials."""
    credentials = service_account.Credentials.from_service_account_file(
        os.getenv('GOOGLE_SHEETS_CREDENTIALS_FILE'),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build("sheets", "v4", credentials=credentials)
    return service.spreadsheets()

def append_to_google_sheets(data, sheet_id, sheet_name):
    """Append data to the Google Sheets document."""
    try:
        sheets = authenticate_sheets_api()

        # Print the data to be appended for debugging
        print("Data to append:", data)

        values = [list(item.values()) for item in data]
        body = {
            'values': values
        }

        range_ = f'{sheet_name}!A2'  # Dynamic range for sheet name

        result = sheets.values().append(
            spreadsheetId=sheet_id,
            range=range_,
            valueInputOption="RAW",
            body=body
        ).execute()

        print(f"{result.get('updates').get('updatedCells')} cells updated.")
    except Exception as error:
        print(f"An error occurred while appending: {error}")
'''