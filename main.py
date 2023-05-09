# consists of blocks
# blocks consist transaction
# blocks are connected through hashing
# unique digital fingerprint - transaction + previous blocks hash

from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Matic",
                                                     "Satoshi sent 5 BTC to Hal Finney"])

second_block = Block(genesis_block.block_hash, ["Matic sent 1 BTC to Satoshi",
                                                "Satoshi sent 1 BTC to Hal Finney"])

third_block = Block(second_block.block_hash, ["A sent 1 BTC to B",
                                                "B sent 1 BTC to C"])

print("")
print("Block hash: Genesis Block")
print(genesis_block.block_hash)
print("")
print("Block hash: Second Block")
print(second_block.block_hash)
print("")
print("Block hash: Third Block")
print(third_block.block_hash)

