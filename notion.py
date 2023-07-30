import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

my_page = notion.databases.query(
    **{
        "database_id": "897e5a76-ae52-4b48-9fdf-e71f5945d1af",
        "filter": {
            "property": "Landmark",
            "rich_text": {
                "contains": "Bridge",
            },
        },
    }
)