# Haoji Liu
"""Binary Merkle Tree implementation"""
import time

def crypto_hash(val):
  """One-way hash of a given tree node"""
  return None

class MerkleTree:
  def __init__(self):
    self.leaves = []
    # BFS traversal
    self.tree = []
    self.last_rebuild_epoch = time.time()
    # last time an update was made to the leaves
    self.last_update_epoch = self.last_rebuild_epoch

  def rebuild(self):
    """Rebuild the tree based on leaf node updates"""
    # TODO: rebuild
    self.last_rebuild_epoch = time.time()

  def add_leaf(self, block):
    digest = crypto_hash(block.to_bytes())
    self.leaves.append(digest)
    self.last_update_epoch = time.time()
    self.rebuild()

  def verify_leaf(self, idx):
    """Check if a data block is corrupted"""
    return True

  def find_leaf_by_idx(self, idx):
    return self.leaves[idx]

  @property
  def is_available(self):
    """Make sure a rebuild happened"""
    return self.last_rebuild_epoch > self.last_update_epoch
