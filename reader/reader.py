# 数据读取基类

support_type = ['pdf','txt','csv','excel']

class Reader:
    def __init__(self,type:str):
        assert type in support_type
        self.type=type

    def read(self,file):
        pass

    def get_pages(self) -> int:
        pass