# Python's zip function wraps two or more iterators with a lazy generator
# Zip consumes the iterator it wraps one item at a time, which means it can be used with infinitely long inputs

# Example
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

longest_name = None
max_count = 0

# with enumerate(a bit noisy)
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(f'Longest name is {longest_name}')

# with zip
longest_name = None
max_count = 0
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(f'Longest name is {longest_name}')

# We can iterate more than two list in parallel
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

# One thing to notice : The iterator stops when the shortest input iterable is exhausted.
names.append("Bill")
for name, count in zip(names, counts):
    print(f'{name} : {count}') # Bill will not be printed