import asyncio
import websockets

class WebSocketPool:
    def __init__(self, max_size):
        self._max_size = max_size
        self._available = asyncio.Queue(max_size)
        self._in_use = set()
        self._lock = asyncio.Lock()

    async def acquire(self, uri, timeout=None):
        async with self._lock:
            while not self._available.empty():
                ws = await self._available.get()
                if ws.closed:
                    continue
                self._in_use.add(ws)
                return ws

            if len(self._in_use) < self._max_size:
                ws = await websockets.connect(uri)
                self._in_use.add(ws)
                return ws

        try:
            ws = await asyncio.wait_for(self._available.get(), timeout=timeout)
            if ws.closed:
                return await self.acquire(uri, timeout=timeout)
            async with self._lock:
                self._in_use.add(ws)
            return ws
        except asyncio.TimeoutError:
            raise RuntimeError("Timeout waiting for WebSocket connection from pool")

    async def release(self, ws):
        async with self._lock:
            if ws not in self._in_use:
                return
            self._in_use.remove(ws)
            if not ws.closed:
                await self._available.put(ws)

    async def close_all(self):
        async with self._lock:
            while not self._available.empty():
                ws = await self._available.get()
                await ws.close()
            await asyncio.gather(*(ws.close() for ws in self._in_use))
            self._in_use.clear()