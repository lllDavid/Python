import asyncio

clients = []

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"New connection from {addr}")
    
    clients.append(writer)

    try:
        while True:
            data = await reader.read(100)
            message = data.decode()
            if not data:
                break

            print(f"Received {message} from {addr}")

            for client in clients:
                if client != writer:
                    client.write(data)
                    await client.drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Closing connection to {addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)
    
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
