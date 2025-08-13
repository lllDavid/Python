import time
import random
import math
from multiprocessing import Manager, Pool, Lock

def generate_data(n):
    return [random.randint(1, 100) for _ in range(n)]

def transform_stage_1(data, lock, result_list):
    try:
        transformed = [x * 2 for x in data]
        with lock:
            result_list.append(('Stage 1', transformed))
    except Exception as e:
        with lock:
            result_list.append(('Stage 1 Error', str(e)))
    time.sleep(random.uniform(0.1, 0.3))

def transform_stage_2(data, lock, result_list):
    try:
        transformed = [x ** 2 for x in data]
        with lock:
            result_list.append(('Stage 2', transformed))
    except Exception as e:
        with lock:
            result_list.append(('Stage 2 Error', str(e)))
    time.sleep(random.uniform(0.1, 0.3))

def error_handling_stage(data, lock, result_list):
    try:
        if random.random() < 0.2: 
            raise ValueError("Random error occurred during processing!")
        processed_data = [math.sqrt(x) for x in data if x > 0]
        with lock:
            result_list.append(('Error Handling Stage', processed_data))
    except Exception as e:
        with lock:
            result_list.append(('Error Handling Stage Error', str(e)))
    time.sleep(random.uniform(0.1, 0.3))

def data_writer(lock, result_list):
    try:
        with lock:
            for stage, result in result_list:
                print(f"{stage}: {result}")
        print("Data writer finished")
    except Exception as e:
        print(f"Error in data writer: {e}")

def process_data(data_chunk, lock, result_list):
    transform_stage_1(data_chunk, lock, result_list)
    transform_stage_2(data_chunk, lock, result_list)
    error_handling_stage(data_chunk, lock, result_list)

def main():
    data = generate_data(20)  
    chunk_size = len(data) // 4 

    manager = Manager()
    result_list = manager.list()
    lock = Lock()

    with Pool(processes=4) as pool:
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
        pool.starmap(process_data, [(chunk, lock, result_list) for chunk in chunks])

    data_writer(lock, result_list)

if __name__ == "__main__":
    main()