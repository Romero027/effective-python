# Python has built-in sorting method
numbers = [81, 23, 123, 1, 41]
numbers.sort()
print(numbers)

# However, it only works for most built-in types
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name}, {self.weight})'


tools = [
    Tool('level', 3),
    Tool('hammer', 4),
    Tool('screwdriver', 2),
    Tool('chisel', 1),
]

#tools.sort() # Error!

# To support sorting customized types, sort function accepts a key function
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted ', tools)

# key function can also be used to do transformations on the values before sorting
places = ['home', 'New york', 'Paris', 'work']
places.sort()
print('case sensitive ', places)
places.sort(key=lambda x: x.lower())
print('case insensitive ', places)

# TO use multiple criteria for sorting, The simplest solution is to use the tuple type
# Tuple are comparable by default and have a natural ordering
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

# If you want to sort multiple criteria in different direction, you can sort it twice(python's sort is stable) or use unary negation