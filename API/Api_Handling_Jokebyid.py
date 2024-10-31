import requests
import random

url="https://api.freeapi.app/api/v1/public/randomjokes"
response = requests.get(url)
data = response.json()

def get_data_from_api():
    try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure there was no error in the request
            data = response.json()

            if data['success'] and 'data' in data:
                jokes = data['data']['data']
                random_joke = random.choice(jokes)
                joke_content = random_joke['content']
                joke_id = random_joke['id']
                print(f"Joke ID: {joke_id}")
                print(f"Joke: {joke_content}")
            else:
                raise Exception("Failed to load joke data")
    except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

def main():
    get_data_from_api()

if __name__ =="__main__":
    main()