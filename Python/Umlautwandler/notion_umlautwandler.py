import json, requests

import os
from notion_client import Client
from datetime import datetime
import re

class Notion_Umlautwandler:

    file = open('Scret.json')

    data = json.load(file)
    
    notion = Client(auth=os.environ[data['database_id']])

# Initialize a client object with your API key
    client = Client(auth=data['notion_api_key'])

# Specify the ID of your database
    database_id = data['database_id']

    file.close()

    url = 'https://api.notion.com/v1/pages'

    headers = {
        'Authorization': f'Bearer {database_id}',
        'Content-Type': 'application/json',
        'Notion-version': '2021-08-16'
    }

    data_input = {
        "parent": { "database_id": f"{database_id}" },
    "properties": {
      "title": {
        "title": [
          {
            "text": {
              "content": "Yurts in Big Sur, California"
            }
          }
        ]
      }
    }
    }

    response = requests.post(url, headers=headers, json= data_input)
 

# Specify the search query
    query = "INSERT_SEARCH_QUERY_HERE"    

# Get a reference to the database
    database = client.databases.retrieve(database_id)

    umlaute = ["aaeee", "Aaeee", "ooeee", "Ooeee", "uueee", "Uueee", "sssss"]

    words_to_replace = []
    
    
    def replace(string):
        # Replace "aee" with "ä"
        string = string.replace("aaeee", "ä") # type: ignore

        string = string.replace("Aaeee", "Ä")

# Replace "oee" with "ö"
        string = string.replace("ooeee", "ö")

        string = string.replace("Ooeee", "Ö")

# Replace "uee" with "ü"
        string = string.replace("uueee", "ü")

        string = string.replace("Uueee", "Ü")

        string = string.replace("sssss", "ß")

# Create a new page in the database with the transformed string
   

    results = client.databases.query(
        **{
            "database_id": database_id,
            "filter": {
                "property": "Name",
                "title": {}
            }
        }
    )["results"] # type: ignore

# Extract all words from the "Description" property of each item
    all_words = []
    for result in results:
        description = result.properties["Description"]["rich_text"][0]["text"]["content"]
        words = re.findall(r'\w+', description)
        all_words += words

# Print all words
    for word in all_words:
        for umlaute in umlaute:
            if  umlaute in word:
                words_to_replace += [word, replace(word)]
    
    finds = notion.databases.query(
        **{
            "databases_id": database_id,
            "filter": {
                "contains": query
            }
        }
    ).get("finds", []) # type: ignore

    for find in finds:
        name = find.get("properties", {}).get("Name", {}).get("title", [{}])[0].get("plain_text", "")

        new_name = name.replace("TARGET_WORD", "REPLACEMENT_WORD")

        notion.pages.update(find["id"], properties={"Name": {"title": [{"text": {"content": new_name}}]}})

    