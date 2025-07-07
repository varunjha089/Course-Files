Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import heapq
>>> # Define a tree node
... class Node:
...     def __init__(self, char, freq):
...         self.char = char # Character (None for internal nodes)
...         self.freq = freq # Frequency of the character
...         self.left = None # Left child
...         self.right = None # Right child
...     # Comparison operator for priority queue (min-heap)
...     def __lt__(self, other):
...         return self.freq < other.freq
... def huffman_coding(char_freq):
...     # Create a heap with one node per character
    heap = [Node(c, f) for c, f in char_freq.items()]
    heapq.heapify(heap)
    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap) # Least frequent node
        right = heapq.heappop(heap) # Next least frequent
        # Merge both nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged) # Insert merged node back
    return heap[0] # Return the root of the Huffman Tree
SyntaxError: invalid syntax
>>> char_freq = {
... ’A’: 5,
... ’B’: 9,
... ’C’: 12,
... ’D’: 13,
... ’E’: 16,
... ’F’: 45
... }
SyntaxError: invalid character '’' (U+2019)
>>> char_freq = {
...     'A' : 5,
    'B' : 9,
    'C' : 12,
    'D' : 13,
    'E' : 16,
    'F' : 45
}
root = huffman_coding(char_freq)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    root = huffman_coding(char_freq)
NameError: name 'huffman_coding' is not defined
def huffman_coding(char_freq):
    # Create a heap with one node per character
    heap = [Node(c, f) for c, f in char_freq.items()]
    heapq.heapify(heap)
    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap) # Least frequent node
        right = heapq.heappop(heap) # Next least frequent
        # Merge both nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged) # Insert merged node back
    return heap[0] # Return the root of the Huffman Tr

char_freq = {
    'A' : 5,
    'B' : 9,
    'C' : 12,
    'D' : 13,
    'E' : 16,
    'F' : 45
}
root = huffman_coding(char_freq)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    root = huffman_coding(char_freq)
  File "<pyshell#13>", line 3, in huffman_coding
    heap = [Node(c, f) for c, f in char_freq.items()]
NameError: name 'Node' is not defined. Did you mean: 'None'?
class Node:
    def __init__(self, char, freq):
        self.char = char # Character (None for internal nodes)
        self.freq = freq # Frequency of the character
        self.left = None # Left child
        self.right = None # Right child
    # Comparison operator for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

    
def huffman_coding(char_freq):
    # Create a heap with one node per character
    heap = [Node(c, f) for c, f in char_freq.items()]
    heapq.heapify(heap)
    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap) # Least frequent node
        right = heapq.heappop(heap) # Next least frequent
        # Merge both nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged) # Insert merged node back
    return heap[0] # Return the root of the Huffman Tr

char_freq = {
    'A' : 5,
    'B' : 9,
    'C' : 12,
    'D' : 13,
    'E' : 16,
    'F' : 45
}
root = huffman_coding(char_freq)
root
<__main__.Node object at 0x000001E1BF6307D0>
def print_huffman_codes(node, code=""):
    if node is None:
        return
    # Leaf node: has a character
    if node.char is not None:
        print(f"{node.char}: {code}")
    print_huffman_codes(node.left, code + "0")
    print_huffman_codes(node.right, code + "1")

    
print_huffman_codes(root)
F: 0
C: 100
D: 101
A: 1100
B: 1101
E: 111
