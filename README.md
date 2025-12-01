# Computer Networking(006) Project (Socket Programming)- Homework 3
#TEAM-11
## Overview

This repository contains the coursework for Homework 3 of the Computer
Networking (006) class. The assignment requires you to build a simple network
application using Python’s low‑level socket module (no web frameworks) and to
demonstrate it live. The application consists of a server that listens on a
TCP port and a client that connects to it and sends requests using a
standard protocol such as HTTP. Only raw socket calls (e.g. socket(),
bind(), listen(), accept(), connect(), recv(), send()) are allowed.

The project is split into four roles:

1. **Protocol & Socket Developer** – Implements the core server, accepts
   connections and parses protocol requests.
2. **Client Developer + Extra Features** – Implements the client and adds
   optional features such as file serving, logging or additional request types.
3. **Build & Documentation Lead**  – Organizes the project structure,
   writes this README and the `Makefile`, and ensures everything works from a
   clean clone.
4. **Testing & Contribution Manager** – Tests the application, prepares the demo
   plan and documents individual contributions.

## Repository Structure
```
networking_project/
├── src/              # Python source files
│   ├── server.py     # Server implementation 
│   └── client.py     # Client implementation 
├── Makefile          # Convenient targets for running scripts and cleaning caches
├── README.md         # Project documentation 
└── CONTRIBUTION.md   # Individual contributions
```


## Requirements

Python 3.8 or newer.

No external Python packages are required unless the team decides to add
optional dependencies. If you introduce third‑party libraries, list them in
a file named requirements.txt and instruct users to install them with:

```
  pip install -r requirements.txt
```
## Setup

Clone the repository and navigate into it:

```
git clone https://github.com/hijab1514/networking_project
```
No compilation is necessary. The provided Makefile offers convenience
targets for running the server and client, and for cleaning up .pyc files.

## Running the Server

To start the server on all interfaces (0.0.0.0) and port 8000:
```
python3 src/server.py --host 0.0.0.0 --port 8000

```
Or, if you prefer to use make:
```
make server
```

## Running the Client

To run the client and connect to a server running on localhost port 8000:
```
python3 src/client.py --host localhost --port 8000

```
Using the Makefile:
```
make client
```
Just like the server, we can extend the client’s argument parser to support
additional options (e.g. specifying request paths, sending files, etc.).

### Example Session

Below is a sample workflow to test your application locally. These commands
should be executed from the project root and can be adjusted once your
protocol and features are finalized.

```
# 1. Start the server on port 8080
python3 src/server.py --host 127.0.0.1 --port 8080

# 2. In another terminal, run the client and connect to the server
python3 src/client.py --host 127.0.0.1 --port 8080

# 3. Interact with the server according to your protocol (e.g. send an HTTP GET)
python3 src/client.py --host 127.0.0.1 --port 8080 --method GET --path /

# 4. Use Makefile targets for convenience
make clean    # remove cached .pyc files
make server   # start the server (defaults to host=0.0.0.0 port=8000)
make client   # start the client (defaults to host=localhost port=8000)

```
## Makefile Targets

make server – Runs src/server.py using Python 3 with default host and
port values. You can override the host and port when invoking make:

```
make server HOST=127.0.0.1 PORT=9000

```
make client – Runs src/client.py using Python 3 with default host and
port values. Override the host and port similarly if needed.

make clean – Removes all .pyc files in the project.

Run make without arguments to see a help message.

## Team Members & Contributions

| Member | Role                                 | Core Responsibilities                                                                                                                 |
| -----: | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
|FATIMA- 23013072 | Protocol & Socket Developer          | Implements the Python server, handles incoming connections, parses requests and generates responses.                                  |
|ARIFUL- 24013592| Client Developer + Extra Features    | Implements the Python client, communicates with the server and adds extra features such as logging or file transfer.                  |
|ARAFAT- 24012958 | Build & Documentation Lead  | Writes and maintains the `Makefile` and `README.md`, ensures the project runs from a clean clone, and keeps documentation up to date. |
|ABDULLAH- 24013590| Testing & Contribution Manager       | Tests the system, reports bugs, prepares the demo plan and maintains `CONTRIBUTION.md`.                                               |

