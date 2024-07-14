import os
from dotenv import load_dotenv
import requests
from airtableUpdate import send_to_airtable

# SEMrush configuration
SEMRUSH_API_URL = 'https://api.semrush.com/'
load_dotenv()
SEMRUSH_API_KEY = os.getenv('SEMRUSH_API_KEY')

# Send request to SEMrush API for URL rank data
def send_semrush_request(blog_post_record_id, url):
    params = {
        'key': SEMRUSH_API_KEY,
        'url': url,
        'type': 'url_rank',
        'database': 'us'
    }
    
    try:
        response = requests.get(SEMRUSH_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad response status codes

        # Decode the response content
        content = response.content.decode('utf-8')

        # Split content by lines
        lines = content.strip().split('\r\n')

        # Check if lines array has enough elements
        if len(lines) < 2:
            print("Error: Unexpected response format from SEMrush API")
            return

        # Parse header and data separately
        header = lines[0].split(';')
        data = lines[1].split(';')

        # Create key-value pairs
        result = {header[i]: data[i] for i in range(min(len(header), len(data)))}

        # Extract SEMrush data points
        organic_keywords = result.get('Organic Keywords', '')  # Default to empty string if key not found
        organic_traffic = result.get('Organic Traffic', '')
        organic_cost = result.get('Organic Cost', '')

        # Send data to Airtable
        send_to_airtable(blog_post_record_id, organic_keywords, organic_traffic, organic_cost)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching SEMrush data: {e}")

    except Exception as e:
        print(f"Error: {e}")
