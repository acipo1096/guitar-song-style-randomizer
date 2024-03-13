from __future__ import print_function
import os
from webbrowser import get
from dotenv import load_dotenv
import gspread
from google.oauth2 import service_account
import pandas as pd
import json
import random

load_dotenv()

service_account_file = os.getenv('SERVICE_ACCOUNT_FILE')
style_json_file = os.getenv('STYLE_JSON_FILE')

# Uses google.oauth2 module to link this code to Google Sheets and get all records from the workbook

credentials = service_account.Credentials.from_service_account_file(service_account_file)
scoped_credentials = credentials.with_scopes('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
gc = gspread.service_account(filename=service_account_file)
sheet = gc.open('Guitar Song List').get_worksheet(4)
get_all_records = sheet.get_all_records()

# Create a dataframe for organization and drop all empty cells
df = pd.DataFrame(get_all_records)
dropEmpty = df.dropna()

# Get the total number of guitarists and get the longest column that doesn't have blanks
totalGuitarists = df.iloc[0][0]
longestColumn = (df.count().max()) - 1

def getChoices():
    # Randomly select one guitarist and one style at random and convert to JSON
    randomGuitarist = random.randint(0,totalGuitarists)

    # Because of the way the sheet is organized, I may know a lot more songs from one artist than another
    # This will result in some columns having a lot of empty cells
    # Which means, conceptually, an artist with an empty song choice could be returned, which isn't good
    # By selecting a song from the longest filled column, this prevents that issue
    
    randomStyle = random.randint(0,longestColumn)
    guitarist_and_style = df.to_json(orient="split")
    json_object = json.loads(guitarist_and_style)
    
    # Set the randomly selected guitarist and style to a JSON object
    guitaristChoice = json_object["columns"][randomGuitarist]
    styleChoice = json_object["data"][randomStyle][randomGuitarist]

    if styleChoice != "":
       final = guitaristChoice, styleChoice
       finalJSON = json.dumps(final)
       print(finalJSON)

       with open(style_json_file,"w") as outfile:
        outfile.write(finalJSON)

    else:
        # If, for some reason, the style choice returns an empty song, recursively run the function again until it selects a cell with a style value
        return getChoices()

getChoices()