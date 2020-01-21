flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

# without using enumerate
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1} : {flavor}')

print()

# using enumerate
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1} : {flavor}')

print()

# better version
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i} : {flavor}')
