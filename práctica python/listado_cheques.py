import sys 
import csv
from datetime import datetime
#Los argumentos van a estar en sys.argv

#El orden de los argumentos son los siguientes:
#a. Nombre del archivo csv.
#b. DNI del cliente donde se filtrarán.
#c. Salida: PANTALLA o CSV.
#d. Tipo de cheque: EMITIDO o DEPOSITADO.
#e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
#f. Rango de fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)

#Todos estos datos se obtienen del archivo .csv
#Antes de los parámetros está el nombre del archivo sys.argv[0]
parametros = sys.argv[1:] #Es como hacer un slice
nombre_archivo_csv = parametros[0]
dni_a_filtrar = parametros[1]
salida = parametros[2]
tipo_cheque_a_filtrar = parametros[3]
estado_a_filtrar = None
rango_fecha = None

if len(parametros) == 5:
    #Mandaron 1 parámetro opcional, ¿cuál de los dos? Revisarlo manualmente.
    opcional = parametros[4]
    tipos_de_estado = ['PENDIENTE', 'APROBADO', 'RECHAZADO']
    if opcional in tipos_de_estado:
        estado_a_filtrar = opcional
    else:
        rango_fecha = opcional.split(':')
        rango_fecha_inicio = datetime.timestamp(datetime.strtime(rango_fecha[0], '%d-%m-%Y'))
        rango_fecha_fin = datetime.timestamp(datetime.strtime(rango_fecha[1], '%d-%m-%Y'))
elif len(parametros) == 6:
    #Mandaron 2 parámetros opcionales.
    estado_a_filtrar = parametros[4]
    #'20-11-2022:25-12-2022' => ['20-12-2022', '25-12-2022']
    rango_fecha = parametros[5].split(':')
    if rango_fecha:
        rango_fecha_inicio = datetime.timestamp(datetime.strtime(rango_fecha[0], '%d-%m-%Y'))
        rango_fecha_fin = datetime.timestamp(datetime.strtime(rango_fecha[1], '%d-%m-%Y'))

#Mientras el archivo csv esté abierto (para no abrilo y cerrarlo manualmente)
res = []
#Este sería el código del filtrado
with open(nombre_archivo_csv, 'r') as archivo_csv:
    csv_reader = csv.reader(archivo_csv, delimiter=',')
    res.append(next(csv_reader, None))
    for fila in csv_reader:
        dni = fila[8]
        tipo_cheque = fila[9]
        estado_cheque = fila[10]
        fecha = float(fila[6]) #Usa fecha de origen
        if dni != dni_a_filtrar and tipo_cheque != tipo_cheque_a_filtrar:
            continue #No corre lo que viene después
        if estado_a_filtrar and estado_cheque != estado_a_filtrar:
            continue
        if rango_fecha and (fecha < rango_fecha_inicio or fecha > rango_fecha_fin):
            continue
        res.append(fila)

#No se puede repetir combinación de mismo DNI, NUMERO_CUENTA y NRO_CHEQUE
vistos = set()
for nro_fila, fila in enumerate(res):
    nro_cheque = fila[0]
    nro_cuenta = fila[3]
    dni = fila[8]
    if (nro_cheque, nro_cuenta, dni) in vistos:
        #fstrings sirve para colocar variables o valores dentro de comillas
        res.append(f'Hay inconsistencia en la fila {nro_fila}') 
    else:
        vistos.add(nro_cheque, nro_cuenta, dni)

if salida == 'PANTALLA':
    for fila in res:
        #fila = ['hola', 'cheque', 'como', 'va']
        #','.join(fila) => 'hola,cheque,como,va'
        print(','.join(fila))
        #print(fila) es otra opción
elif salida == 'CSV':
    #List Comprehension
    #lista = [1, 2, 3, 4]
    #lista_nueva = [element * 2 for element in lista] = [2, 4, 6, 8]
    datos_filtrados = [[fila[3], fila[5], fila[6], fila[7]] for fila in res]
    dt = datetime.now()
    dt = dt.strftime('%d-%m-%Y')
    with open(f'{fila[8]}-{dt}.csv', 'w', newline='') as archivo_salida:
        writer = csv.writer(archivo_salida)
        writer.writerows(datos_filtrados) 
        #Si pongo res en vez de datos_filtrados me imprime la lista con comas
        