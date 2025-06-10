import random
from collections import Counter

print(" Consensus Mechanism Simulation\n")

# PoW - Proof of Work: 3 Miners
pow_validators = {
    "Miner A": random.randint(100, 500),
    "Miner B": random.randint(100, 500),
    "Miner C": random.randint(100, 500),
}

pow_winner = max(pow_validators, key=pow_validators.get)

print("⛏️ [PoW] Proof of Work:")
print(f"Miners' power: {pow_validators}")
print(
    f"Selected Miner: {pow_winner} (power = {pow_validators[pow_winner]} GH/s)\n")
print("✔️ PoW chooses the miner who can do the most work (highest hash power).\n")

# PoS - Proof of Stake
pos_validators = {
    "Validator X": random.randint(1000, 10000),
    "Validator Y": random.randint(1000, 10000),
    "Validator Z": random.randint(1000, 10000),
}

# Select the validator with the highest stake
pos_winner = max(pos_validators, key=pos_validators.get)

print("💰 [PoS] Proof of Stake:")
print(f"Stakers' stake: {pos_validators}")
print(
    f"Selected Validator: {pos_winner} (stake = {pos_validators[pos_winner]} coins)\n")
print("✔️ PoS chooses the validator who has the most coins at stake.\n")


delegates = ["Alice", "Bob", "Charlie"]
votes = [random.choice(delegates) for _ in range(5)]
# It simulates 5 votes cast by users for the delegates
vote_count = Counter(votes)


dpos_winner = vote_count.most_common(1)[0][0]

print(" [DPoS] Delegated Proof of Stake:")
print(f"Delegates: {delegates}")
print(f"Votes Cast: {votes}")
print(f"Vote Tally: {dict(vote_count)}")
print(f"Selected Delegate: {dpos_winner}\n")
print("✔️ DPoS selects a trusted delegate based on votes from other users.\n")
