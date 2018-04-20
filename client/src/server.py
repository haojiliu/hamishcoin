# Haoji Liu
"""Client facing operations, something like:
0. client sign up
1. client sign in
2. client send money
3. client receive money
4. client check balance
5. client edit personal info
"""

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

@app.route('/user/<uid>', methods=['GET'])
def one_user(uid):
  pass

if __name__ == '__main__':
  from argparse import ArgumentParser

  parser = ArgumentParser()
  parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
  args = parser.parse_args()
  port = args.port

  app.run(host='0.0.0.0', port=port)
