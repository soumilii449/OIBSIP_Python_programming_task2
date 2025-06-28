# OIBSIP_Python_programming_task2
# 💬 Real-Time Chat Application - Python Project

A simple terminal-based real-time chat application built using Python's socket and threading modules. It enables two users to communicate over a local network using a client-server model.

## 🚀 Features

- Real-time message exchange between two users
- Multi-threaded handling of send and receive operations
- Easy-to-use command-line interface
- Lightweight and efficient design

## 🛠️ Technologies Used

- Python 3
- `socket` module
- `threading` module

## 📦 How to Run

### 1. Start the Server

On one machine (or terminal), run:
```bash
python server.py
```

### 2. Start the Client

On another machine or terminal window, run:
```bash
python client.py
```

Make sure both are on the same network and use the correct IP and port as defined in the code.

## 📋 Example

```text
[Client 1] You: Hello!
[Client 2] Friend: Hi there!
```

## 📄 Files Included

- `server.py` – Script to start the chat server
- `client.py` – Script for users to connect and chat

## 🛡️ Note

This is a basic real-time chat app designed for learning purposes and works over local networks.

---

💬 **Real-Time Chat App**  
A basic Python client-server chat application using sockets and multithreading for real-time communication between two users.
