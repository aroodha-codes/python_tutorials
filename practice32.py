"""Student Enrolments
Given a list of tuples with info (name, subject):"""
info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
"""list all unique course"""
unique_courses = set()
for tup in info:
    unique_courses.add(tup[1])
print(unique_courses)
"""list students enrolled in English"""
for name,courses in info:
    if (courses == "English"):
        print(name)
"""create dictionary (student, set of courses)"""
print("Dictionary")
dict = {}
for name ,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)