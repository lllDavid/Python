import time
import cProfile

def compute():
    total = 0
    for i in range(1000000):
        total += i
    return total

cProfile.run('compute()')



def load_data():
    time.sleep(0.5)  
    return list(range(10000))

def process_data(data):
    return [x ** 2 for x in data]

def slow_operation(data):
    total = 0
    for i in data:
        for _ in range(10):  
            total += i % 5
    return total

def save_results(result):
    time.sleep(0.2)  
    return True

def main():
    data = load_data()
    processed = process_data(data)
    result = slow_operation(processed)
    save_results(result)

if __name__ == "__main__":
    cProfile.run("main()")