class Node:
    def __init__(self, val=0, Next=None):
        self.val = val
        self.next = Next
        
class MyCircularQueue:
    

    def __init__(self, k: int):
        self.front, self.rear = None, None
        self.len = 0
        self.maxlen = k

            

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.len == 0:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        self.len += 1
        return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        self.len -= 1
        
        return True
        
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.maxlen
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()