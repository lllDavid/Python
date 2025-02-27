import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

def data_source(output_queue):
    for i in range(10):
        data = f"data_{i}"
        output_queue.put(data)
        time.sleep(random.uniform(0.1, 0.5))
    output_queue.put(None)

def process_stage_1(input_queue, stage_1_queue):
    while True:
        data = input_queue.get()
        if data is None:
            break
        processed_data = f"stage_1_{data}"
        stage_1_queue.put(processed_data)
    stage_1_queue.put(None)

def process_stage_2(input_queue, stage_2_queue):
    while True:
        data = input_queue.get()
        if data is None:
            break
        processed_data = f"stage_2_{data}"
        stage_2_queue.put(processed_data)
    stage_2_queue.put(None)

def data_writer(input_queue):
    while True:
        data = input_queue.get()
        if data is None:
            break
        print(f"Data writer wrote: {data}")
    print("Data writer finished")

def main():
    source_queue = Queue()
    stage_1_queue = Queue()
    stage_2_queue = Queue()

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(data_source, source_queue)
        executor.submit(process_stage_1, source_queue, stage_1_queue)
        executor.submit(process_stage_2, stage_1_queue, stage_2_queue)
        executor.submit(data_writer, stage_2_queue)

if __name__ == "__main__":
    main()
