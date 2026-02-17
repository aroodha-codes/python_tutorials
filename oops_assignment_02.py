"""
Concept: Classes and Objects
Q2.Create a class Book with the following attributes:
• title
• author
• list of reviews
Add methods to: add a new review,count reviews,display all reviews  
"""
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.list_of_reviews = []
    # method to add new review
    def add_review(self,review):
        self.list_of_reviews.append(review)
        
    # to count  total reviews
    def count_reviews(self):
        return len(self.list_of_reviews)
    
    # display all reviews
    def display_reviews(self):
        for review in self.list_of_reviews:
            print(review)
    
b1 = Book("VS_CODE","MICROSOFT")
b1.add_review("Great for coding!")
b1.add_review("Very helpful")
b1.add_review("Love it!")        
print(b1.title,b1.author)        

print(f"Total reviews: {b1.count_reviews()}")
b1.display_reviews()