import text_colors


def starting_server():
    print(text_colors.CGREENBG + text_colors.CBOLD + "[STARTING]"+ text_colors.CEND + text_colors.CGREEN +" server is starting" + text_colors.CEND)


def listening(SERVER):
    print(text_colors.CBLUEBG2 + text_colors.CBOLD + "[LISTENING]" + text_colors.CEND + text_colors.CBLUE + " server is listening on "+ text_colors.CBOLD +f"{SERVER}" + text_colors.CEND)


def active_connections(active_connection_num):
    print(text_colors.CVIOLETBG + text_colors.CBOLD + "[ACTIVE CONNECTIONS]"+ text_colors.CEND + f" {active_connection_num}")

def new_connection(addr):
    print(text_colors.CVIOLETBG + text_colors.CBOLD + "[NEW CONNECTION]" + text_colors.CEND + text_colors.CVIOLET2+ f" {addr} connected."+ text_colors.CEND)


def msg_from_client(addr, msg):
    if msg != "!DISCONNECT":
        print(text_colors.CYELLOWBG + text_colors.CBOLD + "[FROM CLIENT]" + text_colors.CEND +  text_colors.CITALIC+ f"{addr}" + text_colors.CBOLD+f": {msg}" + text_colors.CEND)
    elif msg == "!DISCONNECT":
        print(text_colors.CREDBG2 + text_colors.CBOLD + "[CLIENT DISCONNECTED]" + text_colors.CEND  + text_colors.CRED2 + text_colors.CBOLD + f" command used: {msg}" + text_colors.CEND)

def msg_from_server(msg):
    print(text_colors.CYELLOWBG + text_colors.CBOLD + "[FROM SERVER]" + text_colors.CEND + text_colors.CYELLOW2 + text_colors.CBOLD+f" {msg}" + text_colors.CEND)

def type_your_msg(send_to):
    print( text_colors.CYELLOW2 + f"Please type your msg to be send to the " + text_colors.CEND+ text_colors.CBOLD + text_colors.CYELLOW2 + f"{send_to}" + text_colors.CEND)

def client_disconnect_msg():
    print(text_colors.CBLINK + 'SESSION CLOSED - you can exit app' + text_colors.CEND)