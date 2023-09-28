l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)