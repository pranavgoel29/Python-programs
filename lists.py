# List is a collection of items in perticular order.
# We can put anything in a list we want, not perticularly related with each other either.

# We can take example of different bicycle companies.

bicycle = ['kross', 'hero', 'rodeo', 'firefox']
print(bicycle)              # If we print list this way it will print it with the square brackets and we don't want that.
                            # To avoid that we can access a perticular element at a time.

print(bicycle[0])           # In lists the first element is placed at position `0`
                            # As these are the bicycle company names they should have first letter capital, to do that we can use `title` method here.

print(bicycle[0].title())

# There is one other we should keep in mind is that when we print the element at position `-1` it will print the `last` element of the list.

print(bicycle[-1].title())
