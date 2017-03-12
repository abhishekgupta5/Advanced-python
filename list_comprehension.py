#!/usr/bin/python3

# filter() is used  to filter a list based on some condition provided as a Lambda expressionas first argument and list as second argument, example

# Filtering numbers divisible by 5
list1 = filter(lambda x: x % 5 == 0, range(1, 21))
print("Numbers divisible by 5")
print(list1)


# Print table of no.
no = 5
print("\nTable of %d" % no)
table = [[no,b,no*b] for b in range(1, 11)]
for i in table:
    print(i)

# Prime and noprime numbers in range 1-100

noprime = [j for i in range(2, 8) for j in range(i*2, 100, i)]
print("\nNoprime %s" % noprime)

prime = [x for x in range(2, 100) if x not in noprime]
print("\nPrime %s" % prime)

# Partition of list into N groups
list2 = ["My", "name", "is", "Abhishek", "Gupta"]
print("\nOrignal list %s" % list2)
partition = zip(*[iter(list2)] * 2)
print("\nPartitioning into groups of 2 ")
print(partition)
