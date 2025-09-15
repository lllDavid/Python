import socket

def parse_request(request_text):
    lines = request_text.split("\r\n")
    method, path, version = lines[0].split()
    headers = dict(line.split(":", 1) for line in lines[1:] if line)
    body_index = lines.index('') + 1 if '' in lines else len(lines)
    body = "\r\n".join(lines[body_index:])
    return {"method": method, "path": path, "version": version, "headers": headers, "body": body}

host, port = "localhost", 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection accepted from {addr}")
            data = conn.recv(4096).decode('utf-8')
            if not data:
                continue

            try:
                request = parse_request(data)
                print("Parsed HTTP request:", request)
            except Exception:
                conn.sendall(b"HTTP/1.1 400 Bad Request\r\n\r\n")