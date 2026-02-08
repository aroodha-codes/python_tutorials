#dictionaries are written in key value pairs
#dictionary are mutable and unordered
dict = {
    "name" : "ALICE",
    "Subject" : "AI",
    "Score" : 97
}
print(dict)
#methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("Score"))
added = dict.update({
    "City" : "New Delhi"
})
print(dict)
