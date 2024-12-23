import socket

# Step 1: Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
host = '127.0.0.1'  # Server IP
port = 12345  # Server port
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

# Step 3: Chat loop
while True:
    # Send a message to the server
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))
    if message.lower() == 'bye':
        print("You ended the chat.")
        break

    # Receive a reply from the server
    reply = client_socket.recv(1024).decode('utf-8')
    if reply.lower() == 'bye':
        print("Server ended the chat.")
        break
    print(f"Server: {reply}")

# Step 4: Close the connection
client_socket.close()
