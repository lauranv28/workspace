def fizz_buzz():
    n = int(input('Ingresar un número entero: '))
    lista = []
    d = 1

    while d <= n:
        if (n % 3) == 0:
            lista.append('Fizz')
            d += 1
        elif (n % 5) == 0:
            lista.append('Buzz')
        else:
            lista.append(d)
        
        d += 1

    print(lista)

fizz_buzz()