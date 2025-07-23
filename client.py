import socket
import threading
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

HOST = '127.0.0.1'  # or the IP if you're connecting via LAN
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(Fore.CYAN + message + Style.RESET_ALL)
        except:
            print(Fore.RED + "[ERROR] Disconnected from server." + Style.RESET_ALL)
            client.close()
            break

def send():
    while True:
        msg = input()
        if msg.strip().lower() == "exit":
            exit_msg = f"[{datetime.now().strftime('%H:%M:%S')}] {name} has left the chat."
            client.send(exit_msg.encode())  # Send exit message to server
            print(Fore.YELLOW + "[INFO] Exiting chat..." + Style.RESET_ALL)
            client.close()
            break
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        full_msg = f"{timestamp} {name}: {msg}"
        client.send(full_msg.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()