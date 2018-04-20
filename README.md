# Ottercoin

## Questions from Haoji

* how often should resolve_conflicts endpoint be hit?
* using decimal vs float?


## Design choices by Haoji

* using mongodb to store transactions, each current transaction list will be one collection, currently using list, but list lives on memory and is prone to data loss
* using a linked list instead of list, we shouldn't allow moving backwards, a node should only contain information about it's next node


### Schema Design

* Users - store the user info, operations like getting a given user's public key, or search for user by email or phone number
* Wallet - each wallet will be associated with at most one user
* Transaction/Block - should be flushed to db instead of staying on memory for persistency???


## Haoji's version on how it can work in terms of baby food transaction:
* wtf???


## Dev guide
* `docker-compose build app`
* `docker-compose up -d app`
* go to 'localhost:5000/mine' to mine a new block

# References

https://hackernoon.com/blockchain-101-only-if-you-know-nothing-b883902c59f7

https://en.bitcoin.it/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Merkle_tree
