# To modify a list all we need is the index of the elemet and just announce its value.

bicycle = ['kross', 'hero', 'rodeo', 'firefox']

bicycle[0] = 'trek'

print(bicycle[0])       #the first element of the `bicycle` list is changed with the new value we assigned.
print(bicycle)

# Adding new element to the list without deleting any other element.
# To do that we can use the `append` method.

bicycle.append('kross')         # It will add `kross` at the end of the list.
print(bicycle)

# Insertion of a new element in a list, it is bit different then appending an element in a list as this method gives us the flexibility of adding the new element at any position in the list unlike of append in end.

bicycle.insert(1, 'bmw')
print(bicycle)

# Removing an element from a list is easy, we can just use `del`.

del bicycle[0]          # This will delete the element placed at index 0 to be removed from the list.
print(bicycle)


# If we wanrt to use the removed value then we can use `pop` method.

popped_bicycle = bicycle.pop()          # This will remove the last element of the list, and it will also store that value in the var.

print(popped_bicycle)
print(bicycle)

# We can also use `pop` method to remove the element from any position in the list.

popped_bicycle = bicycle.pop(1)

print(popped_bicycle)
print(bicycle)

# There is one another method we can also remove an element by it's value by using `remove` method.

luxury_bicycle = 'bmw'
bicycle.remove(luxury_bicycle)          # This method removes the element when it firsts encounter it and stops after that.

print(bicycle)
