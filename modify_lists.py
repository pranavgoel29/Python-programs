# To modify a list all we need is the index of the elemet and just announce its value.

bicycle = ['kross', 'hero', 'rodeo', 'firefox']

bicycle[0] = 'trek'

print(bicycle[0])       #the first element of the `bicycle` list is changed with the new value we assigned.
print(bicycle)

# Adding new element to the list without deleting any other element.
# To do that we can use the `append` method.

bicycle.append('kross')         # It will add `kross` at the end of the list.
print(bicycle)


