#Modulacion por codigo de pulso, ejercicio 9

valido = False

def validar(valor):                            #Funcion para validar dato
    if len(valor) != 4:                        #Revisa la longitud del dato ingresado
        return False                           
    try:                                       #Comprueba si el dato puede ser float para ver si es un numero
        decimal = float(valor)
    except :
        return False
    for i in valor:                            #Comprueba que solo hay 0 o 1 
        if i != "0" and i != "1":
            return False

    return True                                #El dato es correcto

def validar2(valor):                           #Funcion para validar dato en el cambio de bit
    if len(valor) != 1:                        #Revisa la longitud del dato ingresado
        return False                           
    try:                                       #Comprueba si el dato puede ser float para ver si es un numero
        decimal = float(valor)
    except :
        return False
    for i in valor:
        i = int(i)                                        #Comprueba que solo hay 0 o 1 
        if i < 1 or i > 7:
            return False

    return True                                #El dato es correcto

print('Introduzca un valor, por favor: ')



while not valido:                              #bucle para pedir el valor
    Dato = input(str())
    valido = validar(Dato)
    if not valido:
        print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')

print("El valor es valido")                     


A3= int(Dato[0])                               #Se asignan los valores y se transforman a enteros
A2= int(Dato[1])
A1= int(Dato[2])
A0= int(Dato[3])

def xor(a, b, c):                               #Funcion xor para 3 variables
    if ((a and not b) or (not a and b)):        
        xorab = 1
    else:
        xorab = 0
        
    if ((xorab and not c) or (not xorab and c)):
        xorabc = 1
    else:
        xorabc = 0
        
    return xorabc

def xor4(a, b, c, d):                            #Funcion xor para 4 variables
    if ((a and not b) or (not a and b)):        
        xorab = 1
    else:
        xorab = 0
        
    if ((xorab and not c) or (not xorab and c)):
        xorabc = 1
    else:
        xorabc = 0
    if ((xorabc and not d) or (not xorabc and d)):        
        paridad = 1
    else:
        paridad = 0
        
    return paridad


k2 = (xor(A3,A2,A0))
k1 = (xor(A3,A1,A0))
k0 = (xor(A2,A1,A0))


Dato = [k2,k1,A3,k0,A2,A1,A0]
print(Dato)

valido2 = False

print('Introduzca el numero de bit a cambiar por favor: ')

while not valido2:                               #bucle para pedir el valor
    error = input(str())
    valido2 = validar2(error)
    if not valido2:
        print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')

error = int(error)

error = error -1
if Dato[error] == 1:                            #Reemplaza la ubicacion del bit ingresado por teclado
    Dato[error] = 0
else:
    Dato[error] = 1


print(Dato)

k2= int(Dato[0])                                #Se asignan los valores y se transforman a enteros
k1= int(Dato[1])
A3= int(Dato[2])
k0= int(Dato[3])
A2= int(Dato[4])                                #Se asignan los valores y se transforman a enteros
A1= int(Dato[5])
A0= int(Dato[6])

paridad1 = str((xor4(k2,A3,A2,A0)))
paridad2 = str((xor4(k1,A3,A1,A0)))
paridad3 = str((xor4(k0,A2,A1,A0)))

paridadtotal = str(paridad3+paridad2+paridad1)
print("Esta es la paridad armada= ",paridadtotal)

paridadtotal= int(paridadtotal,2)
print("El bit con error es el bit= ",paridadtotal)





