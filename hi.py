HASH_DATA_SIZE = 8

hash_data = [None] * HASH_DATA_SIZE

def hash_function(s):
    """Naive hashing function --do not use in production!!"""

    # O(n) over the key length
    # O(1) over the HASH_DATA_SIZE

    bytes_list = s.encode()

    total = 0


    for b in bytes_list:  # O(n) over the length of the key
        total += b


        total &= 0xffffffff # 32 bit (8 f's)

    return total

def get_index(s):
    hash_value = hash_function(s)

    return hash_value % HASH_DATA_SIZE

def put(k, v):
    """For a given key, store a value in the hash table"""
    index = get_index(k)
    hash_data[index] = v

def get(k):
    index = get_index(k)

    return hash_data[index]



#print(hash_data)

put("Beej!", "Hello, world!")
# put("g", "zyx")
#put("Goats", 3490)
print(get("Beej!"))
# print(get("Goats"))



#put("Beej!", "Hello, again," )
#print(hash_data)
# print(hash_function("Beej!"))
# print(hash_function("Goats"))
# print(hash_function("oGats"))

   def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY #defined at the top
        self.buckets = [None] * capacity #internal array
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key): #loop through each character in the key
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity # hashsum does not get too gigantic and make sure it stays in the required range
        return hashsum
    def insert(self, key, value):
        self.size += 1 #increment the total size by 1. We know we added an element
        index = self.hash(key)  #Need to know the index we are going to inside the array
        node = self.buckets[index] #find the node at that index
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value) #prev is set to the last node in the linked list
    def find(self, key):
        index = self.hash(key) #compute index using our hash function
        node = self.buckets[index] #find the node
        while node is not None and node.key != key: #find the key or end of the list
            node = node.next
        if node is None: #reached end or nothing was ever there
            return None
        else:
            return node.value
    def remove(self, key): 
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key: #find the node we are looking for
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result