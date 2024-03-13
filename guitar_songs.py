from __future__ import print_function
import os
from webbrowser import get
import gspread
from dotenv import load_dotenv
from google.oauth2 import service_account
import pandas as pd
import json
import random

load_dotenv()

service_account_file = os.getenv('SERVICE_ACCOUNT_FILE')
song_json_file = os.getenv('SONG_JSON_FILE')

# Uses google.oauth2 module to link this code to Google Sheets and get all records from the workbook

credentials = service_account.Credentials.from_service_account_file(service_account_file)
scoped_credentials = credentials.with_scopes('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
gc = gspread.service_account(filename=service_account_file)
sheet = gc.open('Guitar Song List').get_worksheet(0)
get_all_records = sheet.get_all_records()

# Create a dataframe for organization and drop all empty cells
df = pd.DataFrame(get_all_records)
dropEmpty = df.dropna()

# Get the total number of artists and get the longest column that doesn't have blanks
totalArtists = df.iloc[2][0]
longestColumn = (df.count().max()) - 1

def getChoices():
    # Randomly select one artist and one song at random and convert to JSON
    randomArtist = random.randint(1,totalArtists)

    # Because of the way the sheet is organized, I may know a lot more songs from one artist than another
    # This will result in some columns having a lot of empty cells
    # Which means, conceptually, an artist with an empty song choice could be returned, which isn't good
    # By selecting a song from the longest filled column, this prevents that issue
    
    randomSong = random.randint(0,longestColumn)
    df_to_json = df.to_json(orient="split")
    json_object = json.loads(df_to_json)
    
    # Set the randomly selected artist and song to a JSON object
    artistChoice = json_object["columns"][randomArtist]
    songChoice = json_object["data"][randomSong][randomArtist]

    if songChoice != "":
       # Write the selected song and artist to a JSON file, which will be displayed on the frontend when triggered by pressing the "Submit" button
       final = artistChoice, songChoice
       finalJSON = json.dumps(final)
       print(finalJSON)

       with open(song_json_file,"w") as outfile:
            outfile.write(finalJSON)
    else:
        # If, for some reason, the song choice returns an empty song, recursively run the function again until it selects a cell with a song value
        return getChoices()

getChoices()