# Haoji Liu
class Block:
  def __init__(self, index, current_transactions, proof, previous_hash):
    self.index = index
    self.timestamp = time(),
    self.transactions = current_transactions # pass by reference is the key here!!!
    self.proof = proof
    self.previous_hash = previous_hash

  def to_bytes(self):
    return b'hello world'
