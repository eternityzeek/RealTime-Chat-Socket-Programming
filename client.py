import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

# Client configuration
HOST = '192.168.0.108'  # Change this to your IPv4 Address
PORT = 5555

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            messages_frame.insert(tk.END, message + '\n')
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send(event=None):
    message = my_message.get()
    my_message.set("")
    client_socket.send(message.encode('utf-8'))
    if message == "/quit":
        client_socket.close()
        root.quit()

def logout():
    my_message.set("/quit")
    send()

def personal_chat():
    recipient = simpledialog.askstring("Personal Chat", "Enter recipient's username:", parent=root)
    if recipient:
        message = simpledialog.askstring("Personal Chat", "Enter your message:", parent=root)
        if message:
            client_socket.send(f"@{recipient}:{message}".encode('utf-8'))

def clear_chat():
    messages_frame.delete('1.0', tk.END)

def connect(event=None):
    global username
    if not connected:
        username = simpledialog.askstring("Username", "Enter your username:", parent=root)
        if username:
            try:
                client_socket.connect((HOST, PORT))
                client_socket.send(username.encode('utf-8'))
                connect_button.config(state=tk.DISABLED)
                logout_button.config(state=tk.NORMAL)
                personal_chat_button.config(state=tk.NORMAL)
                clear_chat_button.config(state=tk.NORMAL)
                connected_label.config(text=f"Connected as: {username}", fg="green")
                send_button.config(state=tk.NORMAL)
                root.title(f"Chatroom - {username}")
                receive_thread = threading.Thread(target=receive)
                receive_thread.start()
                return True
            except Exception as e:
                print(f"Connection Error: {e}")  # Print the error message
                messagebox.showerror("Connection Error", f"Failed to connect to the server: {e}")
                return False
    return False

# GUI setup
root = tk.Tk()
root.title("Client")
root.geometry("400x400")
root.config(bg="#f0f0f0")

my_message = tk.StringVar()
connected = False

# Message frame
message_frame = tk.Frame(root, bg="#f0f0f0")
message_frame.pack(pady=10)

messages_frame = scrolledtext.ScrolledText(message_frame, width=50, height=15, wrap=tk.WORD)
messages_frame.pack()

# Entry field
entry_field = tk.Entry(root, textvariable=my_message, width=40)
entry_field.pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

connect_button = tk.Button(button_frame, text="Connect", command=connect, bg="#b3b3b3", fg="black")
connect_button.pack(side=tk.LEFT, padx=5)

logout_button = tk.Button(button_frame, text="Logout", command=logout, state=tk.DISABLED, bg="#ff4d4d", fg="black")
logout_button.pack(side=tk.LEFT, padx=5)

personal_chat_button = tk.Button(button_frame, text="Personal Chat", command=personal_chat, state=tk.DISABLED, bg="#66ccff", fg="black")
personal_chat_button.pack(side=tk.LEFT, padx=5)

clear_chat_button = tk.Button(button_frame, text="Clear Chat", command=clear_chat, state=tk.DISABLED, bg="#ccff66", fg="black")
clear_chat_button.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(button_frame, text="Send", command=send, state=tk.DISABLED, bg="#00cc66", fg="black")
send_button.pack(side=tk.LEFT, padx=5)

connected_label = tk.Label(root, text="Not connected", fg="red", bg="#f0f0f0")
connected_label.pack(pady=5)

root.mainloop()
