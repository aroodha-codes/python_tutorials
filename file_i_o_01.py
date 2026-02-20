f = open("file_i_o_01_sample.txt","r")
data = f.read()
print(data)
print(type(data))
#readline reads line by line
#data = f.readline()
#print(data)
#if we open file we have to close it
f.close()