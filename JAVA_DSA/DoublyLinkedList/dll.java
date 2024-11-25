import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node prev;

    Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {

    Scanner scanner = new Scanner(System.in);
    Node head = null;
    Node tail = null;

    // Add nodes to the list
    public void add() {
        System.out.print("Enter the node Count: ");
        int nodeCount = scanner.nextInt();
        for (int i = 0; i < nodeCount; i++) {
            System.out.print("Enter the node data: ");
            Node newNode = new Node(scanner.nextInt());
            scanner.nextLine();
            if (this.head == null) {
                this.head = this.tail = newNode; // Initialize head and tail
            } else {
                this.tail.next = newNode;
                newNode.prev = this.tail;
                this.tail = newNode;
            }
        }
    }

    // Add a node at the front
    public void addFront() {
        System.out.print("Enter the node data to add front: ");
        Node newNode = new Node(scanner.nextInt());
        scanner.nextLine();
        if (this.head == null) {
            this.head = this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head.prev = newNode;
            this.head = newNode;
        }
    }

    // Add a node at the end
    public void addLast() {
        System.out.print("Enter the node data to add last: ");
        Node newNode = new Node(scanner.nextInt());
        scanner.nextLine();
        if (this.tail == null) {
            this.head = this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }

    // Remove a node from the front
    public void removeFront() {
        if (this.head == null) {
            System.out.println("List is empty. Nothing to remove.");
            return;
        }
        System.out.println("Removed: " + this.head.data);
        if (this.head == this.tail) { // Single node case
            this.head = this.tail = null;
        } else {
            this.head = this.head.next;
            this.head.prev = null;
        }
    }

    // Remove a node from the last
    public void removeLast() {
        if (this.tail == null) {
            System.out.println("List is empty. Nothing to remove.");
            return;
        }
        System.out.println("Removed: " + this.tail.data);
        if (this.head == this.tail) { // Single node case
            this.head = this.tail = null;
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
        }
    }

    // Remove a node at a specific position
    public void removeAtPosition() {
        System.out.print("Enter the position to remove: ");
        int position = scanner.nextInt();

        if (this.head == null) {
            System.out.println("List is empty. Nothing to remove.");
            return;
        }

        if (position == 1) {
            removeFront();
            return;
        }

        Node current = this.head;
        int count = 1;

        while (current != null && count < position) {
            current = current.next;
            count++;
        }

        if (current == null) {
            System.out.println("Invalid position. No node to remove.");
        } else if (current == this.tail) {
            removeLast();
        } else {
            System.out.println("Removed: " + current.data);
            current.prev.next = current.next;
            current.next.prev = current.prev;
        }
    }

    // Display the list
    public void display() {
        if (this.head == null) {
            System.out.println("The list is empty.");
            return;
        }
        Node temp = this.head;
        while (temp != null) {
            System.out.print(temp.data);
            if (temp.next != null) {
                System.out.print(" -> ");
            }
            temp = temp.next;
        }
        System.out.println(" -> null");
    }
}

public class dll {

    public static void main(String[] args) {
        DoublyLinkedList linkedList = new DoublyLinkedList();
        linkedList.add();
        linkedList.display();

        linkedList.addFront();
        linkedList.addLast();
        linkedList.display();

        linkedList.removeFront();
        linkedList.display();

        linkedList.removeLast();
        linkedList.display();

        linkedList.removeAtPosition();
        linkedList.display();
    }
}
