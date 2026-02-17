"""
Concept: OOP Mini Project
Q10
Create an OOP Chat System with the classes:
• User
• Message
• ChatRoom
Implement features:
• sending messages
• viewing chat history
• user joining the chatroom
• user leaving the chatroom
"""
#classes 
class User:
    def __init__(self, username):
        self.username = username
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
    def __str__(self):
    # Returns a readable string representation of the object
        return f"{self.sender.username}: {self.content}"
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    #add user
    def add_user(self,user):
        if user in self.users:
            print(f"{user.username} is already present in {self.name}")
            return
        self.users.append(user)
        print(f"{user.username} joined {self.name}")
    #remove user
    def remove_user(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left {self.name}")
        else:
            print(f"{user.username} not found in {self.name}")
    #sending messages
    def broadcast_messages(self, sender, content):
        if sender not in self.users:
            print(f"{sender.username} is not present in {self.name} and cannot send messages.")
            return
        msg = Message(sender, content)
        self.messages.append(msg)
    #viewing history
    def view_history(self):
        for message in self.messages:
            print(message)

#testing
# Create users
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")
dave = User("Dave")  # extra user who never joins

# Create chatroom
room = ChatRoom("General Chat")

# Test 1: Users join the room
print("\n--- Test 1: Users Joining ---\n")
room.add_user(alice)
room.add_user(bob)
room.add_user(charlie)

# Test 2: Add already existing user
print("\n--- Test 2: Add Already Existing User ---\n")
room.add_user(alice)  # alice already in room

# Test 3: Dave tries to send message without joining
print("\n--- Test 3: Send Message Without Joining ---\n")
room.broadcast_messages(dave, "Hey can I join?")  # should be blocked

# Test 4: Normal conversation
print("\n--- Test 4: Normal Conversation ---\n")
room.broadcast_messages(alice, "Hey everyone!")
room.broadcast_messages(bob, "Hi Alice!")
room.broadcast_messages(charlie, "Hello all!")

# Test 5: View history
print("\n--- Test 5: Chat History ---\n")
room.view_history()

# Test 6: Bob leaves
print("\n--- Test 6: Bob Leaves ---\n")
room.remove_user(bob)

# Test 7: Bob tries to send after leaving
print("\n--- Test 7: Send Message After Leaving ---\n")
room.broadcast_messages(bob, "Can I still send?")  # should be blocked

# Test 8: Remove user not in room
print("\n--- Test 8: Remove User Not In Room ---\n")
room.remove_user(dave)  # dave never joined

# Test 9: Remove same user twice
print("\n--- Test 9: Remove Same User Twice ---\n")
room.remove_user(charlie)
room.remove_user(charlie)  # already removed

# Test 10: Send message to empty room
print("\n--- Test 10: Send Message To Empty Room ---\n")
room.remove_user(alice)  # last user leaves
room.broadcast_messages(alice, "Anyone there?")  # should be blocked

# Test 11: View history after all activity
print("\n--- Test 11: Final Chat History ---\n")
room.view_history()

# Test 12: New user joins empty room
print("\n--- Test 12: New User Joins Empty Room ---\n")
room.add_user(dave)
room.broadcast_messages(dave, "Hello? Anyone here?")
print("\n--- Test 12: Dave Chat History ---\n")
room.view_history()