import socket
import threading

clients = []

# Relay messages from one client to another
def handle_client(client, addr):
    print(f"[CONNECTED] {addr} connected.")
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            # Send to the other client
            for c in clients:
                if c != client:
                    c.send(msg)
        except:
            break
    print(f"[DISCONNECTED] {addr} disconnected.")
    clients.remove(client)
    client.close()

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

print(f"[WAITING] Server listening on {HOST}:{PORT}...")

while len(clients) < 2:
    client_socket, client_addr = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
    thread.start()

print("[CHAT STARTED] Two clients connected. They can now chat.")
