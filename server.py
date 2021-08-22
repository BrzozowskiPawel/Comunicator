import socket
import threading
import messages

# Length of message (first message is 64).
import time

import text_colors

HEADER = 64
# This should be free port.
PORT = 5050
# Getting ip address (SERVER variable).
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# Format of decoding
FORMAT = 'utf-8'
# Setting disconnect flag
DISCONNECT_MESSAGE = "!DISCONNECT"


# Picking socket and binding it to the address.
# We need to put socket family as argument, SOCK_STREAM simply put, it means streaming data.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

active_connection_num = 0

def handle_client(conn, addr):
    messages.new_connection(addr)
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
            messages.msg_from_client(addr,msg)
            if msg != DISCONNECT_MESSAGE and ((threading.activeCount() - 1) > 0):
                messages.type_your_msg("CLIENT")
                message_to_send = input('Type here: ')
            elif msg == DISCONNECT_MESSAGE:
                message_to_send = text_colors.CBLINK2 + 'CONNECTION FROM SERVER LOST' + text_colors.CEND
            # Sending answer back to the client
            conn.send(message_to_send.encode(FORMAT))

    conn.close()


def start():
    # Allowing server to listening for connections
    server.listen()
    messages.listening(SERVER)
    while True:
        # When there is new connection we are storing this connection data.
        conn, addr = server.accept()
        # Creating and starting thread for connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        thread.join()
        # This gives info about how manny clients is connected
        active_connection_num = (threading.activeCount() - 1)
        messages.active_connections(active_connection_num)

messages.starting_server()
start()
input('PLEASE TYPE ENTER TO EXIT')
exit(0)
