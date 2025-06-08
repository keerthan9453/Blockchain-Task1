import time
from src.Block_create import Block


difficulty = 4

block_to_mine = Block(1, "0", "Testing Nonce Mining")

print("🔨 Starting mining process...")
start_time = time.time()

block_to_mine.mine_block(difficulty)

end_time = time.time()
time_taken = end_time - start_time

print("\n Block successfully mined!")
print(f"Hash: {block_to_mine.hash}")
print(f"Nonce: {block_to_mine.nonce}")
print(f"Time Taken: {time_taken:.2f} seconds")
