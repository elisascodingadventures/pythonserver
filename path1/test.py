import requests

base = "http://127.0.0.1:8000"  # Adjust the URL as per your server setup
endpoint_path = "/test"  # Adjust the endpoint path as needed
url = base + endpoint_path
response = requests.get(url)

print(response.status_code)
print(response.json())