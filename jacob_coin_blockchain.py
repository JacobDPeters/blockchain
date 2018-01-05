import json
import hashlib
from datetime import datetime



class block:
	def __init__(self, index, time_stamp, data, previous_hash = ' '):
		self.index = index
		self.time_stamp = time_stamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calculate_hash_value()

	def calculate_hash_value(self):
		return hashlib.sha256((str(self.index) + self.previous_hash + self.time_stamp + json.dumps(self.data)).encode('utf-8')).hexdigest()




class blockchain:

    def __init__(self):
        self.chain = [self.create_initial_block()]

    def create_initial_block(self):
    	return block(0, str(datetime.now()), "Initial Block", "0")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]


    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash_value()
        self.chain.append(new_block)


    def see_block_chain(self):
    	for i in range(1, len(self.chain)):
    		print("Block " + str(self.chain[i].index) + " to wallet " + str(self.chain[i].data["wallet_id"]) + " at hash " + str(self.chain[i].hash))
    		print("Previous Hash on chain is " + str(self.chain[i].previous_hash))



def main():
		jacob_coin = blockchain()
		jacob_coin.add_block(block(1, str(datetime.now()), {"wallet_id": "X3YYKLJ%1U8@","amt": .55,"transaction_type": "bid"}))
		jacob_coin.add_block(block(2, str(datetime.now()), {"wallet_id": "JR43^9(FTR","amt": .55,"transaction_type": "ask"}))
		jacob_coin.see_block_chain()

if __name__ == "__main__":
		main()
