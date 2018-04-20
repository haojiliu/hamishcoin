# Haoji Liu
"""Server doesn't need web API, change to grpc or zmq"""
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request

CONST_NEW_COIN_BONUS_SENDER = '0'


import blockchain as bc

from decimal import *
context = getcontext()

# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
nid = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = bc.Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
  # We run the proof of work algorithm to get the next proof...
  last_block = blockchain.last_block
  proof, last_hash = blockchain.proof_of_work(last_block)

  # We must receive a reward for finding the proof.
  # The sender is "0" to signify that this node has mined a new coin.
  amt_in_decimal = Decimal('1')
  blockchain.new_transaction(
    sender=CONST_NEW_COIN_BONUS_SENDER,
    recipient=nid,
    amount=amt_in_decimal,
  )

  # Forge the new Block by adding it to the chain
  block = blockchain.new_block(proof, last_hash)

  response = {
    'message': "New Block Forged",
    'index': block['index'],
    'transactions': block['transactions'],
    'proof': block['proof'],
    'previous_hash': block['previous_hash'],
  }
  return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  values = request.get_json()

  # Check that the required fields are in the POST'ed data
  required = ['sender', 'recipient', 'amount']
  if not all(k in values for k in required):
    return 'Missing values', 400

  # Create a new Transaction
  amt = str(values['amount'])
  amt_in_decimal = Decimal(amt)

  index = blockchain.new_transaction(values['sender'], values['recipient'], amt_in_decimal)

  response = {'message': f'Transaction will be added to Block {index}'}
  return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain),
  }
  return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
  """I assume this endpoint will be hit periodically
  to reflect the latest reality
  """
  values = request.get_json()

  nodes = values.get('nodes')
  if nodes is None:
    return "Error: Please supply a valid list of nodes", 400

  for node in nodes:
    blockchain.register_node(node)

  response = {
    'message': 'New nodes have been added',
    'total_nodes': list(blockchain.nodes),
  }
  return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
  """I assume this is hit periodically/everytime
  we add a new transaction/block to reflect the reality
  """
  replaced = blockchain.resolve_conflicts()

  if replaced:
    response = {
        'message': 'Our chain was replaced',
        'new_chain': blockchain.chain
    }
  else:
    response = {
        'message': 'Our chain is authoritative',
        'chain': blockchain.chain
    }

  return jsonify(response), 200

if __name__ == '__main__':
  from argparse import ArgumentParser

  parser = ArgumentParser()
  parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
  args = parser.parse_args()
  port = args.port

  app.run(host='0.0.0.0', port=port)
