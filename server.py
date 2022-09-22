import socket
import threading
import random
ENCODING = 'utf-8'


def handle_client(conn, addr, quotes, file_handler):
    print("Handling connection from {}".format(addr))
    number = random.randint(0,29)
    print(number)
    while conn:
        quote  = quotes[number]
        message = conn.recv(25)
        print(message.decode())
        if "network" in message.decode():
            message_to_send = "Hello there " + str(addr) + ". Here is another random quote of wisdom for you:" + quote
            print(message_to_send)
            file_handler.write(message_to_send)
            conn.send(message_to_send.encode())
        break
        #TODO: handle connection closing from client

if __name__ == '__main__':
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
    log = open('logfile', 'a')
    #create a TCP socket
    print("Creating a socket")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #create a UDP socket
    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #IP_ADDR = '0.0.0.0'
    #gethostbyname()
    print ("Socket successfully created")
    port = 3389
    server_socket.bind(('', port))        
    print ("socket binded to %s" %(port))
    server_socket.listen(5)    
    print ("socket is listening")
    
    #PORT = 8002
    #SERVER_ADDR = (IP_ADDR, PORT)
    #print("Binding to {}".format(SERVER_ADDR))
    #server_socket.bind(SERVER_ADDR)

    #server_socket.listen()
    #print("Server is listening on {}".format(SERVER_ADDR))

    while True:
        connection, address = server_socket.accept()
#        print("Received a connection from {}".format(connection))
        thread = threading.Thread(target=handle_client, args=(connection, address, quotes, log))
        thread.start()