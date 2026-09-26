
details={"name":"Ramdhan","age":78, "Branch":"IT"}
print(details)

# details["age"]=88
# print(details)##changing value in the dictionary

# details["Branch"]="Computer Science"
# print(details)

# details["state"]="Jharkhand"
# print(details)## adding new value in the list

# print(details["name"])
# print(details["state"])##printing details with help of key value

#deleting value from the dictionary
# del details["age"]
# print(details)

# del details["Branch"]
# print(details)

# print(details.keys())
# print(details.values())
# print(details.items())

#dictionary in loop

for key, value in details.items():
    print(key,":", value)
