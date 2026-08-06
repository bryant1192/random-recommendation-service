import zmq


def send_request(socket, category):
    request = {
        "category": category
    }

    socket.send_json(request)
    return socket.recv_json()


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    categories = [
        "property_improvement",
        "maintenance",
    ]

    for category in categories:
        response = send_request(socket, category)

        print(f"\nCategory: {category}")
        print(response)

    print("\nInvalid category test:")
    print(send_request(socket, "invalid_category"))

    socket.close()
    context.term()


if __name__ == "__main__":
    main()