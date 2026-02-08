color = input("Enter color:")
match color:
    case "Red":
        print("Stop.")
    case "Yellow":
        print("Ready.")
    case "Green":
        print("Go")
    case _:
        print("Wrong color!")
