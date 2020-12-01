class Queue :
    def __init__(self):
        self._list = []
    
    def empty(self):
        return True if len(self._list) == 0 else False
    
    def get(self):
        if len(self._list) == 0:
            return 0
        else :
            return self._list.pop(-1)
    
    def put(self, value):
        return self._list.insert(0,value)
    
    def getQueue(self):
        return self._list.copy()

q1 = Queue()
q1.empty()
q1.get()
q1.put(1)
q1.put(2)
print(q1.getQueue())

q1.get()
print(q1.getQueue())
q1.get()
print(q1.getQueue())

