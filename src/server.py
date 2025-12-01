import socket

PORT = 8080
BUFFER_SIZE = 1024

def main():
    # 1. Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(3)

    print(f"HTTP server listening on port {PORT}")

    while True:
        # 2. Accept a connection
        client_socket, address = server_socket.accept()
        print(f"Connected from {address}")

        # 3. Read HTTP request
        request = client_socket.recv(BUFFER_SIZE).decode()
        print("Received request:\n" + request)

        # 4. Parse request line
        try:
            method, path, version = request.split("\r\n")[0].split(" ")
        except ValueError:
            client_socket.close()
            continue

        print(f"Parsed request:\nMethod: {method}\nPath: {path}\nVersion: {version}\n")

        # 5. Parse headers
        print("Headers:")
        lines = request.split("\r\n")[1:]
        for line in lines:
            if line == "":
                break
            print(line)

        # 6. Basic routing
        if path == "/":
            body = "Hello, World!"
            response = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
        else:
            body = "Not Found"
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )

        # 7. Send response
        client_socket.sendall(response.encode())

        # 8. Close connection
        client_socket.close()


if __name__ == "__main__":
    main()
