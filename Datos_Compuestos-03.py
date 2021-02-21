"""
3.- Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
mayor.

"""
loteria = []
cont = 1
print("Ingresa los numero de la loteria (entre 1 y 49)")

while cont < 7:
    n = int(input((f"Ingresa numero {cont}: ")))
    while n < 0 or n > 49:
        print("Lo sentimos, pero ese no es un numero valido, ingresa otro")
        n = int(input((f"Ingresa numero {cont}: ")))
        loteria.append(n)
        cont += 1
    else:
        loteria.append(n)
        cont += 1

print("Los numero de la loteria ganadora son: ", sorted(loteria[:]))

"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas.
"""
#Lista del 1 al 10
import random
c = 1
ejemplo = []
while c <11:
    ejemplo.append(c)
    c += 1
"""
for i in range (10):
    ejemplo.append(random.randint(1,10))"""

print("Numeros Normal: ", ejemplo[:])
ejemplo.reverse()
print("Numeros al Reves: ", ejemplo[:]) 