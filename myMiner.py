'''
# AUTHOR: Shenhav_Hezi.
# ID: 313594764.

'''

import hashlib
import time
from time import sleep 


# return encrypted string by using SHA256, Secure Hash Algorithem.
def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()



# Class for the block chain which has all the blocks that's been added.
class BlockChain:
    
    # initialize block chain.
    def __init__(self):
        self.block_chain = []
          
    # get the last block from the block chain.
    def get_last_block(self):
        return self.block_chain[-1]
        
    # push the current block to the block chain.
    def push(self, block):
        self.block_chain.append(block)
        
    # notify that a new block have been added.
    def notify_everybody(self): 
        print('-' * 120)
        print('ATTENTION EVERYONE, THIS BLOCK HAS BEEN ADDED:')
        print('BLOCK #{} : {}'.format(len(self.block_chain), self.get_last_block()))
        print('-' * 120)

    # this function verify the validity of the chain.
    def chain_validation():
        # not implemented for this project.
        return True
        


# Class for the transaction which has all the information needed.
class TransactionGenerator:
   
    # initialize transcation.
    def __init__(self):
        self.random_seed = 0

    # generate transaction using secure hash algorithem.
    def generate_transaction(self):
        transaction_rand = 'Simulate transaction between 2 persons' \
                           'random seed for uniqueness {} '.format(self.random_seed)
        transaction_hash = hash_256(transaction_rand)
        self.random_seed += 1
        return transaction_hash
    
  
    
# Class for the block which contains set of transcation, connected to previous blocks.
class Block:
    
    # # initialize block.   
    def __init__(self, hash_prev_block, target):
        self.transactions = []
        self.hash_prev_block = hash_prev_block  
        self.hash_merkle_block = None
        self.target = target
        self.nounce = 0
        self.total_time = 0.00
        
    # limited the block size to 1MB, likewise bitcoin block size.
    def full_block(self):
        return len(self.transactions) >= 1000
    
    # return if there is a block.
    def can_mine(self):
        self.total_time = time.time()
        return self.full_block()
       
    # adding transaction to the block if it has space, otherwise it's closed already.       
    def add_transaction(self, new_transac):
        if not self.full_block():
            self.transactions.append(new_transac)
            self.hash_merkle_block = hash_256(str('-'.join(self.transactions)))

    # convert block to string format.
    def __str__(self):
        return '-'.join([self.hash_merkle_block, str(self.nounce)])

    # mining to the point the block is fully and closed.
    def apply_mining_step(self):
        current_block = hash_256(self.__str__())
        print('CURRENT_BLOCK_HASH = {}, TARGET = {}'.format(current_block, self.target))
        if int(current_block, 16) < int(self.target, 16):
            # the one who's closed the block rewarded with some BTCs.
            print('Block was successfully mined! Your rewarded with 6.25 BTC!') 
            print('It took {} steps to mine it.'.format(self.nounce))
            self.total_time = round(time.time() - self.total_time, 2)
            return True
        else:
            # increasing the nounce, to change current_block so it will be below the target.
            self.nounce += 1
        return False



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def my_Miner():
    
    block_header = '0e0fc2132e9bd4b03c8b6371bfe6ab7df812b992d4a02885783a066ad92940a3'
    block_target = '00dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    # initialize the blocks.
    block_chain = BlockChain()
    
    # initialize transaction.
    transaction_generator = TransactionGenerator()

    # setting all the transactions into the new block, 80 transactions will have to wait.
    block = Block(block_header, block_target)
    for i in range(1080):
        block.add_transaction(transaction_generator.generate_transaction())

    assert block.full_block()
    assert block.can_mine()

    # block is full meaning it's time to mine it.
    while not block.apply_mining_step():
        continue
    
    # pushing the full block.
    block_chain.push(block)
    
    # wake up, can work on a new block! 
    block_chain.notify_everybody()
    
    # might take some time.
    sleep(3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ First Block Finish ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    # adding another zero just to demonstrate the difference.
    block_target = '000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
    
    # connect the fully block with the block chains, the header.
    block_header = hash_256(str(block_chain.get_last_block()))
    
    # setting all the transactions into the new block, 500 transactions will have to wait.
    block_2 = Block(block_header, block_target)
    for i in range(1500):
        block_2.add_transaction(transaction_generator.generate_transaction())

    assert block_2.full_block()
    assert block_2.can_mine()

    # block is full meaning it's time to mine it.
    while not block_2.apply_mining_step():
        continue
    
    # pushing the full block.
    block_chain.push(block_2)
    
    # wake up, can work on a new block!
    block_chain.notify_everybody()
    
    # might take some time.
    sleep(3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Second Block Finish ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    # adding another zero just to demonstrate the difference.
    block_target = '0000dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    # connect the fully block with the block chains, the header.
    block_header = hash_256(str(block_chain.get_last_block()))

    block_3 = Block(block_header, block_target)

    # setting all the transactions into the new block, 700 transactions will have to wait.
    for i in range(1700):
        block_3.add_transaction(transaction_generator.generate_transaction())

    assert block_3.full_block()
    assert block_3.can_mine()

    # now that our block is full, we can start to mine it.
    while not block_3.apply_mining_step():
        continue

    # pushing the full block.
    block_chain.push(block_3)
    
    # wake up, can work on a new block!
    block_chain.notify_everybody()
   
   # might take some time.
    sleep(3)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Third Block Finish ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
 # NOTICE: this might take some time, toggle off/on if needed.
 
    '''
    
    # adding another zero just to demonstrate the difference.
    block_target = '00000ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'

    # connect the fully block with the block chains, the header.
    block_header = hash_256(str(block_chain.get_last_block()))

    block_4 = Block(block_header, block_target)

    # setting all the transactions into the new block, 170 transactions will have to wait.
    for i in range(2170):
        block_4.add_transaction(transaction_generator.generate_transaction())

    assert block_4.full_block()
    assert block_4.can_mine()

    # now that our block is full, we can start to mine it.
    while not block_4.apply_mining_step():
        continue

    # pushing the full block.
    block_chain.push(block_4)
    
    # wake up, can work on a new block!
    block_chain.notify_everybody()
   
   # might take some time.
    sleep(3)                                    
     
    '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Fourth Block Finish ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    
    print('All of the transactions have been completed.')
    print('')
    print('relevant information:')
    print('')
    
    # relevance information for each block, after each block difficulty level increased.
    overall_mining_time = 0.00
    for i, block_added in enumerate(block_chain.block_chain):
        if i==len(block_chain.block_chain)-1:
            print('Block #{} added, The number of steps to find it out {}.'.format(i, block_added.nounce))
            print('The mining time took: {} seconds.'.format(str(block_added.total_time))) 
            overall_mining_time += block_added.total_time   
            print('')
        else:
               print('Block #{} added, The number of steps to find it out {}.'.format(i, block_added.nounce))
               print('The mining time took: {} seconds.'.format(str(block_added.total_time)))
               overall_mining_time += block_added.total_time
               print('Difficulty increased!!!')
               print('')
               
    print('Total time for mining all the blocks: {} seconds.'.format(str(round(overall_mining_time, 2))))

if __name__ == '__main__':
    prog_time = time.time()
    my_Miner()
    total_prog_time = str(round(time.time() - prog_time, 2))
    print('Total program running time: {} seconds.'.format(total_prog_time))


