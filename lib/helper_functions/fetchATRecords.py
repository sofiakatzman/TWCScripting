import os
from dotenv import load_dotenv
from airtable import Airtable
from semrushAnalytics import send_semrush_request 

load_dotenv()

# Airtable configuration
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_API_KEY= os.getenv('AIRTABLE_API_KEY')
AIRTABLE_TABLE_NAME = 'Blog Posts'
AIRTABLE_VIEW_NAME = 'Published Blog Post'

# Initialize Airtable client
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

def fetch_and_process_records():
    # Fetch all records from a specific view in Airtable
    records = airtable.get_all(view=AIRTABLE_VIEW_NAME)
    
    # Process each record
    for record in records:
        # Extract relevant data from the record
        blog_post_record_id = record['id']  
        url = record['fields'].get('Published URL') 
        
        print(blog_post_record_id)
        print(url)
        
        # Call your semRushAnalytics function if there is a URL and Blog Record (otherwise AT will fail)
        if url and blog_post_record_id:
            # timeout in case too many requests are being sent at once
            # time.sleep(60) 
            send_semrush_request(blog_post_record_id, url)
        else:
            # Handle the case where either url or blog_post_record_id is missing
            if not url:
                print("URL is missing")
            if not blog_post_record_id:
                print("Blog post record ID is missing")

# Call the function to fetch and process records
fetch_and_process_records()