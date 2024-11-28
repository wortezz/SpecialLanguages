import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_data(endpoint: str):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API error: {e}")
            return None
