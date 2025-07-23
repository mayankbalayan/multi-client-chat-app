# this is the server side of the multi chat 
import socket
import threading
# Listens on all network interfaces (127.0.0.1 for localhost)
HOST = '0.0.0.0'  
PORT = 12345
clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if "has left the chat" in message:
                print(f"{message}")
                broadcast(message, client)  # Broadcast the exit message
                clients.remove(client)
                client.close()
                break
            broadcast(message, client)
        except:
            if client in clients:
                clients.remove(client)
            client.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[STARTED] Chat server running on {HOST}:{PORT}")
    
    while True:
        client, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

start_server()