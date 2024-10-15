import math
'''

Exercicio7.5. Dada unha lista de números enteiros, escribir unha función que:
Devolte unha lista con tódolos que sexan primos.
Devolte a sumatoria e o promedio dos valores.
Devuelva unha lista co factorial de cada un desos números.

'''

def es_primo(n):
    try:
        if n == 0 or n == 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                return False
    except ValueError:
        print("Numero negativo: " + str(n))
        return False
    return True

def dame_lista_primos(lista):
    lista_primos = []
    for i in range(len(lista)):
        if es_primo(lista[i]):
            lista_primos.append(lista[i])
    return lista_primos

introduce_lista = [1,10,-23,24,65,47,82,9,53,127,823,50,-7]
print(dame_lista_primos(introduce_lista))

#--------------------------------------------------X----------------------------------------------------#

def suma_promedio(lista):
    suma = 0
    promedio = 0
    contador = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        contador = contador + 1

    promedio = suma / contador
    return "La suma es: " + str(suma) + "\ny el promedio: " + str(promedio)

introduce_lista2 = [1,10,23,24,65,47,82,9]
print(suma_promedio(introduce_lista2))

#--------------------------------------------------------X---------------------------------------------------

def factorial(n):
    try:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
    except RecursionError:
        return 0

def lista_factorial(lista):
    for i in range(len(lista)):
        lista[i] = factorial(lista[i])
    return lista

introduce_lista3 = [4,5,3,10,-1,7,-2]
print(lista_factorial(introduce_lista3))

#----------------------------------------------------------X-------------------------------------------------------------
'''
. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre, dni) y 
devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.
'''

class NotDniException(Exception):
    def __str__(self):
        return "Este dni no es legal, vete a tu país"



def comprueba_numeros(cadena):
    for i in cadena:
        if not i.isdigit():
            return False
    return True

def comprueba_longitud(cadena):
    if len(cadena) != 9:
        return False
    return True

def comprueba_ultima_letra(cadena):
    if cadena.isalpha():
        return True
    return False


def recibe_lista_tuplas(tupla):
    if len(tupla) > 3:
        dni = tupla[3]
        if not comprueba_numeros(dni[0:8]):
            raise NotDniException()

        if not comprueba_longitud(dni):
            raise NotDniException()

        if not comprueba_ultima_letra(dni[8:9]):
            raise NotDniException()
    nueva_lista = [tupla[1], tupla[2] + ".", tupla[0], tupla[3]]
    return nueva_lista

try:
    tupla_ejemplo = ('Rodriguez', 'Florentino', 'P', '12345678K')
    print(recibe_lista_tuplas(tupla_ejemplo))
except NotDniException as e:
    print(e)