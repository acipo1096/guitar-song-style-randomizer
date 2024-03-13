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

# Uses google.oauth2 module to link this code to Google Sheets

credentials = service_account.Credentials.from_service_account_file(service_account_file)
scoped_credentials = credentials.with_scopes('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
gc = gspread.service_account(filename=service_account_file)
sheet = gc.open('Guitar Song List').get_worksheet(0)


get_all_records = sheet.get_all_records()

df = pd.DataFrame(get_all_records)
dropEmpty = df.dropna()

totalArtists = df.iloc[2][0]
longestColumn = (df.count().max()) - 1

def getChoices():
    randomArtist = random.randint(1,totalArtists)
    randomSong = random.randint(0,longestColumn)
    df_to_json = df.to_json(orient="split")
    json_object = json.loads(df_to_json)
    
    artistChoice = json_object["columns"][randomArtist]
    songChoice = json_object["data"][randomSong][randomArtist]

    if songChoice != "":
       final = artistChoice, songChoice
       finalJSON = json.dumps(final)
       print(finalJSON)

       with open(song_json_file,"w") as outfile:
            outfile.write(finalJSON)
    else:
        return getChoices()

getChoices()