lst = [
    "Elvin",
    "Ola",
    "Pushkar",
    "Elvin",
    "Ola",
    "Can",
]

my_dict = {}

for name in lst:
    if name in my_dict:
        my_dict[name] += 1
    else:
        my_dict[name] = 1
print(my_dict)