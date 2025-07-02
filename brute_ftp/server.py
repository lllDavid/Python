import threading
import time
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

def start_server(host='0.0.0.0', port=21):
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '123456', 'D:\\FTP', perm='elradfmwMT')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((host, port), handler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print(f"FTP Server started on {host}:{port}. Press Ctrl+C to stop.")

    try:
        while server_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down FTP server...")
        server.close_all()

start_server()