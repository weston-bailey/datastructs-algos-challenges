class PriorityQueue:
    '''
        FIFO priority based queue
    '''
    def __init__(self):
        self.queue = []

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        '''
            returns True when Queue is empty, False when not
        '''
        return len(self) == 0

    def insert(self, data):
        '''
            adds a new data value to queue at last priority
        '''
        self.queue.append(data)
        return self

    def clear(self):
        '''
            clears all items in the queue
        '''
        self.queue = []
        return self

    def peek(self):
        '''
            retrieves, but does not remove, the head of the queue. Returns None if empty.
        '''
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def poll(self):
        '''
            retrives and removes the head of the queue, returns None if empty
        '''
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def add(self, data, priority):
        '''
            adds data at a specific priority
        '''
        self.queue[priority] = data
        return self

    def contains(self, data):
        '''
            returns true if data is found in queue
        '''
        try:
            self.queue.index(data)
            return True
        except ValueError:
            return False

