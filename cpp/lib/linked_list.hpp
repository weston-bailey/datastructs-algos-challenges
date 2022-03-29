typedef int node_value;

class Node {
  public: 
    node_value data;
    Node *next;
    Node *prev;
    Node(node_value val) {
      data = val;
      next = NULL;
      prev = NULL;
    }

};

class LinkedList {
  public: 
    Node *head;
    Node *tail;
    int length;
    LinkedList() {
      head = NULL;
      tail = NULL;
      length = -1;
    }

    void print() { }

    Node push(node_value val) {
      Node *newNode = *Node(val);
      if (length < 0) { 
	head = newNode;
	tail = newNode;
	head->next = tail;
	tail->prev = head;
      } else {
	tail->next = newNode;
	newNode->prev = tail;
      } 
      length++;
      return newNode;
    }
};
