import os
from dotenv import load_dotenv
import requests

# Airtable configuration
AIRTABLE_TABLE_NAME = 'SEMRush Data'
load_dotenv()
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')

def send_to_airtable(blog_post_record_id, organic_keywords, organic_traffic, organic_cost, prev_organic_keywords, prev_organic_traffic):
    # Ensure all values are integers
    organic_keywords = int(organic_keywords)
    organic_traffic = int(organic_traffic)
    organic_cost = int(organic_cost)
    prev_organic_keywords = int(prev_organic_keywords)
    prev_organic_traffic = int(prev_organic_traffic)

    # Calculate differences
    organic_keywords_diff = organic_keywords - prev_organic_keywords
    organic_traffic_diff = organic_traffic - prev_organic_traffic
    
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "Blog Post": [blog_post_record_id],  
            "Organic Keywords": organic_keywords,
            "Organic Traffic": organic_traffic,
            "Organic Cost": organic_cost,
            "Organic Keywords Change": organic_keywords_diff,
            "Organic Traffic Change": organic_traffic_diff,
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