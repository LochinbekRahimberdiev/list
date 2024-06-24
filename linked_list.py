class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# LinkedList obyektini yaratish
llist = LinkedList()

# .append() metodiga misollar
llist.append(6)
llist.append(7)
llist.append(8)
llist.append(9)
llist.append(10)

# .printList() metodiga misollar
llist.printList()

# .push() metodiga misollar
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

# .printList() metodiga misollar
llist.printList()

# .insert() metodiga misollar
llist.insert(llist.head.next, 15)
llist.insert(llist.head.next.next, 20)
llist.insert(llist.head.next.next.next, 25)
llist.insert(llist.head.next.next.next.next, 30)
llist.insert(llist.head.next.next.next.next.next, 35)

# .printList() metodiga misollar
llist.printList()
