#---Ejemplo 1
try:
    n = int(input('Introducí un número: '))
    5/n
#Evita que salga el mensaje de error para los distintos casos
except ZeroDivisionError as e: 
    print('No se puede dividir por cero.')
except ValueError:
    print('Tiene que ingresar un número válido.')
finally:
    print('Terminó la ejecución.')

#---Ejemplo 2
print('Empezó bien')
try:
    dividendo = 5
    divisor = 0
    res = dividendo/divisor
except ValueError:
    print('Hubo un error')
print('Terminó todo bien!')

#---Ejemplo 3
raise Exception('Hola') #Hace una excepción a mano

#---Ejemplo 4
#Cuando lo que está adentro evalúa falso tira error
assert(False) 
#Sirve para testear
assert(3>5)

def multiplicarPorDos(n):
    return n * 2
try:
    assert(multiplicarPorDos(3) == 6)
except AssertionError:
    print('Hubo un error en los test')
