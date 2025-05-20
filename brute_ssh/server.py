import socket
import sys
import paramiko

USERNAME = "testuser"
PASSWORD = "testpass"

host_key = paramiko.RSAKey.generate(2048)

class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

def start_ssh_server(host="127.0.0.1", port=22):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(100)
        print(f"[+] SSH Server listening on {host}:{port}")
        
        while True:
            client, addr = sock.accept()
            print(f"[+] Connection from {addr}")

            transport = paramiko.Transport(client)
            transport.add_server_key(host_key)
            server = SSHServer()

            try:
                transport.start_server(server=server)
                chan = transport.accept(20)
                if chan is None:
                    print("[-] No channel.")
                    continue
                chan.send(b"Welcome to the test SSH server!\n")
                chan.close()
            except Exception as e:
                print(f"[-] SSH negotiation failed: {e}")
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_ssh_server()
