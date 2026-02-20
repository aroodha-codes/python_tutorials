"""
Q4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json"
Then load the JSON and print each city and its population.
Ask the user for a new city & its population. Update this info in the json file.
"""
import json
data = {
    "city":"population",
    "Tokyo":"13.96 million",
    "New York":"8.3 million",
    "Mumbai":"12.5 million"
}
#original
with open ("cities.json","w") as f:
    json.dump(data,f,indent = 4)
    
with open ("cities.json","r") as f:
    d = json.load(f)
    print("City >> Population")
    print("-"*30)
    for c,p in d.items(): #for dictionaries use .items()
        print(c,">>",p)
        
new_city = input("Enter city:")
new_population = input("Enter population:")
data[new_city] = new_population
#updated
with open ("cities.json","w") as f:
    json.dump(data,f,indent = 4)
    
print("Updated cities:")
print(data)