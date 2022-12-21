class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self._head = None

    def push(self, data):
        if not self._head:
            self._head = Node(data, None)
        else:
            old_head = self._head
            self._head = Node(data, old_head)

    def pop(self):
        if not self._head:
            return None

        data = self._head.data
        self._head = self._head.next
        return data

    def count(self):
        num =0
        cur =self._head
        while cur:
            num += 1
            cur =cur.next
        return num

    def get(self,index):
        if index >= self.count():
            return None
        if index == 0:
            cur = self._head
        else:
            cur =self._head
            for i in range(index):
                cur =cur.next

        return cur.data

    def enqueue(self, data):
        if not self._head:
            self._head =Node(data,None)
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def dequeue(self):
        return self.pop()
