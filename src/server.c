#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};

    // 1. Create TCP socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // 2. Bind socket to port
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // 3. Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("HTTP server listening on port %d\n", PORT);

    // 4. Accept connections loop
    while (1) {
        if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
            perror("accept");
            continue;
        }

        // 4a. Clear buffer and read HTTP request
        memset(buffer, 0, BUFFER_SIZE);
        read(new_socket, buffer, BUFFER_SIZE);
        printf("Received request:\n%s\n", buffer);

        // 4b. Parse request line: METHOD PATH VERSION
        char method[16], path[256], version[16];
        sscanf(buffer, "%s %s %s", method, path, version);
        printf("Parsed request:\nMethod: %s\nPath: %s\nVersion: %s\n", method, path, version);

        // 4c. Parse HTTP headers
        printf("Headers:\n");
        char *line = strtok(buffer, "\r\n");  // start from first line
        line = strtok(NULL, "\r\n");           // skip request line
        while (line != NULL && strlen(line) > 0) {
            printf("%s\n", line);
            line = strtok(NULL, "\r\n");
        }

        // 4d. Basic routing
        char response[BUFFER_SIZE];
        if (strcmp(path, "/") == 0) {
            sprintf(response, "HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!");
        } else {
            sprintf(response, "HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found");
        }

        // 4e. Send response
        write(new_socket, response, strlen(response));

        // 4f. Close connection
        close(new_socket);
    }

    return 0;
}
