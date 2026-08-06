# Random Recommendation Service

A program used to return a random recommendation based on a selected category.

## Usage

`random-recommendation-service` is hosted using **ZeroMQ** and communicates using `socket.send_json()` and `socket.recv_json()`.

To use the service, launch `random_recommendation.py`. Once the program is running, send a JSON object containing the following field:

- `"category"`: A string containing the category to retrieve a recommendation from.

The service is hosted on port `5555`.
 
Example:

```python
request = {
    "category": "property_improvement"
}

socket.send_json(request)
response = socket.recv_json()

# Check if error here
# Print the returned recommendation
```

## Example Categories

- `property_improvement`
- `maintenance`
- `random_event`
- `item`
- `encounter`

## Return Values

A JSON object will be returned with **one of two keys**:

### `"recommendation"`

The program will respond with a randomly selected recommendation from the requested category.

Example:

```json
{
    "recommendation": "Add clearer parking instructions to your listing."
}
```

or

```json
{
    "recommendation": "A traveling merchant appears and offers a rare item."
}
```

### `"error"`

The program will respond with an error code. Error codes are listed below.

## Possible Error Numbers

**Note:** These error codes are returned as integers.

| Error Code | Description |
|------------|-------------|
| **1** | The program could not decode the JSON request. |
| **2** | The request was not valid JSON or did not contain the required `"category"` field. |
| **3** | The requested category does not exist. |
| **4** | The requested category exists but contains no recommendations. |
