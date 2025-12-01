PYTHON := python3
# Default host and port; can be overridden on the command line
HOST   ?= 0.0.0.0
PORT   ?= 8000

.PHONY: all server client clean help

## Default target: show help
all: help

## Run the Python server
server:
	@echo "Starting server on $(HOST):$(PORT)..."
	$(PYTHON) src/server.py --host $(HOST) --port $(PORT)

## Run the Python client
client:
	@echo "Starting client connecting to $(HOST):$(PORT)..."
	$(PYTHON) src/client.py --host $(HOST) --port $(PORT)

## Remove compiled Python bytecode files
clean:
	@echo "Removing cached .pyc files..."
	find . -name '*.pyc' -delete

## Display available targets and usage
help:
	@echo "Available Makefile targets:"
	@echo "  make server HOST=<addr> PORT=<port>  - Run the server (defaults to 0.0.0.0:8000)"
	@echo "  make client HOST=<addr> PORT=<port>  - Run the client (defaults to localhost:8000)"
	@echo "  make clean                          - Remove .pyc files"
	@echo "  make help                           - Show this help message"
