import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        # list to add blocks to
        self.chain = []
        # list of transactions that have not been added to the chain in a block
        self.pending_transactions = []
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.prending_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        transactions = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transactions)
        return self.last_block['index'] - 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    def proof_of_work(self):
        previous_proof = self.last_block['proof']
        new_proof = 1
        check_proof = False
        while check_proof is False:
            proof_guess = hashlib.sha256(str(new_proof ** 2 - previous_proof **
                                            2).encode()).hexdigest()

            print(new_proof, 'matches!' if proof_guess[:4] == '0000' else 'does not match')
            if proof_guess[:4] == '0000':
               check_proof = True
            else:
                new_proof += 1

        return new_proof


def main():
    bc = Blockchain()
    t1 = bc.new_transaction('bob', 'alice', 10)
    t2 = bc.new_transaction('frank', 'mary', 20)
    bc.new_block(bc.proof_of_work())
    # print(bc.chain)
    # proof = bc.proof_of_work()
    # print(proof)

if __name__ == '__main__':
    main()
