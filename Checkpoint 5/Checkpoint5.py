#1

for i in range(5):
    print(i)
#2

def suma(a, b, c):
    return a + b + c

resultado = suma(2, 3, 4)
print(resultado)

#3

suma_lambda = lambda a, b, c: a + b + c

resultado = suma_lambda(2, 3, 4)
print(resultado)

#4
nombre = 'Enrique'

lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombre:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")
