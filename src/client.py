"""
 Member 2 – HTTP Client & Features Developer 
 Author: Rasel MD Ariful Islam
"""

import socket
import sys

BUFFER_SIZE = 4096

def main():

  # Validate command-line arguments
  
  if len(sys.argv) < 5:
        print(f"Usage: python3 {sys.argv[0]} <server_ip> <port> <GET/HEAD> <path>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    method = sys.argv[3].upper()
    path = sys.argv[4]

    # Validate method (GET or HEAD only)
   
  if method not in ["GET", "HEAD"]:
        print("Error: Method must be GET or HEAD.")
        sys.exit(1)

    # Create TCP socket

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client_socket.connect((server_ip, port))
    except Exception as e:
        print("Connection failed:", e)
        sys.exit(1)

    # Build HTTP request (GET or HEAD)
    request = (
        f"{method} {path} HTTP/1.1\r\n"
        f"Host: {server_ip}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

    # Send request
    client_socket.sendall(request.encode())

    print("\n=== HTTP Request Sent ===")
    print(request)

    # Receive server response
    print("=== Server Response ===\n")

    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        print(data.decode(errors="replace"), end="")

    # Close connection
    client_socket.close()
    print("\n\n[Client Finished]")


if __name__ == "__main__":
    main()

