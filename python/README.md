# Python Data Structures and Algorithms

## unittest cheatsheet

See [here](https://docs.python.org/3/library/unittest.html#test-cases) for test case methods.

to run a test use `python3 -m unittest <file_name>`

```python
from unittest import TestCase, main

class Test_Name(TestCase):
    def test_description(self):
        self.assertTrue(True, True)

if __name__ == '__main__':
    main()
```

## General Todos

- [x] create function to check if arrays are sorted
- [x] merge all of the random list functions from ./lib/data into one function
- [ ] add the rest of sorts
- [ ] add sort speed tests
- [ ] https://jovian.ai/learn/data-structures-and-algorithms-in-python

## Coding challenges

## Sort Algorithms

- [x] Bubble Sort
- [ ] bucket_sort
- [ ] heap sort
- [ ] insertion_sort
- [ ] quick sort
- [ ] Timsort
- [ ] selection sort
- [ ] Tree sort
- [ ] shell sort
- [ ] radix sort
- [ ] counting sort
- [ ] cubesort

## Data Structures

### Linked List

- [ ] single
- [ ] double
- [ ] circular
- [ ] stack
- [ ] queue

### Binary Search Tree

### Trie

### Stack

### Queue

- [ ] priority queue https://adrianmejia.com/priority-queue-data-structure-and-heaps-time-complexity-javascript-implementation/

### Graph

### Blockchain

https://www.section.io/engineering-education/how-to-create-a-blockchain-in-python/
- [x] merkle tree https://trebaud.github.io/posts/merkle-tree/
- [x] blockchain https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
