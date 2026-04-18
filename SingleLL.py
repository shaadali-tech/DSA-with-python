class Node:
    def __init__(self, data):
        self.data = data   # value
        self.next = None   # pointer


# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link nodes
n1.next = n2
n2.next = n3

# Print linked list
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next