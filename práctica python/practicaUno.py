# EJERCICIO 1
# Dado un número entero n, realiza las siguientes acciones condicionales:
# - Si n es impar, imprime "Weird".
# - Si n es par y está en el rango inclusivo de 2 a 5 , imprima "Not Weird".
# - Si n es par y está en el rango inclusivo de 6 a 20 , imprima "Not Weird".
# - Si n es par y mayor que 20 , imprima "Not Weird".
# Formato de entrada: una sola línea que contiene un entero positivo.
# Restricciones: n entre 1 y 100.
# Formato de salida: imprima "Weird" si el número es raro. De lo contrario, imprima "Not Weird".

def numerosLocos():
    
    n = int(input("Ingresar un número entero entre 1 y 100: "))
    if (n >= 1) and (n <= 100):
        if (n % 2) != 0:
            print("Weird")
        elif (n % 2) == 0:
            if (n >= 2) and (n <= 5):
                print("Not Weird")
            elif (n >= 6) and (n <= 20):
                print("Not Weird")
            elif (n > 20):
                print("Not Weird")
        else:
                print("Weird")
    else:
        print("Weird")

#numerosLocos()

# -----------------------------------------------------------------------------------------------------
# EJERCICIO 2
# Ingresando dos números enteros por pantalla a y b . Agregue código para imprimir tres líneas donde:
# - La primera línea contiene la suma de los dos números.
# - La segunda línea contiene la diferencia de los dos números (primero - segundo).
# - La tercera línea contiene el producto de los dos números.
# Formato de entrada:
# - La primer linea contiene el primer entero a.
# - La segunda linea contiene el segundo entero b.
# Restricciones:
# - a entre 1 y 10000000.
# - b entre 1 y 10000000.
# Formato de salida: imprimir las 3 lineas citadas en el ejercicio.

def operacionesDosNumeros():

    a = int(input("Un número entre uno y diez millones: "))
    b = int(input("Otro número entre uno y diez millones: "))

    if (a >= 1 and a <= 10000000) and (b >= 1 and b <= 10000000):
        print("La suma de ambos números es: ", a + b)
        print("El primero menos el segundo da: ", a - b)
        print("El producto entre a y b es: ", a * b)
    else:
        print("MIRÁ BIEN LOS NÚMEROS")

#operacionesDosNumeros()

# ------------------------------------------------------------------------------------------------
# Ejercicio 3
# Ingresando un numero entero n por pantalla. Para todos los numero enteros no negativos i < n, imprimir i**2.
# Ejemplo:
# n=3 La lista de números enteros positivos que son menor que n es: n=3 es [0,1,2]. 
# Imprimir la secuencia con lineas separadas

# 0

# 1

# 2

# Formato de entrada: la primer y unica linea contiene el primer entero n.
# Restricciones: n entre 1 y 20.
# Formato de salida: imprimir las n lineas una correspondiente a cada i.

def enterosPositivos():

    n = int(input('Ingresar un número entero entre 1 y 20: '))
    listaNumeros = []

    if (n >= 1) and (n <= 20):
        i = 0
        while i < n:
            listaNumeros.append(i)
            i += 1

    for i in range(len(listaNumeros)):
        print(listaNumeros[i], end = '\n' + '\n')

#enterosPositivos()
