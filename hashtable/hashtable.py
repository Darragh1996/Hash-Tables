class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.num_elements = 0
        self.load_factor = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # hash_num = 0
        # for i in range(0, len(key)):
        #     hash_num += (ord(key[i]) * (i + 1))
        # print("hash: ", hash_num)
        # return hash_num & 0xFFFFFFFF

        hash = 5381
        for char in key:
            hash = ((hash * 33) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        # print("index: ", self.djb2(key) % self.capacity)
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.load_factor >= 0.7:
            self.resize()
        if self.storage[self.hash_index(key)] == None:
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)
            self.num_elements += 1
        else:
            current = self.storage[self.hash_index(key)]
            while current.next != None:
                if current.key == key:
                    current.value = value
                    break
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = HashTableEntry(key, value)
                self.num_elements += 1
        self.load_factor = self.num_elements / self.capacity

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.storage[self.hash_index(key)].key == key:
            self.storage[self.hash_index(key)] = None
        else:
            current = self.storage[self.hash_index(key)]
            while current.next.key != key:
                if current.next == None:
                    break
                else:
                    current = current.next
            current.next = current.next.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.storage[self.hash_index(key)] != None:
            if self.storage[self.hash_index(key)].key == key:
                return self.storage[self.hash_index(key)].value
            else:
                current = self.storage[self.hash_index(key)]
                while current.key != key:
                    if current.next == None:
                        return None
                    current = current.next
                return current.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.load_factor = 0
        self.num_elements = 0
        oldStuff = self.storage
        self.capacity *= 2
        # self.load_factor = self.num_elements / self.capacity
        self.storage = [None] * self.capacity
        for i in oldStuff:
            if i != None:
                current = i
                while current != None:
                    self.put(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(5)
    print("load factor: ", ht.load_factor)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "Resize!")
    print("load factor: ", ht.load_factor)

    # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    # ht.resize()
    ht.put("line_5", "Resize!")
    print("load factor: ", ht.load_factor)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")
