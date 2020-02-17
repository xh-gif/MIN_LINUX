from sys import getsizeof


class SuperBlock(object):
    def __init__(self,
                 file_system_size=1024 * 1024 * 1024,#文件系统大小
                 block_index_size=4,
                 bit=64, #系统位数
                 inode_size=128, #大小
                 inode_density=2048, #密度
                 data_block_size=8 * 1024,#数据块大小
                 data_block_num=120000,
                 ):

        self.bit = bit
        self.file_system_size = file_system_size
        self.block_index_size = block_index_size
        self.inode_size = inode_size
        self.inode_num = int(self.file_system_size / inode_density) #大小除密度就是inode的数量
        self.data_block_size = data_block_size
        self.data_block_num = data_block_num
        self.__address_size = 4
        self.inodes = []
        for i in range(inode_density*inode_size):
            self.inodes.append(0)
        # Block(data_block_num, data_block_size)
        Inode_Block(data_block_num,data_block_size)

# class Block(object):
    # def __init__(self, num, size):


class Inode_Block(object):
    def __init__(self,num,block_size):
        # self.file_size = 0
        # self.block_num = 0
        self.block_size = block_size
        self.block_index = [] #inode

        self.num = num
        self.blocks = []
        for i in range(num):
            self.blocks.append([])

    def set_size(self, size):
        self.file_size = size

    def set_data(self, data):
        size = len(data)
        a = []

        count = int(size / self.block_size)+ 1
        for i in range(count):
            if self.block_index[i] == []:
                self.blocks = data[8192*i:8192*(i*1)]
                a.append(i)
        # self.block_index.append(a)
        return a

    def get_inode_index(self, data):
        a = self.set_data(data)
        self.block_index.append(a)
        return len(self.block_index)