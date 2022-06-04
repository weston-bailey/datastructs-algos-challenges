

class PriorityQueue:
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
            checks if queue is empty
        '''
        pass

    def insert(self, data):
        '''
            adds a new data value to queue at last priority
        '''
        pass

    def clear(self):
        '''
            clears all items in the queue
        '''
        pass

    def peek(self):
        '''
            retrieves, but does not rmove, the head of the queue
        '''
        pass

    def poll(self):
        '''
            retrives and removes the head of the queue
        '''
        pass

    def add(self, data, priority):
        '''
            adds data at a specific priority
        '''
        pass

    def contains(self, data):
        '''
            returns true if data is found in queue
        '''
        pass
