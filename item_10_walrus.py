# Requires python 3.8

# Walrus assignment(a := b) are useful where normal assignment(a = b) is disallowed(e.g., conditional expression of an if statement)
# For example, w/o walrus
a = [1, 2, 3, 4]
length = len(a)
if length > 3: 
    print(f"List is too long ({length} elements, expected <= 3)") 

# With walrus
a = [1, 2, 3, 4] 
if (n := len(a)) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 

# It can also be used to emulate do while



