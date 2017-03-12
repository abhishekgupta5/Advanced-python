#!/usr/bin/python3

# filter() is used  to filter a list based on some condition provided as a Lambda expressionas first argument and list as second argument, example

#filtering numbers divisible by 5
list1 = filter(lambda x: x % 5 == 0, range(1, 21))
print("Numbers divisible by 5")
print(list1)


#print table of no.
no = 5
print("\nTable of %d" % no)
table = [[no,b,no*b] for b in range(1, 11)]
for i in table:
    print(i)

# prime and noprime numbers in range 1-100

noprime = [j for i in range(2, 8) for j in range(i*2, 100, i)]
print("\nNoprime %s" % noprime)

prime = [x for x in range(2, 100) if x not in noprime]
print("\nPrime %s" % prime)
