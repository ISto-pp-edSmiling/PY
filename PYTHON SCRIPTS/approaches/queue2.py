import collections

de = collections.deque([1,2,3,4,5,6])

de.insert(3,10)   # at the 3rd position inserting 10

print(de.count(3))   # counts all instances of three
de.remove(3)
# there is also de.extend and de.extendleft

print(de)
de.rotate(3)
print(de, 'rotated by index 3')