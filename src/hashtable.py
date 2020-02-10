# '''
# Linked List hash table key/value pair
# '''

import hashlib

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.currentSize = 0

    def _hash(self, key):
        # hashed = hashlib.sha256(key).hexdigest()
        # print(hashed)
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        hash = 5381
        # 33 would also work?
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''

        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # print(self._hash(key) % self.capacity)
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed = self._hash_mod(key)
        self.storage[hashed] = LinkedPair(key, value)

        if self.storage[hashed]:
            pushed = LinkedPair(key, value)
            pushed.next = self.storage[hashed]
            self.storage[hashed] = pushed
        else:
            self.storage[hashed] = LinkedPair(key, value)
            self.currentSize =+ 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed = self._hash_mod(key)

        if self.storage[hashed]:
            self.storage[hashed] = None
            self.currentSize -1
        else:
            return None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed = self._hash_mod(key)
        
        # if self.storage[hashed]:
        #     while self.storage[hashed]:
        #         if self.storage[hashed].key is key:
        #             return self.storage[hashed].value
        #         else:
        #             self.storage[hashed].next
        # return None

        if self.storage[hashed]:
            return self.storage[hashed].value
        else:
            return("Key was not found")
            
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        self.capacity *= 2
        new_storage = HashTable(self.capacity)

        for i in range(self.currentSize):
            self.insert(i.key, i.value)

        self.storage = new_storage.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
