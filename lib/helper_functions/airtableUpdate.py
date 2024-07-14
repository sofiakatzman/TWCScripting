import os
from dotenv import load_dotenv
import requests
from airtable import Airtable

# Airtable configuration
AIRTABLE_TABLE_NAME = 'SEMRush Data'
load_dotenv()
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY= os.getenv('AIRTABLE_API_KEY')

def send_to_airtable(blog_post_record_id, organic_keywords, organic_traffic, organic_cost):
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "Blog Post": [blog_post_record_id],  
            "Organic Keywords": int(organic_keywords),
            "Organic Traffic": int(organic_traffic),
            "Organic Cost": int(organic_cost),
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print("Record created successfully in Airtable")
    else:
        print(f"Failed to create record in Airtable: {response.status_code}, {response.text}")

# # Example data
# blog_post_id = 123456
# blog_post_record_id = "recdetILDj5jK4imO" 
# organic_keywords = 123456
# organic_traffic = 123456
# organic_cost = 123456

# # Call the function
# send_to_airtable(blog_post_record_id, organic_keywords, organic_traffic, organic_cost