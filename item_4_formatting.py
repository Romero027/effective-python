# Interpolated Format Strings(Iterpolated F-strings)

key = 'my_var'
value = 1.234

formatted_1 = f'{key} = {value}' # prefix the formatted strings wth an f character
print(formatted_1)

formatted_2 = f'{key!r:<10} = {value:.2f}' # Format string after the colon in the placeholders within an f-string
print(formatted_2)

pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]

for i, (item, count) in enumerate(pantry):
    c_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)
    )

    # F-string also enable you to put a full python expression within the place holder braces
    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}' 

    assert c_style == f_string


places = 3    
number = 1.23456
# Python expressions may also appear within the format specifier option
print(f'My number is {number:.{places}f}')

    