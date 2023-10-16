import requests

API_KEY = 'AIzaSyDdB7Qb1gh_eOGbC6vnDHj2LsndbXPRDEs'

CUSTOM_SEARCH_ENGINE_ID = '33b667c75076b4da2'

def scrape_google_results(query, num_results=10):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "num": num_results,
        "key": API_KEY,
        "cx": CUSTOM_SEARCH_ENGINE_ID,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        for i, item in enumerate(items, start=1):
            title = item.get('title', 'No title available')
            link = item.get('link', 'No link available')
            snippet = item.get('snippet', 'No snippet available')

            print(f"Result {i}:")
            print("Title:", title)
            print("Link:", link)
            print("Snippet:", snippet)
            print()


search_query = "Software Firma [Wien]"
scrape_google_results(search_query)