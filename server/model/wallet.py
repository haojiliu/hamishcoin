# Haoji Liu
"""Wallet"""
import uuid

class Wallet:
  def __init__(self, uid):
    self.id = uuid.uuid1()
    self.uid = uid
