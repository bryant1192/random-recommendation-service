import random
import zmq


RECOMMENDATIONS = {
    "property_improvement": [
        "Add clearer parking instructions to your listing.",
        "Include more details about nearby attractions.",
        "Add high-quality photos of each room.",
        "Clearly list the Wi-Fi and check-in information."
    ],
    "maintenance": [
        "Check the smoke detectors.",
        "Inspect the air conditioning system.",
        "Test the locks and entry codes.",
        "Check for plumbing leaks."
    ],
}


def get_recommendation(request):
    if not isinstance(request, dict):
        return {"error": 2}

    if "category" not in request:
        return {"error": 2}

    category = request["category"]

    if not isinstance(category, str):
        return {"error": 2}

    if category not in RECOMMENDATIONS:
        return {"error": 3}

    recommendations = RECOMMENDATIONS[category]

    if len(recommendations) == 0:
        return {"error": 4}

    return {
        "recommendation": random.choice(recommendations)
    }


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Random Recommendation Service is running on port 5555...")

    while True:
        try:
            request = socket.recv_json()
        except ValueError:
            socket.send_json({"error": 1})
            continue

        response = get_recommendation(request)
        socket.send_json(response)


if __name__ == "__main__":
    main()