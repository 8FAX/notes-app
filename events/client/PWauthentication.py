import socket

def send_data(data):
    HOST = '127.0.0.1'  # Change this to the IP address or hostname of your server
    PORT = 9999  # Change this to the port number your server is running on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode('utf-8'))  # Ensure data is encoded as bytes before sending
        response = s.recv(1024).decode('utf-8')
    return response

def authenticate(username, password):
    username = username.strip()
    password = password.strip()
    data = f"authenticate={username}={password}"
    responce = send_data(data)
    if responce[0:] == "success":
        return True
    else:
        error_split = responce.split(",")
        error_format = error_split[1][2:-2]
        return False, error_format