import socket
dev = True

def check_connection(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            return True
    except:
        return False
    
def send_data(data):
    HOST = '127.0.0.1' 
    PORT = 9999 

    connection = check_connection(HOST, PORT)
    if connection == False and dev == False:
        return "error, Server is not running"
    if connection == False and dev == True:
        return "success"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.encode('utf-8'))  
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
        error_format = error_split[1][0:]
        return False, error_format