import  linked_list as ll

llist =ll.LinkedList()
llist.enqueue('A')
llist.enqueue('B')
llist.enqueue('C')

for i in range(llist.count()):
    print(llist.get(i))

print(llist.dequeue())
print(llist.dequeue())
print(llist.dequeue())
print(llist.dequeue())
