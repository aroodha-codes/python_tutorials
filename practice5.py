username = input("Enter name:")
password = input("Enter password:")
if (username=="admin" and password=="pass"):
    print("Login successful...")
else:
    if(username!="admin" and password=="pass"):
        print("Invalid username!")
    elif (username=="admin" and password!="pass"):
        print("Invalid password.")
    else:
        print("Invalid credentials!")