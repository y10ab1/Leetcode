class Node:
    def __init__(self,val = 0, Next = None):
        self.val = val
        self.next = Next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        cur = self.head
        if index < self.size:
            for i in range(index):
                cur = cur.next
            return cur.val
        else:
            return -1
        
    def getnode(self, index: int) -> int:
        cur = self.head
        if index < self.size:
            for i in range(index):
                cur = cur.next
            return cur
        else:
            return None
            
        
        

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        if self.head:
            newnode.next = self.head
        self.head = newnode
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        tmp = self.head
        if tmp:
            while tmp:
                if tmp.next:
                    tmp = tmp.next
                else:
                    tmp.next = newnode
                    break
        else:
            self.head = newnode
            
        self.size += 1
    
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            inode = self.getnode(index-1)
            newnode = Node(val, inode.next)
            inode.next = newnode
            self.size += 1
        
        
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            inode = self.getnode(index-1)
            inode.next = inode.next.next
            self.size -= 1
        



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)