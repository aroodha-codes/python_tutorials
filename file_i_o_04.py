"""
#word search
with open("file_i_o_01_sample.txt","r") as f:
    if "wealthy" in f.read():
        print("Found.")
    else:
        print("Not Found.")
"""
#using while
line = 1
data = True
with open("file_i_o_01_sample.txt","r") as f:
    while data:
        data = f.readline()
        if "built" in data:
            print(f"Word Found at {line}")
            break
        line += 1
        print(data)