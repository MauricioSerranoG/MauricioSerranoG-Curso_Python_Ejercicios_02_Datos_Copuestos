"""
2.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
pantalla.
"""

lista = []
contador = 1
while contador < 8:
    m = input(f"Ingresa materia {contador}: ")
    lista.append(m)
    contador +=1
print("\n")
print("Materias escolares: ", lista[:])


