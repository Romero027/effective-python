# Unpacking allows for assigning multiple values in a single statement

item = ('apple', 'banana')
a, b = item
print(a, 'and', b)

# Unpacking can even be used to swap values in place
# Python will create an implicit temp value for you
x = 1 
y = 2
x, y = y, x 
print('x =', x, 'and y =', y)

# It is also useful in for loops and similar constructs
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
# Iterate without unpacking
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} has {calories} calories')

print()

for i, (name, calories) in enumerate(snacks, 1): # 1 tells enumerate to start from 1 instead of 0
    print(f'#{i}: {name} has {calories} calories')
