import socket

# Constants below are described in server.py, to save space I didn't put the same comments here.
PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# Below you need to pass YOUR SERVER ip (as a string ex. "192.168.1.1").
SERVER = '192.168.1.3'
ADDR = (SERVER,PORT)

# Establishing connection to server (IP and port as tuples).
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # We need to encode message.
    message = msg.encode(FORMAT)
    # Same as before, we need to send message and also it length.
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # We need to send first message with length of original message.
    # However it need to be 64 because this is set set length of header.
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # Printing received message from server.
    print(f"[CLIENT] {client.recv(2048).decode(FORMAT)}")

# Dummy content message for testing purposes.
send("Hello World!")
input()
send(DISCONNECT_MESSAGE)

exit(0)