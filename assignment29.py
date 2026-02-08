"""Q9. Given a list, print all elements that appear more than once in the list
[Hint- use sets]
"""
list = [8,9,7,5,6,2,5,7]
seen = set()
repeted = set()
print(type(seen))
for l in list:
    if (l in seen):
        repeted.add(l)
    else:
        seen.add(l)
print("Repeted elements are:",repeted)
print(type(repeted))