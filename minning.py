import time
from src.Block_create import Block

# Set mining difficulty (e.g., number of leading zeroes in hash)
difficulty = 4  # Try 3 or 5 for faster/slower mining

# Create a new block manually
block_to_mine = Block(1, "0", "Testing Nonce Mining")

print("🔨 Starting mining process...")
start_time = time.time()

# Mine the block (find nonce)
block_to_mine.mine_block(difficulty)

end_time = time.time()
time_taken = end_time - start_time

# Output mining results
print("\n✅ Block successfully mined!")
print(f"Hash: {block_to_mine.hash}")
print(f"Nonce: {block_to_mine.nonce}")
print(f"Time Taken: {time_taken:.2f} seconds")
