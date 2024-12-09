import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "instagram-scraper-api2.p.rapidapi.com"

def get_recent_posts_by_username(username_or_id_or_url):
    url = f"https://{RAPIDAPI_HOST}/v1.2/posts"
    params = {"username_or_id_or_url": username_or_id_or_url}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            print("Unexpected response format. Expected a JSON object.")
            return {}
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
        return {}
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", response.text)
        return {}
    except Exception as err:
        print(f"Other error occurred: {err}")
        return {}

def get_post_info(code_or_id_or_url):
    url = f"https://{RAPIDAPI_HOST}/v1/post_info"
    querystring = {
        "code_or_id_or_url": code_or_id_or_url,
        "include_insights": "true"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            print("Unexpected response format for post info. Response:", data)
            return {}
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
        return {}
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON for post info. Response was:", response.text)
        return {}
    except Exception as err:
        print(f"Other error occurred: {err}")
        return {}
