#using loops in lists
list = [1,2,10,3,4]
idx = 0
x = 10
for i in list:
    if (i == x):
        print(f"x found at index {idx}")
        break
    idx += 1
    