import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print("\nFriend:", msg)
        except:
            break

def send_messages(sock):
    while True:
        msg = input()
        try:
            sock.send(msg.encode())
        except:
            break

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the server. Start chatting!")

# Start two threads
recv_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))
recv_thread.start()
send_thread.start()
