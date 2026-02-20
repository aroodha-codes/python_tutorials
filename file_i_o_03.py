import os
with open("file_i_o_01_sample.txt","r") as f:
    data = f.read()
    print(data)
    print(len(data))
os.remove("file_i_o_01_sample.txt")
#os.remove("file_i_o_02_sample.txt")
