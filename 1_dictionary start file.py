import random

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(type(phonebook))
# list uses index value to search
# dictionaries uses key to search

print(len(phonebook))

mydictionary = dict(m=9, n=10)
print(mydictionary)
# dict function used to create a dictionary

# how to index a dictionary
# dictionary-name[key]
#ie. phonebook['Chris']

print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

# print(phonebook["Chris"])
# print(phonebook['chris'])
# keys are case sensitive

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")

print()
print("*****  end section 2 ********")
print()





print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook[
    "Chris"
] = "555-0123"  # if given key value pair is there; then value is update
phonebook[
    "Joe"
] = "555-4444"  # if given key value pair is not there; then value is appended

print(phonebook)

print()
print("*****  end section 3 ********")
print()





print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]
print(phonebook)


print()
print("*****  end section 4 ********")
print()




print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

# iterating through key values and items

for key in phonebook:
    print(key)

for key in phonebook:
    print(phonebook[key])

for v in phonebook.values():
    print(v)

for k, v in phonebook.items():
    print(f"the Key: {k} and the value: {v} ")

for ph_tuple in phonebook.items():
    print(ph_tuple)


print()
print("*****  end section 5 ********")
print()





print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get("chris", "key not found") #second line default; can be used as alternative to if/else function
print(phone)

phonebook.clear()
print(phonebook) #clears content of the object, but does not delete the object

print()
print("*****  end section 6 ********")
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#removing key value pair from the dictionary with pop method; can be used to temporarily process materials

remove = phonebook.pop('Chris','not found')
print(remove)
print(phonebook)




print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)
print(phonebook)
#random part of pop item not working




print()
print('*****  end section 8 ********')
print()
"""


print()
print("*****  start section 9 - using random and converting to list ********")
print()

# list_of_keys = list(phonebook)
list_of_keys = random.choice(list(phonebook))
# random.choice specifically used for a list
# random_key = random.choice(list_of_keys)
# print(random_key)
# print(phonebook[random_key])

print(list_of_keys)

print(phonebook[random.choice(list(phonebook))])

print()
print("*****  end section 9 ********")
print()
