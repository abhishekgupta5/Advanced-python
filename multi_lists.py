#!/usr/bin/python3

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print('First list- %s' % list1)
print('Second list- %s' % list2)
print('Merged list')
# zip() uses 2 lists as arguments and merges them together in pairs
for a, b in zip(list1, list2):
    print(a, b)
