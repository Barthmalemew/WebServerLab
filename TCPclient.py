import socket as s

port = 8080

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

file_path = input("Enter the requested file: ")

http_request = f"GET /{file_path} HTTP/1.1\r\nHost: localhost\r\n\r\n"

client_socket.send(http_request.encode())

server_message = b''
while True:
    data = client_socket.recv(2048)
    if not data:
        break
    server_message += data

print(server_message.decode())

response_headers, _, response_body = server_message.decode().partition('\r\n\r\n')

print("File content:")
print(response_body)

client_socket.close()