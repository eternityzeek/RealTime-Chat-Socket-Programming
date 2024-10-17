import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Server configuration
HOST = '192.168.0.108'  # Change this to your IPv4 Address
PORT = 5555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to host and port
server_socket.bind((HOST, PORT))

# Dictionary to keep track of clients and their usernames
clients = {}

def accept_connections():
    server_socket.listen()
    messages_text.insert(tk.END, f"Server is listening on {HOST}:{PORT}\n")
    while True:
        client_socket, client_address = server_socket.accept()
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = username
        clients_text.config(state=tk.NORMAL)
        clients_text.insert(tk.END, f"{username} ({client_address[0]}:{client_address[1]})\n")
        clients_text.config(state=tk.DISABLED)
        messages_text.insert(tk.END, f"{username} connected from {client_address}\n")
        client_socket.send("Welcome to the chatroom!".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.startswith("@"):
                recipient, message = message[1:].split(":", 1)
                send_personal_message(client_socket, recipient, message)
            else:
                broadcast(message, clients[client_socket])
                messages_text.insert(tk.END, f"{clients[client_socket]}: {message}\n")
        except:
            print(f"{clients[client_socket]} has disconnected")
            del clients[client_socket]
            update_clients_list()
            client_socket.close()
            break

def broadcast(message, sender):
    for connection in clients:
        connection.send(f"{sender}: {message}".encode('utf-8'))

def send_personal_message(sender_socket, recipient, message):
    for connection, username in clients.items():
        if username == recipient:
            connection.send(f"(Private) {clients[sender_socket]}: {message}".encode('utf-8'))
            return

def stop_server():
    for connection in clients:
        connection.close()
    server_socket.close()
    root.quit()

def update_clients_list():
    clients_text.config(state=tk.NORMAL)
    clients_text.delete('1.0', tk.END)
    for client_socket, username in clients.items():
        clients_text.insert(tk.END, f"{username} ({client_socket.getpeername()[0]}:{client_socket.getpeername()[1]})\n")
    clients_text.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Server")
root.geometry("800x600")

# Messages Section
messages_frame = tk.Frame(root)
messages_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

messages_label = tk.Label(messages_frame, text="Messages:", font=("Helvetica", 14, "bold"))
messages_label.pack()

messages_text = scrolledtext.ScrolledText(messages_frame, width=40, height=20, font=("Helvetica", 12))
messages_text.pack(fill=tk.BOTH, expand=True)

# Connected Clients Section
clients_frame = tk.Frame(root)
clients_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

clients_label = tk.Label(clients_frame, text="Connected Clients:", font=("Helvetica", 14, "bold"))
clients_label.pack()

clients_text = scrolledtext.ScrolledText(clients_frame, width=30, height=20, font=("Helvetica", 12))
clients_text.pack(fill=tk.BOTH, expand=True)
clients_text.config(state=tk.DISABLED)

# Stop Server Button
stop_button = tk.Button(root, text="Stop Server", command=stop_server, font=("Helvetica", 12, "bold"), bg="red", fg="white", width=10)
stop_button.pack(pady=10)

# Start the server in a new thread
server_thread = threading.Thread(target=accept_connections)
server_thread.start()

root.mainloop()
