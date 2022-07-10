import hashlib
import json
from time import time
from pprint import pprint

class Block:
    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def __str__(self):
        return str(self.__dict__)

    def hash(self):
        # stringify self as ordered json
        string_object = json.dumps(self.__dict__, sort_keys=True)
        block_string = string_object.encode()

        # hash json
        raw_hash = hashlib.sha256(block_string)
        digest = raw_hash.hexdigest()

        return digest

class Transaction:
    pass

class Blockchain:
    def __init__(self):
        # list to add blocks to
        self.chain = []
        # list of transactions that have not been added to the chain in a block
        self.pending_transactions = []
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    def __str__(self):
        return str(self.chain)

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash_algorithm(prev_proof, new_proof):
        return hashlib.sha256(str(new_proof ** 2 - prev_proof ** 2).encode()).hexdigest()

    def new_block(self, proof, previous_hash=None):
        block = Block(len(self.chain) + 1, time(), self.pending_transactions,
                          proof, previous_hash or self.last_block.hash())
        # block = {
        #     'index': len(self.chain) + 1,
        #     'timestamp': time(),
        #     'transactions': self.pending_transactions,
        #     'proof': proof,
        #     'previous_hash': previous_hash or self.hash(self.last_block)
        # }

        self.pending_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        transactions = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transactions)
        return self.last_block.index - 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    def proof_of_work(self, verbose=False):
        previous_proof = self.last_block.proof
        new_proof = 1
        check_proof = False
        while check_proof is False:
            proof_guess = Blockchain.hash_algorithm(previous_proof, new_proof)
            if verbose:
                print(new_proof, 'matches!' if proof_guess[:4] == '0000' else 'does not match')
            if proof_guess[:4] == '0000':
               check_proof = True
            else:
                new_proof += 1

        return new_proof

    def validate_chain(self):
        # loop over entire chain
        i = 0
        while i <= len(self.chain) - 2:
            # comparing the blocks in groups of two
            prev_block = self.chain[i]
            next_block = self.chain[i + 1]
            print(i, len(self.chain))
            # if the hashes don't line up, there is a mismatch
            if next_block.previous_hash != prev_block.hash():
                return False

            # check that the hashes match the algorithm
            hash_check = Blockchain.hash_algorithm(prev_block.proof,
                                                   next_block.proof)
            # the hash needs to start with four zeros to be valid
            if hash_check[:4] != '0000':
                return False

            i += 1

        # if we make it here, all hashes have checked
        return True

def main():
    bc = Blockchain()
    t1 = bc.new_transaction('bob', 'alice', 10)
    t2 = bc.new_transaction('frank', 'mary', 20)
    bc.new_block(bc.proof_of_work(verbose=True))
    t3 = bc.new_transaction('spam', 'eggs', 30)
    t4 = bc.new_transaction('bacon', 'sausage', 15)
    bc.new_block(bc.proof_of_work())
    t5 = bc.new_transaction('eggs', 'spam', 7)
    t6 = bc.new_transaction('bacon', 'sausage', 15)
    pprint(bc.chain)
    print(bc.validate_chain())
    # print(bc.chain)
    # proof = bc.proof_of_work()
    # print(proof)

if __name__ == '__main__':
    main()
