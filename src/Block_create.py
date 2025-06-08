
import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.index = len(self.chain)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index} {{")
            print(f" Timestamp: {time.ctime(block.timestamp)}")
            print(f" Data: {block.data}")
            print(f" Previous Hash: {block.previous_hash}")
            print(f" Hash: {block.hash}")
            print(f" Nonce: {block.nonce}")
            print("}")
