class SimpleAllocator:
    def __init__(self, size):
        self.memory = bytearray(size)
        self.free_blocks = [(0, size)]

    def malloc(self, size):
        for i, (start, end) in enumerate(self.free_blocks):
            if end - start >= size:
                self.free_blocks.pop(i)
                if end - (start + size) > 0:
                    self.free_blocks.append((start + size, end))
                return (start, start + size)
        return None

    def free(self, block):
        self.free_blocks.append(block)
        self.free_blocks.sort()

allocator = SimpleAllocator(1024)
block1 = allocator.malloc(256)
block2 = allocator.malloc(128)
allocator.free(block1)
block3 = allocator.malloc(64)
