# Description:
    This code implement a simulate of the bitcoin miner by using the logic below.


# Miner will do: 
    step 1 - getting the block header.
    step 2 - changing the nonce.
    step 3 - checking if the block header hash is less than the target.  
    step 4 - jumping to step 1 if someone else win the block otherwise jump to step 2.


# IMPORTANT: 
   * This miner will run slower than a real time miner because it's implement with python, which is not 
     recommended for such a things.
   * In this code the difficulty raise by 1 after each block, In reality it's not the case.


# Code samples: 

                                  | Block#0 | Block#1 | Block#2 |  
  Block size of 1MB fully covered:    312      2995      81301               ------
  Block size of 2MB fully covered:    277      1506      67025                     |
  Block size of 4MB fully covered:    346      253       118840                    | 
  Block size of 8MB fully covered:    524      1192      29643                     |     Notice the diff
                                                                                   |==>  gap between each
                                         | Block#0 | Block#1 | Block#2 |           |     of the blocks.
  Block size of 1MB with the same offset:    312      2859      87507              |
  Block size of 2MB with the same offset:    277      3542      12897              |
  Block size of 4MB with the same offset:    346      9088      102358             |
  Block size of 8MB with the same offset:    524      2715      294406       ------     


# Additional information: 
   * The difficulty level of the bitcoin is 24 as for today, 9/1/2022.
   * The nonce size of the bitcoin is 32Bits or 4Bytes.
   * The bitcoin block size is 1MB.
   * The expected block time of each bitcoin block is at around 10 minutes.
   * The bitcoin highest peak is at 64,800$ as for today, 9/1/2022.


# References:
 - https://en.bitcoin.it/wiki/Nonce
 - https://en.bitcoin.it/wiki/Target
 - https://en.bitcoin.it/wiki/Block_hashing_algorithm
 - https://en.bitcoin.it/wiki/Difficulty
 - http://www.righto.com/2014/02/bitcoin-mining-hard-way-algorithms.html
