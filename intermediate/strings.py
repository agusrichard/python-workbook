my_string = 'Sekardayu Hana Pradiani'

# Indexing string
print(my_string)
print(my_string[0])
print(my_string[1:5])
print(my_string[::-1])

#  Concatenating string
new_string = my_string + ' loves me'
print(new_string)

# In statement
print('a' in my_string)
print('agus' in my_string)

# Stripping whitespaces
my_string = '    ' + my_string + '    '
print(my_string)
print(my_string.strip())

# upper and lower method
my_string = my_string.strip()
print(my_string.upper())
print(my_string.lower())

# Startswith and endswith
print(my_string.startswith('Sekar'))
print(my_string.endswith('agus'))

# Find method
print(my_string.find('Sekar'))
print(my_string.find('agus'))

# Replace method
print(my_string.replace('Sekardayu', 'Saskia'))

# Split method
print(my_string.split(' '))

# Join method
new_list = my_string.split(' ')
new_string = ' '.join(new_list)
print(new_string)

# String formatting
name = 'Agus Richard Lubis'
print('Sekardayu Hana Pradiani loves %s' % 'me')
print('Sekardayu Hana Pradiani loves {}'.format('me'))