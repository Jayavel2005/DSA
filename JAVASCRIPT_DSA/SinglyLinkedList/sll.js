class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    add() {
        let nodeCount = parseInt(prompt("Enter the node Count: "));
        for (let i = 0; i < nodeCount; i++) {
            let newNode = new Node(parseInt(prompt("Enter the data: ")));

            if (this.head === null) {
                this.head = newNode; // If the list is empty, this new node is both head and tail
                this.tail = newNode; // Set tail to the new node
            } else {
                this.tail.next = newNode; // Link the current tail to the new node
                this.tail = newNode; // Move the tail pointer to the new node
            }
        }
    }

    display() {
        let temp = this.head;
        while (temp !== null) {
            console.log(temp.data + " -> ");
            temp = temp.next;
        }
    }
}

const list = new SLL();

// Add a few nodes
list.add();

// Display the list
list.display();
