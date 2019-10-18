import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
binary_names_1 = BinarySearchTree(names_1[0])
for name in names_1:
    if name is not names_1[0]:
        binary_names_1.insert(name)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
binary_names_2 = BinarySearchTree(names_2[0])
for name in names_2:
    if name is not names_2[0]:
        binary_names_2.insert(name)
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# Runtime for this solution is O(n^2)

duplicates = []

def append_dupplicates(value):
    if binary_names_2.contains(value):
        duplicates.append(value)

binary_names_1.for_each(append_dupplicates)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
