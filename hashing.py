import random
import time
# Hash Table Implementation with Separate Chaining

class HashTable:
    def __init__(self, size=10, prime=109345121):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = prime
        self.a = random.randint(1, prime-1)
        self.b = random.randint(0, prime-1)

    def load_factor(self):
        num_elements = sum(len(chain) for chain in self.table)
        return num_elements / self.size

    def _hash(self, key):
        return ((self.a * hash(key) + self.b) % self.p) % self.size

    # Insert: Add a key-value pair to the hash table.
    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # Update value if key exists
                return
        self.table[idx].append((key, value))

    # Search: Retrieve a value associated with a given key.
    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    # Delete: Remove a key-value pair from the hash table.
    def delete(self, key):
        idx = self._hash(key)
        self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]

# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    start = time.time()
    ht.insert("Austin", 1)
    ht.insert("Buffalo", 2)
    ht.insert("Cleveland", 3)
    print(f"Load factor: {ht.load_factor():.2f}")

    # Timing search for search operation
    start = time.time()
    print(ht.search("Cleveland"))
    end = time.time()
    print(f"Search time: {end - start:.8f} seconds")

    # time for insert operation
    start = time.time()
    ht.insert("Denver", 4)
    end = time.time()
    print(f"Insert time: {end - start:.8f} seconds")

    # time for delete operation
    start = time.time()
    ht.delete("Buffalo")
    end = time.time()
    print(f"Delete time: {end - start:.8f} seconds")