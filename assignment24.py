""" Q4. Given a tuple of integers, 
create:
• A tuple of all even numbers
• A tuple of all odd numbers
"""
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print("Tuple:",t)
even = []
odd = []
for each in t:
    if (each % 2 == 0):
        even.append(each)
    else:
       odd.append(each)
Even_tuple = tuple(even)
odd_tuple = tuple(odd)
print("Even tuple:",Even_tuple)
print("Odd tuple:",odd_tuple)