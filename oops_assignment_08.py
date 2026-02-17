"""
Concept: Instance and Class Attributes
Q8.Create a class Player with:
• a class variable player_count
• instance variables name and level
Track how many players are created.
"""
class Player:
    player_count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count += 1
        
#testing
p1 = Player("Ankush","National")
p2 = Player("Ayush","state")
print(p1.name,p1.level)
print(p2.name,p2.level)
print(f"The total players are:{Player.player_count}")