import hashlib
import datetime

class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

    def hash_black(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        # 返回加密后的字符串
        return sha.hexdigest()

    @classmethod
    def create_genesis_block(cls):
        return cls(0, datetime.datetime.now(), 'Geneis Block', '0')

    def next_block(self, last_block):
        self.index += 1
        self.timestamp = datetime.datetime.now()
        self.data = 'hello 我是区块链' + str(self.index)
        self.hash = hash
        return Block(self.index, self.timestamp, self.data, self.hash)

#创建区块链\
obj = Block.create_genesis_block()
block = [obj.hash_black()]
previous_block = block[0]
# 限定有多少链
num_of_chain = 2
for i in range(0, num_of_chain):
    block_to_add = obj.next_block(previous_block).hash_black()
    block.append(block_to_add)
    previous_block = block_to_add
    print('上链成功')