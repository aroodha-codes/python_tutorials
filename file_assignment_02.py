"""
Q2.Create a program that:
Opens a file "log.txt" in append mode
Adds a new log entry (like "Program run successfully")
Opens the file in read mode and prints all logs
"""
with open("log.txt","a") as f:
    f.write("\nProgram runs successfully.")
    
with open("log.txt","r") as f:
    logs = f.read()
    print(logs)