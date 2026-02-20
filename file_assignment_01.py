"""
Q1.Create a program that:
Opens a file "names.txt" in write mode
Writes 5 names (one per line) entered by the user
Then opens the same file in read mode and prints all names
"""
with open ("names.txt","w") as f:
    for i in range(5):
        name = input(f"Enter name{i+1}:")
        f.writelines([name + "\n"]) # writes multiples lines

with open("names.txt","r") as f:
    names = f.read()
    print("The names are:")
    print(names)