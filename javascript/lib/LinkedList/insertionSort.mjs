// import { isSorted } from './isSorted.mjs'



function insertionSort(list) {
  if(list.isEmpty()) return null;
  let listSorted = false;
  let madeSwap = false;

  while(!listSorted){
    let currentNode = list.head.next;
    let previousNode = null
    while(currentNode){
      // stop when the next node is null
      if(!currentNode.next){
        // if a swap was made, start again at the head
        if(madeSwap){
          currentNode = list.head.next;
          madeSwap = false;
        } else {
          listSorted = true;
        }
      }
      list.log()
      if(currentNode.value > currentNode.next.value) {
        let prev = previousNode;
        let current = currentNode;
        let next = currentNode.next;
        previousNode.next = next;
        currentNode.next.next = current;
        currentNode.next = next.next;
      }
      previousNode = currentNode;
      currentNode = currentNode.next;
    }

  }
  return isSorted(list)
}

export { insertionSort }