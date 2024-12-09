from bs4 import BeautifulSoup
import requests

def search_influencers(topic):
    query = f"top Instagram influencers in {topic}"
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = [a.text for a in soup.find_all("h3")]
        return results[:10]
    else:
        raise Exception("Failed to fetch search results.")
