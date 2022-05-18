// https://www.notion.so/Linked-List-White-boarding-Problems-137e8a2cddb94e33a3b1f5f08bbfdac5

// a list node
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

// linked list datatype
class Single {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  /* // // // // // // // // // //
  UTILITY METHODS
  */ // // // // // // // // // // 

  // just for fun
  toString() {
    return `[object ${this.constructor.name}]`
  }

  // can be checked to see if list is empty 
  isEmpty() {
    return this.size === 0;
  }

  // executes a callback function on each Node in the list with arguments index and currentNode and supplied args
  forEachNode(callback, ...args) {
    if(typeof callback != 'function') return console.error('supplied argument to forEachNode() must be a function');

    let callbackReturn;
    let currentNode = this.head;
    let i = 0;
    while(currentNode != null) {
      callbackReturn = callback(currentNode, i, ...args);
      currentNode = currentNode.next;
      i++
    }
  
    return callbackReturn;
  }

  // calculate how many nodes there are in a list
  length() {
    return this.forEachNode( (currentNode, i) => {
      return i;
    });
  }

  // print list with optional start and stop nodes, no return
  log(beg, end) {
    let start = beg || 0;
    let stop = end || this.size;

    if(this.isEmpty()) console.log(null);

    this.forEachNode( (currentNode, i) => {
      if(i >= start && i <= stop){
        console.log(i, currentNode)
      }
    }, start, stop)
  }

  /* // // // // // // // // // //
  OPERATION METHODS
  */ // // // // // // // // // //   

  //returns node at index
  get(index){
    // add check for empty list, if true, return null
    if(this.isEmpty()) return null;
    // if index is out of range
    if(index > this.size || index < 0) {
      console.error(`Index out of range.`)
      return null;
    }

    // if index 0, return node.head
    if(index === 0) {
      return this.head
    }

    // if index == lenght - 1, node.tail
    if(index === this.size) {
      return this.tail
    }

    // we want a node anywhere in the list minus head or tail
    let currentNode = this.head
    let i = 1
    while (i < index) {
      i++
      currentNode = currentNode.next
    }
    
    // return node found at index
    return currentNode
  }

  // add value to end of list
  push(value) {
    //  make a new node
    const newNode = new Node(value)

    // populate head and tail if list if empty
    if(this.isEmpty()){
      this.head = newNode;
      this.tail = newNode;
    // set the tail's next to the new node and place the new node at the tail
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++
  }

  // add a node to the beginning of the list
  append(value) {
    // make a new node
    const newNode = new Node(value);

    // update head and tail if list if empty
    if(this.isEmpty()){
      this.head = newNode;
      this.tail = newNode;
    // asiign head to the next of the new node and place the new node at the head
    } else {
      newNode.next = this.head;
      this.head = newNode
    }
    this.size++
  }

  // remove last node form list
  pop() {
    // bail if the list if empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    let removed;
    // find the second to last node
    let currentNode = this.get(this.size - 1);
    // grab the next node to return it after removal
    removed = currentNode.next;
    // nullify last node and update tail
    currentNode.next = null;
    this.tail = currentNode;
    // decrement list size
    this.size--;
    // return the node that was removed 
    return removed;
  }

  // remove first node from the list
  shift() {
    // return immediately is list is empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    let removed;
    // grab the node to be returned
    removed = this.head;
    // set head to next 
    this.head = this.head.next;
    // decrement size
    this.size--;
    if(this.isEmpty()) this.tail = null;
    return removed;
  }

  // removes node at index and returns it
  remove(index) {
    // return immediately is list is empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    
    // in case we are removing the head or tail
    if(index === 0) return this.shift();
    if(index === this.size) return this.pop();
    
    let removed;
    // find the node right before the one we want to remove
    let currentNode = this.get(index - 1);
    // return if no node was found (likely a bad index)
    if(currentNode === null) return null;
    // grab the next node to return it after removal
    removed = currentNode.next;
    currentNode.next = currentNode.next.next;
    // decrement list size
    this.size--;
    // return the node that was removed 
    return removed;
  } 

  // replace a value at an index
  replace(index, value) {
    // if list is empty return with an error
    if(this.isEmpty()) return console.error('list is empty');
    // make a new node
    const newNode = new Node(value);

    // handle case if the index is the head 
    if(index === 0) {
     newNode.next = this.head.next;
     this.head = newNode;
     return
    }

    // find the node before the index
    let currentNode = this.get(index - 1);
    // return if no node at that index is found
    if(currentNode === null) return null;
    // if we are at the end of the list, update the tail
    if(this.size === index) {
      currentNode.next = newNode;
      this.tail = newNode;
    } else {
      newNode.next = currentNode.next.next;
      currentNode.next = newNode;
    }
    return
  }

  // removes all nodes of the list and returns the count of nodes nullified
  clear() {
    if(this.isEmpty()) return 0;
    // how many nodes have been removed
    let inc = 0;

    return this.forEachNode( (currentNode) => {
      this.shift();
      inc++
      return inc;
    })
  }

  // returns first found index of value
  find(value) {
    if(this.isEmpty()) return null;

    let currentNode = this.head;
    let i = 0;
    while(currentNode != null) {
      if(currentNode.value === value) break;
      currentNode = currentNode.next;
      i++
    }
    // if current node is null, we reached the end without finding the value
    return currentNode ? i : null;
  }

  // returns and array of all indexes with value
  findAll(value) {
    if(this.isEmpty()) return null;
    let indexes = []
    this.forEachNode( (currentNode, index) => {
      if(currentNode.value === value) return indexes.push(index);
    }, indexes)

    return indexes.length ? indexes : null;
  }

  // returns the last found index of supplied value
  findLast(value) {
    let all = this.findAll(value);
    return all ? all[all.length - 1] : null;
  }
  
  // concatenate multiple lists and return a new list (doesn't have to include self)
  concat(...args) {
    let newList = new Single();

    // make sure arguments are all lists and add up the total length
    for(let i = 0; i < args.length; i++){
      if(args[i].toString() != '[object Single]') return console.error('arguments must be of type Single');

      // iterate over current list and push it to new list
      let currentNode = args[i].head
      let j = 0;
      while(j < args[i].size){
        newList.push(currentNode.value)
        currentNode = currentNode.next;
        j++;
      }
    }
    return newList
  }

  // returns the highest and lowest values found in the list...only for number values presently
  bounds() {
    if(this.isEmpty()) return null;
    // maximum boundaries possible
    let min = Number.POSITIVE_INFINITY
    let max = Number.NEGATIVE_INFINITY

    return [min, max] = this.forEachNode( (currentNode) => {
      if(currentNode.value < min) min = currentNode.value;
      if(currentNode.value > max) max = currentNode.value;
      return [min, max]
    }, min, max)
    
  }

  /* // // // // // // // // // //
  CHALLENGE SOLUTION METHODS
  */ // // // // // // // // // // 

  // returns the value at the middle index of the list
  middle() {
    let index = this.size - 1 
    if(index % 2 === 0) {
      // size is even
      return this.get(Math.floor(index * .5))
    }
    // size is odd
    return this.get((index * .5) + 1) 
  }
}

export { Single }
