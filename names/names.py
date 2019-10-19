import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
line_count = 0
for line in f:
    if line_count == 0:
        binary_names_2 = BinarySearchTree(line[:-1])
    else:
        binary_names_2.insert(line)
    line_count += 1
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# Runtime for this solution is O(n^2)

duplicates = [name for name in names_1 if binary_names_2.contains(name + "\n")]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
