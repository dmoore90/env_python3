class Node:
    def __init__(self, data=None, num=None):
        self.data = data
        self.next = None
        self.num = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = Node(data)

    def show(self):
        showlist = self.head
        while(showlist != None):
            print(showlist.data, " ")
            showlist = showlist.next

    def index(self, num):
        index = self.head
        length = 0
        n = num
        while(index != None):
            length += 1
            index = index.next
        index = self.head
        while(length != n):
            length -= 1
            index = index.next
        print(index.data)

l = LinkedList()
number = int(input())
values = input()
# number = 2
# values = "1 2 3 4 5 6 7 8 9 10"
if (number <= 0 or number >= (2**32 -1)):
    print("NIL")
    exit()
length = 0
values = map(int, values.split(" "))
for i in values:
    if (i < 0 or i >= (2**32 -1)):
        print("NIL")
        exit()
    l.append(i)
    length += 1
    if (length <= 0 or length >= 1024):
        print("NIL")
        exit()
if (number > length or number <= 0):
    print("NIL")
else:    
    l.index(number)