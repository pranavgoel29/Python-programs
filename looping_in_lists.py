# Program to loop through the lists to print their content.
# We will first make a list.

cars = ['mcqueen', 'matter', 'sally']
for car in cars:                        # This line just pull a name from cars list and store them in var `car`.
    print(car)                          # This line just print the value of `car` var that we have declared prevously.
                                        # It run until the very last element of the list is done.

# We can name var anything for example:

for cycle in cars:
    print("\n",cycle)

# We can also use the `title` method here in loop too.
for car in cars:
    print(car.title()+", is a great character.")

