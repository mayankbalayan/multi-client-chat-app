# 🧑‍💻 Multi-Client Chat Application using Sockets in Python

This is a **LAN-based multi-user chat application** developed using Python's `socket` and `threading` libraries. It enables multiple clients to connect to a server and exchange real-time messages in a terminal-based interface.

> 💡 Built as a project for the **Computer Networks** course to demonstrate socket programming, TCP communication, and multithreading.

---

## 🛠️ Features

- 🔄 Real-time communication using TCP sockets
- 👥 Supports multiple clients simultaneously
- 🕒 Message timestamping for clarity
- 🎨 Color-coded messages using `colorama`
- 🚪 Graceful exit with broadcasted leave message
- 💻 Simple terminal UI for both server and client

---

## 📌 Technologies Used

- `Python 3`
- `socket` (for network communication)
- `threading` (to handle multiple clients)
- `colorama` (for terminal output formatting)
- `datetime` (for timestamps)

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/mayankbalayan/multi-client-chat-app.git
cd multi-client-chat-app
```
### 2. Start the Server
```bash
python server.py

```
### 3. Start Clients (Run in separate terminals)
```bash
python client.py

```
### 4. Exit Chat
```bash

Type exit and press Enter in the client terminal.
```
 ## 📚 Learning Objectives  
Deepened understanding of TCP/IP and socket communication

Built a multithreaded server to manage concurrent client connections

Practiced clean client-server message formatting with metadata (timestamp, username)

Applied synchronization logic for message broadcasting


✍️ Author
Mayank Balayan
[LinkedIn](https://www.linkedin.com/in/mayankbalayan) • [GitHub](https://github.com/mayankbalayan)

📃 License
This project is open source under the MIT License.


