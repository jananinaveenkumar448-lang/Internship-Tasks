import requests
URL = "https://jsonplaceholder.typicode.com/users"
def fetch_top_users():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 404:
            print("Error: 404 - Resource not found")
            return
        response.raise_for_status()
        users = response.json()
        top_5_users = users[:5]
        print("\nTOP 5 USERS")
        print("-" * 50)
        print(f"{'NAME':<25} {'EMAIL'}")
        print("-" * 50)
        for user in top_5_users:
            print(f"{user['name']:<25} {user['email']}")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
    except requests.exceptions.ConnectionError:
        print("Error: Connection error")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    fetch_top_users()