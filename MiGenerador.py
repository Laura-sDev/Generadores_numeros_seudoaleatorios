# Librerias
import math
import random
from PruebasIndependencia import *
from PruebasUnformidad import *
#from tokenize import String

# Variables GLC
secuenciaGLC = list()
relacionSecuenciaGLC = list()
frecuenciaObtenidaGLC = [0]*10

# Variables GEM
secuenciaGEM = list()
relacionSecuenciaGEM = list()
frecuenciaObtenidaGEM = [0]*10

# Variables GPY
secuenciaGPY = list()
frecuenciaObtenidaGPY = [0]*10

# Generador lineal congruente
def GLC(a,c,m,x0):
    xn = x0
    secuenciaGLC.append(x0)
    parada = 0
    while True:
        if (m>0 and (0<a and a<m) and (0<=c and c<m) and (0<=xn and xn<m)):
            relacion = round(xn/m, 5)
            relacionSecuenciaGLC.append(relacion)
            
            posicion = math.floor(relacion*10) 
            if posicion == 10:
                frecuenciaObtenidaGLC[9]+=1
            else:
                frecuenciaObtenidaGLC[posicion] += 1

            xn = (a * xn + c) % m
            secuenciaGLC.append(xn)

            if (xn == x0):
                break

            parada+=1
            if parada == 1000000:
                print("semilla lejos")
                break

        else: break

    print('---------------------- GENERADOR LINEAL CONGRUENTE --------------------------------\n' ) 
    hallarPeriodo(secuenciaGLC)
    print('**************** Secuencia generada ****************************\n')
    print(secuenciaGLC, '\n')

    return secuenciaGLC,frecuenciaObtenidaGLC, relacionSecuenciaGLC

# Generador estadar minimo
def GEM(a,m,x0):
    xn = x0
    secuenciaGEM.append(x0)
    parada = 0
    while True:
        if (0<xn and xn<=m):
            relacion = round(xn/m, 5)
            relacionSecuenciaGEM.append(relacion)
            posicion = math.floor(relacion*10)
            
            if posicion == 10:
                frecuenciaObtenidaGEM[9]+=1
            else:frecuenciaObtenidaGEM[posicion] += 1
            xn = (a * xn) % m

            secuenciaGEM.append(xn)

            if (xn == x0):
                break
            parada+=1
            if parada > m:
                print("semilla lejos")
                break

        else: break

    print('----------------------------------- GENERADOR ESTANDAR MÍNIMO -------------------------------------\n')
    hallarPeriodo(secuenciaGEM)
    print('*********************************** Secuencia generada: **************************************\n')
    print(secuenciaGEM, '\n')

    return secuenciaGEM,frecuenciaObtenidaGEM, relacionSecuenciaGEM

# Generador python
def GPY(m):
    for _ in range(m):
        xn = round(random.uniform(0,1),5)
        if xn < 0.0001:
            xn = 0

        posicion = math.floor(xn*10) 
        if posicion == 10:
            frecuenciaObtenidaGPY[9]+=1
        else:frecuenciaObtenidaGPY[posicion] += 1

        secuenciaGPY.append(xn)

    print('-------------------------------------- GENERADOR DE PYTHON -----------------------------------\n')
    print('\n')
    hallarPeriodo(secuenciaGPY)
    print('***********************************Secuencia generada:**********************************\n')
    print(secuenciaGPY,'\n')

    return secuenciaGPY,frecuenciaObtenidaGPY

#funcion para el periodo
def hallarPeriodo(lista):
    try:
        periodo = lista.index(lista[0],1)
        print("El periodo para este generador es: ", periodo, '\n')
    except ValueError:
        print("¡Oops! No se halla el periodo para la cantidad de datos generada.\n")

#llamadosFunciones

#GLC(106,145,6075,5)

#GEM(106,6075,5)
#GPY(5000)
#corridas(secuenciaGPY)




#kolmogorov(secuenciaGLC,frecuenciaObtenidaGLC)

#PCC(secuenciaGLC,frecuenciaObtenidaGLC)
#PCC(secuenciaGEM, frecuenciaObtenidaGEM)
#print(relacionSecuenciaGLC)

#PCC(secuenciaGLC,frecuenciaObtenidaGLC)
#PCC(secuenciaGEM, frecuenciaObtenidaGEM)
#print(relacionSecuenciaGLC)
#series(relacionSecuenciaGLC)
#poker(relacionSecuenciaGLC,5)
#poker(relacionSecuenciaGLC,3)
#corridas(relacionSecuenciaGLC)

#print(secuenciaGLC)
#GEM(100,6075,10)
#print(relacionSecuenciaGEM)
#print(secuenciaGEM)
