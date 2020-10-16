class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.storage = []
        self.count = 0

    def append(self, item):
        # If len of storage is equal to capacity 
        if len(self.storage) == self.capacity: 
            # Set item to storage at count index
            self.storage[self.count] = item
            # If count plus 1 equals capacity 
            if self.count + 1 == self.capacity: 
                self.count = 0
            else:
                # If not -1 away from capacity add 1 
                self.count += 1 
        else: 
            # If not at capacity recursivley
            self.storage.append(item)
        return item


    def get(self):
        return self.storage