"""Constructing a dictionary."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# add a key, value pair
ice_cream["mint"] = 3

# remove a key, value pair
ice_cream.pop("mint")

# accessing a value
print(ice_cream["chocolate"])

# modifying a value
ice_cream["vanilla"] = 10

# length of a dictionary
print(len(ice_cream))

# check if key in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

# using a for loop with a dictionary to print keys
for key in ice_cream:
    print(key)

# using a for loop with a dictionary to print
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

print(ice_cream)