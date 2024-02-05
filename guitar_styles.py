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

credentials = service_account.Credentials.from_service_account_file(service_account_file)
scoped_credentials = credentials.with_scopes('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
gc = gspread.service_account(filename=service_account_file)
sheet = gc.open('Guitar Song List').get_worksheet(4)

rock = sheet.get_all_records()

df = pd.DataFrame(rock)
dropEmpty = df.dropna()

totalGuitarists = df.iloc[0][0]
longestColumn = (df.count().max()) - 1

def getChoices():
    randomGuitarist = random.randint(0,totalGuitarists)
    randomStyle = random.randint(0,longestColumn)
    guitarist_and_style = df.to_json(orient="split")
    json_object = json.loads(guitarist_and_style)
    
    guitaristChoice = json_object["columns"][randomGuitarist]
    styleChoice = json_object["data"][randomStyle][randomGuitarist]

    if styleChoice != "":
       final = guitaristChoice, styleChoice
       finalJSON = json.dumps(final)
       print(finalJSON)

       with open(style_json_file,"w") as outfile:
        outfile.write(finalJSON)

    else:
        # print("No good - try again!")
        return getChoices()

getChoices()