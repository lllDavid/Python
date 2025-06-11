import hashlib
import time
import random
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash, validator):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}{self.validator}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.stakes = {}  
        self.validators = []  
        self.min_stake = 10

    def create_genesis_block(self):
        return Block(0, time.time(), {"amount": 0}, "0", "genesis")

    def add_stake(self, address, amount):
        if amount >= self.min_stake:
            self.stakes[address] = self.stakes.get(address, 0) + amount
            if address not in self.validators:
                self.validators.append(address)
        else:
            print(f"Minimum stake is {self.min_stake} tokens.")

    def select_validator(self):
        if not self.validators:
            return None
        total_stake = sum(self.stakes[addr] for addr in self.validators)
        if total_stake == 0:
            return None
        weights = [self.stakes[addr] / total_stake for addr in self.validators]
        return random.choices(self.validators, weights=weights, k=1)[0]

    def add_block(self, data):
        validator = self.select_validator()
        if not validator:
            print("No validators available.")
            return
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), data, previous_block.hash, validator)
        self.chain.append(new_block)
        print(f"Block #{new_block.index} added by validator: {validator}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                print(f"Invalid hash at block {i}")
                return False
            if current.previous_hash != previous.hash:
                print(f"Invalid previous hash at block {i}")
                return False
            if current.validator not in self.validators:
                print(f"Invalid validator at block {i}")
                return False
        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_stake("Alice", 50)
    blockchain.add_stake("Bob", 30)
    blockchain.add_stake("Charlie", 20)

    print("Adding block 1.")
    blockchain.add_block({"amount": 4})
    print("Adding block 2.")
    blockchain.add_block({"amount": 10})

    for block in blockchain.chain:
        print(f"Block #{block.index}: Hash={block.hash}, Validator={block.validator}")
