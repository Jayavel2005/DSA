class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add(self):
        nodeCount = int(input("Enter the node count: "))
        for i in range(nodeCount):
            newNode = Node(int(input("Enter the data: ")))
            if self.head is None:
                self.head = newNode
                temp = newNode
            else:
                temp.next = newNode
                temp = newNode

    def addFront(self):
        newNode = Node(int(input("Enter the data: ")))
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def addLast(self):
        newNode = Node(int(input("Enter the data: ")))
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode

    def addPosition(self):
        position = int(input("Enter the position: "))
        newNode = Node(int(input("Enter the data: ")))
        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        for i in range(position - 1):
            if temp is None:  # If position is out of bounds
                print("Position out of bounds!")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds!")
            return
        newNode.next = temp.next
        temp.next = newNode

    def removeFront(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        self.head = self.head.next

    def removeLast(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.next is None:  # If only one node exists
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def removePosition(self):
        position = int(input("Enter the position: "))
        if self.head is None:
            print("Linked list is empty.")
            return
        if position == 0:
            self.head = self.head.next
            return
        prev = None
        temp = self.head
        for i in range(position):
            if temp is None:  # If position is out of bounds
                print("Position out of bounds!")
                return
            prev = temp
            temp = temp.next
        if temp is None:
            print("Position out of bounds!")
            return
        prev.next = temp.next

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    sll = SLL()
    sll.add()
    sll.display()
    sll.addFront()
    sll.display()
    sll.addLast()
    sll.display()
    sll.addPosition()
    sll.display()
    sll.removeFront()
    sll.display()
    sll.removeLast()
    sll.display()
    sll.removePosition()
    sll.display()
