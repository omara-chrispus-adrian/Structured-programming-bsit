## list operations
girl = ['sarah', 'winnie', 'imie']
print(f"original: {girl}")
girl[0] = "Sarafinah"
girl.insert(1, "Juliet")
print(f"Changed and added :{girl}")
#girl.pop()# deleting the last item
print(f"Delete last girl:{girl}")
girl.remove("Juliet")
print(f"Removed Juliet:{girl}")

##READING THE NAMES
for g in girl:
    print(g)

##LIST SLICING
print(girl[1:4])

#nested lists
[
    [1,12,3],
    [4,5,6]
]