"""
1.- Realiza una función separar(lista) que tome una lista de números enteros
desordenados y devuelva dos listas ordenadas. La primera con los números pares y la
segunda con los números impares.
"""

lista_desordenada = [10, 3, 5, 2, 6, 9, 4, 1, 8, 7]
lista_pares= []
lsitas_inpares= []


def separar(lista):
    for i in lista_desordenada:
        if i%2 ==0:
            lista_pares.append(i)
        else:
            lsitas_inpares.append(i)
           



print("Lista original: ", lista_desordenada, "\n")
print(lista_desordenada[:])
print("Ordenando...")
separar(lista_desordenada)
print("Lista de pares ordenados: ", sorted(lista_pares[:]), "\n")
print("Lista de inpares odenados: ", sorted(lsitas_inpares[:]))

