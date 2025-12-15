PYTHON := python
HOST   ?= 127.0.0.1
PORT   ?= 8080
METHOD ?= GET
PATH   ?= /

.PHONY: server client clean help

## Run the Python server
server:
	@echo "Starting server on port $(PORT)..."
	$(PYTHON) server.py

## Run the Python client
client:
	@echo "Connecting to $(HOST):$(PORT)"
	$(PYTHON) client.py $(HOST) $(PORT) $(METHOD) $(PATH)

## Remove compiled Python cache files
clean:
	@echo "Removing cached .pyc files..."
	find . -name '*.pyc' -delete

## Show help
help:
	@echo "Available Makefile targets:"
	@echo "  make server"
	@echo "  make client METHOD=GET PATH=/"
	@echo "  make client METHOD=GET PATH=/abc"
	@echo "  make clean"
