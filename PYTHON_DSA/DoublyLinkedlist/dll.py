class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self):
        nodeCount = int(input("Enter the node count: "))
        for i in range(nodeCount):
            newNode = Node(int(input("Enter the node value: ")))
            if self.head is None:
                self.head = newNode
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
            self.tail = newNode

    def addFront(self):
        newNode = Node(int(input("Enter the data: ")))
        if self.head is None:  # Empty list
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addLast(self):
        newNode = Node(int(input("Enter the data: ")))
        if self.tail is None:  # Empty list
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def addPosition(self):
        position = int(input("Enter the position: "))
        newNode = Node(int(input("Enter the data: ")))

        if position == 1:  # Insert at the beginning
            self.addFront()
            return

        temp = self.head
        current_position = 1

        # Traverse to the node just before the given position
        while temp and current_position < position - 1:
            temp = temp.next
            current_position += 1

        if not temp:  # If position is beyond the current list length
            print("Position out of bounds.")
            return

        if temp.next is None:  # Insert at the end
            self.addLast()
        else:
            # Insert between temp and temp.next
            nextNode = temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = nextNode
            nextNode.prev = newNode

    def removeFront(self):
        if self.head is None:  # Empty list
            print("List is empty, nothing to remove.")
            return

        if self.head == self.tail:  # Single element
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeLast(self):
        if self.tail is None:  # Empty list
            print("List is empty, nothing to remove.")
            return

        if self.head == self.tail:  # Single element
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def removePosition(self):
        position = int(input("Enter the position to remove: "))
        if self.head is None:  # Empty list
            print("List is empty, nothing to remove.")
            return

        if position == 1:  # Remove from the beginning
            self.removeFront()
            return

        temp = self.head
        current_position = 1

        # Traverse to the node at the given position
        while temp and current_position < position:
            temp = temp.next
            current_position += 1

        if not temp:  # If position is beyond the list length
            print("Position out of bounds.")
            return

        if temp == self.tail:  # Remove from the end
            self.removeLast()
        else:
            # Remove the node at the given position
            prevNode = temp.prev
            nextNode = temp.next
            prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverseDisplay(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")


# Example Usage:
dll = DLL()
dll.add()             # Add nodes
dll.addFront()        # Add a node to the front
dll.addLast()         # Add a node to the end
dll.addPosition()     # Add a node at a specific position
dll.display()         # Display the list
dll.removeFront()     # Remove a node from the front
dll.removeLast()      # Remove a node from the end
dll.removePosition()  # Remove a node from a specific position
dll.display()         # Display the list after removals
