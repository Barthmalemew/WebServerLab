import socket as s

host = 'localhost'
post = 8080

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((host, post))

server_socket.listen()
print("The server is ready to receive")

while True:
    connection_socket, client_address = server_socket.accept()
    client_message = connection_socket.recv(2048).decode()

    requested_file = client_message.split()[1][1:]

    try:
        file = open(requested_file, 'rb')
        file_content = file.read()
    except FileNotFoundError:
        print("File Not Found")

    if file_content:
        status_code = b"HTTP/1.1 200 OK\r\n"
    else:
        status_code = b"HTTP/1.1 404 Not Found\r\n"

    response_header = status_code + b"\r\n"
    response_body = file_content if file_content else b"File Not Found"

    connection_socket.send(response_header + response_body)

    connection_socket.close()