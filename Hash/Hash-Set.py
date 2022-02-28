class MyHashSet:

    def __init__(self):
        self.space = 409
        self.v = [[] for _ in range(self.space)]
    
    def hash(self, key):
        return key % self.space
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            idx = self.hash(key)
            lis = self.v[idx]
            lis.append(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        lis = self.v[idx]
        if len(lis)>0:
            for i in range(len(lis)):
                if lis[i]==key:
                    del lis[i]
                    return
        
    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        lis = self.v[idx]
        if len(lis)>0:
            for i in range(len(lis)):
                if lis[i]==key:
                    return True
        return False
