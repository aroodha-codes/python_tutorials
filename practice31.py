#sets are mutable,unique and unordered
s = {1,2,3,4,}
print(s)
print(type(s))
s.add(5)
print(s)
empty = set()
print(type(empty))
#set methods
s.remove(4)
print(s)
print(s.clear())
s = {1,2,3,4}
s2 = {3,4,5,6,7}
print(s.union(s2))
print(s.intersection(s2))