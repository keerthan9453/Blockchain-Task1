from src.Block_create import Blockchain, Block

my_blockchain = Blockchain()

print("📜 Initial Blockchain:")
my_blockchain.add_block(Block(1, my_blockchain.chain[-1].hash, "Second Block"))
my_blockchain.add_block(Block(2, my_blockchain.chain[-1].hash, "Third Block"))


print("\n🔧 Tampering Block 1...")
my_blockchain.chain[1].data = "Tampered Block"
my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

my_blockchain.print_chain()
