# Random Recommendation Service

A program used to return a random recommendation based on a selected category.

## Usage

`random-recommendation-service` is hosted using **ZeroMQ** and communicates using `socket.send_json()` and `socket.recv_json()`.

To use the service, launch `random_recommendation.py`. Once the program is running, send a JSON object containing the following field:

- `"category"`: A string containing the category to retrieve a recommendation from.

Example:

```python
request = {
    "category": "property_improvement"
}

socket.send_json(request)
response = socket.recv_json()

# Check if error here
# Print the returned recommendation
