
import os
from notion_client import Client

class Notion_Umlautwandler:
    
    notion = Client(auth=os.environ['secret_m83w1Be6sq8f5BLkj7jumYKPJ1Kaz1JeXcLb1MuVuIw'])

    database_id = "1001844ceac24d748760759a3cea0521"

    replacements = {
        "uueee": "ü",
        "aaeee": "ä",
        "ooeee": "ö",
        "ssss": "ß",
        "Uueee": "Ü",
        "Aaeee": "Ä",
        "Ooeee": "Ö"
    }

    results = notion.databases.query(
        **{
            "database_id": database_id,
            "filter": {
                "property": "Name",
                "title": {
                    "contains": "Suchbegriff"
                }
            }
        }
    ).get("results") # type: ignore

    for result in results:
        text = result.properties["Text"].rich_text[0].text.content.lower()
        for key, value in replacements.items():
            if key in text:
                text = text.replace(key, value)
                result.properties["Text"].rich_text[0].text.content = text
                notion.pages.update(result["id"], properties=result.properties)
