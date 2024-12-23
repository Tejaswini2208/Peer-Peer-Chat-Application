import socket

# Step 1: Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to an IP address and port
host = '127.0.0.1'  # Localhost
port = 12345  # Port number
server_socket.bind((host, port))

# Step 3: Listen for incoming connections
server_socket.listen(1)  # Allow one connection at a time
print(f"Server started on {host}:{port}. Waiting for a connection...")

# Step 4: Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Step 5: Chat loop
while True:
    # Receive message from client
    message = client_socket.recv(1024).decode('utf-8')
    if message.lower() == 'bye':
        print("Client ended the chat.")
        break
    print(f"Client: {message}")

    # Send a reply to the client
    reply = input("You: ")
    client_socket.send(reply.encode('utf-8'))
    if reply.lower() == 'bye':
        print("You ended the chat.")
        break

# Step 6: Close the connection
client_socket.close()
server_socket.close()
