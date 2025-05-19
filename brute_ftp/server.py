from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

def start_server(host='0.0.0.0', port=21):
    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '123456', 'D:\\FTP') 

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((host, port), handler)

    server.serve_forever()

start_server()