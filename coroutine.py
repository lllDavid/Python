import asyncio

async def data_processor(queue):
    """Coroutine that continuously processes data from a queue."""
    print("Coroutine started. Ready to process data.")
    while True:
        data = await queue.get()  
        if data is None:  
            break
        print(f"Processing: {data}")
        await asyncio.sleep(1)  
    print("Coroutine closed.")

async def main():
    queue = asyncio.Queue()

    processor_task = asyncio.create_task(data_processor(queue))

    await queue.put("Task 1")
    await queue.put("Task 2")
    await queue.put("Task 3")

    await asyncio.sleep(0.5)  

    await queue.put(None)

    await processor_task

asyncio.run(main())
