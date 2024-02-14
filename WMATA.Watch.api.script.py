import requests

# Your actual WMATA API key
api_key = '9cbe4dcd63484dcba8eabea07e0f9a39'

# The URL for the WMATA API endpoint you're accessing
url = 'https://api.wmata.com/Bus.svc/json/jBusPositions?RouteID=31'

# Parameters for the request, including the RouteID
params = {
    'RouteID': '31',
    'api_key': api_key  # Some APIs require the key as a query parameter, but WMATA needs it in the header.
}

# The headers where you include your API key
headers = {'api_key': '9cbe4dcd63484dcba8eabea07e0f9a39'}

# Make the GET request to the WMATA API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    bus_positions = response.json()
    # Print the result
    print(bus_positions)
else:
    print(f"Failed to retrieve data: {response.status_code}")
