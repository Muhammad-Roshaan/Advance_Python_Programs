# Create a dictionary representing a person with keys like name, age, city, etc
person = {
    "name": "John Doe",
    "age": "30",
    "city": "Lahore",
}
print("\nPerson 1: ", person)

# Modify the values of 3rd keys in the dictionary
person["city"] = "Multan"
print("\nModify city: ", person)

# Concatenate two dictionaries
personUpdate = {
    "occupation": "Engineer",
    "hobbies": ["Reading", "Travelling"]
}
print("\n2nd Dictionary: ", personUpdate)
concatenatedDict = {**person, **personUpdate}
print("\nConcatenate Dictionary: ", concatenatedDict)

# Check if a specific key exists in the dictionary
print("\nCheck specific key: ", "occupation" in concatenatedDict)

# Remove the 8th key-value pair from the dictionary
print("\nRemove key: ", personUpdate.pop("hobbies"))
print(personUpdate)