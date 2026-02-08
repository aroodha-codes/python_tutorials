"""Q8. Write a program to check whether two lists share no common elements.
share no common elements : list1=[1,2,3,4] & list2=[5,6,7,8]
share common elements : list1=[1,2,3] & list2=[3,4]
"""
list1 = list((map(int,input("Ente list 1:").split(","))))
list2 = list((map(int,input("Ente list 2 :").split(","))))
for l1 in list1:
    if (l1 in list2):
        print("Share common elements.")
        break
else:
    print("No common elements.")
        