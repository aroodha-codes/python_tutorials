""" Q2.Given a list of integers compute the average of all numbers in the list"""
list = [7,9,11]
sum = 0
for each in list:
    sum += each
average = sum/len(list)
print(average)