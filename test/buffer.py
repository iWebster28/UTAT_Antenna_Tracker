# buffer.py
# A ring buffer implementation.

# Can also use:
"""
import collections

buffer = collections.deque(maxlen=5)
for i in range(0, 10):
    buffer.append(i)
"""

# Allows for polling the IMU at a different rate than our tracker logic reads.

# enqueue(): write to location at write_ptr; advance write_ptr; leave read_ptr where it is.
# dequeue(): "read" item that read_ptr is pointed to; increment read_ptr.

# Time complexity: O(1) for enqueue(), dequeue().

class RingBuffer:
    def __init__(self, size):
        self.size = size if size != 0 else 1 # Min. size of 1
        self.data = []
        self.read_ptr = 0
        self.write_ptr = 0
    
    def __str__(self):
        line1 = f"Size: {self.size} | read_ptr: {self.read_ptr} | write_ptr: {self.write_ptr}"
        line2 = [item for item in self.data]
        return f"{line1}\n {line2}"

    def enqueue(self, item):
        """Enqueues an item to the ring buffer at position `write_ptr`"""
        if (len(self.data) == self.size):
            self.write_ptr = 0
            print("Buffer full; changing class.")
            self.__class__ = self.__isFull
            return
        
        self.data.insert(self.write_ptr, item)
        self.write_ptr = (self.write_ptr + 1) % self.size

    def dequeue(self):
        """Dequeues an item from the ring buffer at position `read_ptr`"""
        item = self.data[self.read_ptr]
        self.read_ptr = (self.read_ptr + 1) % self.size
        return item

    class __isFull:
        """Full buffer: can now use [] operator on list"""
        def enqueue(self, item):
            """Enqueues an item to the ring buffer at position `write_ptr`"""
            self.data[self.write_ptr] = item
            self.write_ptr = (self.write_ptr + 1) % self.size
        
        def dequeue(self): # unchanged
            """Dequeues an item from the ring buffer at position `read_ptr`"""
            item = self.data[self.read_ptr]
            self.read_ptr = (self.read_ptr + 1) % self.size
            return item
        
        def __str__(self):
            line1 = f"Size: {self.size} | read_ptr: {self.read_ptr} | write_ptr: {self.write_ptr}"
            line2 = [item for item in self.data]
            return f"{line1}\n {line2}"
 

# Testing
if __name__ == "__main__":
    print("--- Ring Buffer Test ---")
    buffer = RingBuffer(2)
    
    # Enqueue
    for item in [1, 2]:
        buffer.enqueue(1)
        print(buffer)

    # Dequeue
    for i in range(0, 3):
        value = buffer.dequeue()
        print(f"Read: {value}")
        print(buffer)

    # Enqueue    
    for item in [1, 2, 3]:
        buffer.enqueue(1)
        print(buffer)
    
    # Dequeue
    for i in range(0, 3):
        value = buffer.dequeue()
        print(f"Read: {value}")
        print(buffer)
