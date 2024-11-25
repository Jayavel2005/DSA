class Node{
    int data;
    Node next;
    Node(int data){
        this.data = data;
        this.next = null;
    }
}
class LinkedList {

    Node head = null;
    Node temp = null;
    // Adding Nodes
    public void add(int data){
        Node newNode = new Node(data);
        if(this.head == null){
            head = newNode;
            temp = newNode;
        }
        else{
            temp.next  = newNode;
            temp = newNode;

        }
    }
    // InsertAtFront
    public void addFront(int data){
        Node newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
    }
    // InsertAt last
    public void addLast(int data){
        Node newNode = new Node(data);
        temp = this.head;
        while (temp.next!=null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }
    // Add at Position
    public void addPosition(int data, int position){
        Node newNode = new Node(data);
        temp = this.head;
        for(int i = 1;i<position;i++){
            temp = temp.next;
        }
        newNode.next = temp.next;
        temp.next = newNode;

    }

    // Remove at Front
    public void removeFront(){
        if(this.head == null){
            System.out.println("Linked List is empty.");
            return;
        }
        this.head = this.head.next;
    }

    // remove at last
    public void removeLast(){
        temp = this.head;
        while (temp.next.next!=null) {
            temp = temp.next;
        }
        temp.next = null;
    }

    // Remove at position
    // Remove at Position
    public void removePosition(int position) {
        if (this.head == null) {
            System.out.println("The list is empty. Nothing to remove.");
            return;
        }

        if (position == 0) {
            this.head = this.head.next;
            return;
        }

        Node prev = null;
        temp = this.head;

        for (int i = 1; i <= position; i++) {
            if (temp == null) {
                System.out.println("Position out of bounds!");
                return;
            }

            prev = temp;
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("Position out of bounds!");
            return;
        }

        prev.next = temp.next;
    }


    // Display 
    public void display(){
        Node temp = this.head;
        while (temp!=null) {
                System.out.print(temp.data + " -> ");
                temp = temp.next;
        }
    }

    
}

public class SinglyLinkedList {

    public static void main(String[] args) {
        LinkedList sll = new LinkedList();

        sll.add(90);
        sll.add(89);
        sll.add(12);
        sll.addFront(10);
        sll.addLast(34);
        sll.display();
        System.out.println();
        sll.removePosition(0);
        sll.display();

    }
    
}