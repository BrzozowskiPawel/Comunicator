import socket
import messages


messages.IP_confing_info()
SERVER = input("Port:")

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# Below you need to pass YOUR SERVER ip (as a string ex. "192.168.1.1").
ADDR = (SERVER, PORT)

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
    received_msg = client.recv(2048).decode(FORMAT)
    messages.msg_from_server(received_msg)



while True:
    messages.type_your_msg("SERVER")
    msg = input("Type here:")
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        messages.client_disconnect_msg()
        break
        exit(0)