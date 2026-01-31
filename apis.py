import requests
from dotenv import load_dotenv
import os

def get_apod():
    load_dotenv()
    url = "https://api.nasa.gov/planetary/apod?api_key="
    unique_key = os.getenv("NASA_API_KEY")
    final_url = url + unique_key
    return requests.get(final_url).json()