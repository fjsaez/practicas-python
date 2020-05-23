print('')
print('Prueba de cadenas en Python')
print('')

# cadenas:
Variable = 'hola mundo'
# concatenación:
print('Mi frase es: ' + Variable)
print(f'Mi frase es: {Variable}')
print('Mi frase es: {0}'.format(Variable))

print(Variable.upper())
print(Variable.lower())
print(Variable.swapcase())
print(Variable.capitalize())
print(Variable.replace('Hola','Chao'))
print(Variable.count('o'))
print(Variable.startswith('h'))
print(Variable.endswith('mundx'))
print(Variable.split(' '))
print(Variable.find('n'))
print(len(Variable))
print(Variable.index('a'))
print(Variable.isnumeric())
print('')