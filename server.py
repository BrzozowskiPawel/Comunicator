import socket
import threading

# Length of message (first message is 64).
import time

HEADER = 64
# This should be free port.
PORT = 5050
# Getting ip address (SERVER variable).
hostname = socket.gethostname()
SERVER = socket.gethostbyname(hostname)
ADDR = (SERVER, PORT)
# Format of decoding
FORMAT = 'utf-8'
# Setting disconnect flag
DISCONNECT_MESSAGE = "!DISCONNECT"

# Picking socket and binding it to the address.
# We need to put socket family as argument, SOCK_STREAM simply put, it means streaming data.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # Blocking line of code, we will not pass this line until we will receive message from client.
    # This need to be thread to not block server. In bracket we type how many bites we accept.
    # msg_length is receiving information how long message will be
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # This fix error when message is blank.
        if msg_length:
            msg_length = int(msg_length)
            # This is final message that receive
            msg = conn.recv(msg_length).decode(FORMAT)
            # Client should use "!DISCONNECT" to disconnect property,
            # in other cases client could have problems with reconnecting.
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[SERVER]{addr} {msg}")
            # When we receive message, we encode it and send it back
            conn.send(f"[SERVER] Msg received ({msg})".encode(FORMAT))

    conn.close()


def start():
    # Allowing server to listening for connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # When there is new connection we are storing this connection data.
        conn, addr = server.accept()
        # Creating and starting thread for connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        thread.join()
        # This gives info about how manny clients is connected
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
input()
exit(0)
