"""Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
list1 = [1, 2, 7] list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
"""
l1 = list(map(int ,input("Enter numbers for L1:").split(",")))
l2 = list(map(int ,input("Enter numbers for L2:").split(",")))
result = l1 + l2
print(result)
result.sort()
print(result)