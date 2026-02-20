# the list comprehension we can do it insteadof loops
# [output for item in iterable if condition] if is optional
sq = [i*i for i in range(6) if i
      %2 != 0]
print(sq)

nums = [8,-5,2,-3,7,-3]
ans = [0 if num<0 else num for num in nums]
print(ans)

words = ["Hello","Python","AI"]
words = [val.upper() for val in words]
print(words)