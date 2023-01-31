person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print(person["children"][1])
# mylist = person['children']

# print out the name of the cat
print(person["pets"]["cat"])

# use a loop to print out the names of each child

for child in person["children"]:
    print(child)

# use a loop to print out the pets in the following format:
# the type of pet is: dog and the name of the pet is: Fido

# pets_dict = person["pets"]
# for key, value in pets_dict.items():
# print(key, value)

for key, value in person["pets"].items():
    print(f"the type of pet is: {key} and the name of the pet is {value}")
