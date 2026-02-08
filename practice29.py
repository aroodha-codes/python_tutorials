#tuples are immutables
t = (1,2,3,4,5,4,4)
print(t)
#tuples using loops
sum = 0
for i in t:
    sum += i
print(sum)
#tuple methods
r = t.index(3)
print(r)
c = t.count(4)
print(c)