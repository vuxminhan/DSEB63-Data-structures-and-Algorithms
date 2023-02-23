import queue
class Queue:
    def __init__(self):
        self._data = []
        self._len = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        return f"{self._data}"

    def is_empty(self):
        if len(self) == 0:
            print(f"len: {len(self)}")
            return True
        print(f"len: {len(self)}")
        return False

    def enqueue(self, num):
        self._data.append(num)
        self._len += 1

    def dequeue(self):
        if self.is_empty():
            raise queue.Empty("Empty stack")
        else:
            self._len -= 1
            return self._data.pop(0)

class Stream:
    def __init__(self, k):
        self._data = []
        self.s = 0
        self.k = k

    def forward(self, e):

        if len(self._data) < 3:
            self._data.append(e)
            self.s += e
        else:
            self._data.append(e)
            self.s += e
            self.s -= self._data.pop(0)
        return float(self.s) / float(len(self._data))

# s = Stream(3)
# print(s.forward(3))
# print(s.forward(2))
# print(s.forward(1))
# print(s.forward(5))
# print(s.forward(7))
# print(s.forward(3))

#list
class Stream1:
    def __init__(self, k):
        self.data = []
        self.k = k

    def forward(self, e):
        # if len(self._data) < self.k:
        self.data.append(e)
        s = 0
        for i in range(len(self.data)-self.k-1,len(self.data)):
            s += self.data[i]
        # else:
        #     self._data.append(e)
        #     self.s += e
        #     self.s -= self._data.pop(0)
        return float(s) / float(len(self.data))

s = Stream1(3)
print(s.forward(3))
print(s.forward(2))
print(s.forward(1))
print(s.forward(5))
print(s.forward(7))
print(s.forward(3))