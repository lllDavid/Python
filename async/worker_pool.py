import asyncio
import random
import time

async def process_job(job_id: int) -> str:
    await asyncio.sleep(random.uniform(0.5, 2))
    return f"Job {job_id} completed"

async def worker(worker_id: int, queue: asyncio.Queue):
    while True:
        try:
            job_id = await asyncio.wait_for(queue.get(), timeout=5.0)
            result = await process_job(job_id)
            print(f"Worker {worker_id}: {result}")
            queue.task_done()
        except asyncio.TimeoutError:
            print(f"Worker {worker_id}: No more jobs, exiting")
            break
        except Exception as e:
            print(f"Worker {worker_id}: Error - {str(e)}")

async def main():
    job_queue = asyncio.Queue()
    for i in range(10):
        await job_queue.put(i)

    num_workers = 3
    start_time = time.time()
    
    workers = [worker(i, job_queue) for i in range(num_workers)]
    await asyncio.gather(*workers)
    
    print(f"All jobs processed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())