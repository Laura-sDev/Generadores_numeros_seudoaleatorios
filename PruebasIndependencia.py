# Librerias
import math
from prettytable import PrettyTable

# Variables corridas
listaS = list()
listaA = list()

# Variables series
listaPares = list()
FOseries = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
listaSeries = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]

# Variables poker
listaXcalc = list()
digitos = list()
# ---------- 3 ----------
categiras_3 = [0]*3
secuenciaTresCifras = list()
# ---------- 5 ----------
listaDigitos = list()
listaCantidad = list()
listaCasos = list()
categorias = [0]*7

# Corridas
def corridas(secuencia):
    #cabecera tabla 
    t = PrettyTable (['N° Corrida','Longitud','Creciente o decreciente'])

    a = 0
    valorEsperado,varianza = 0,0
    rangoIndependencia = 1.96
    contadorAuxnumcorrida=0
    contadorAuxRango=0
    #listaLongitudCorridas=list()
    for i in range(len(secuencia)-1):
        if secuencia[i] < secuencia[i+1]:
            listaS.append(1)
        else:
            listaS.append(0)
    
    for j in range(len(listaS)-1):
        a  = abs(listaS[j+1]-listaS[j])
        listaA.append(a) #cada 1 generado representa una corrida

        #para longitud de cada corrida en la tabla
        if a == 0:
            contadorAuxnumcorrida+=1
        else:  
            contadorAuxRango+=1
            if listaS[j]==1:
                auxSigno='+'
            else: auxSigno='-'
            t.add_row([contadorAuxRango, contadorAuxnumcorrida+1,auxSigno])
            contadorAuxnumcorrida=0

    
    valorEsperado = (2*(len(secuencia))-1)/3
    varianza = (16*(len(secuencia))-29)/90
    Z = round(abs((sum(listaA)-valorEsperado)/math.sqrt(varianza)),5)

    print('--------------------------------- PRUEBA INDEPENDENCIA: * CORRIDAS * -------------------------------------\n' ) 
    print('Numero de Corridas: ', sum(listaA))
    if Z < rangoIndependencia:
        print("PASA LA PRUEBA: No hay evidencia para rechazar la hipotesis de independencia, el valor calculado se encuentra dentro del rango")
        print('Valor calculado:', Z)
        print('valor critico:',  rangoIndependencia, '\n')

    else: 
        print("NO PASA LA PRUEBA: Se rechaza la hipotesis de independencia, el valor calculado no se encuentra dentro del rango")
        print('Valor calculado:', Z)
        print('valor critico:',  rangoIndependencia, '\n')
    print('++++++++++++++++++++++++++++ Comportamiento crecimiento - decrecimiento corridas ++++++++++++++++++++++\n')

    print('(*)',end=" ")
    for x in range(1,len(listaS)):
        if listaS[x]==1:
            print('+',end=" ")
        else: print('-',end=" ")
    print('\n')
    #print(t, '\n') #Esa es la tabla que muestra la longitud de cada corrida y es extremadamente largo, que pereza

# Series
def series(secuencia):
    #creacion de las cabeceras de las tablas
    listaValoresRango=('','0 - 0.2 ','0.2 - 0.4', '0.4 - 0.6', '0.6 - 0.8', '0.8 - 1')
    tablaFO = PrettyTable (listaValoresRango)
    tablaChicuadrado = PrettyTable (listaValoresRango)
    tablaFE= PrettyTable (listaValoresRango)
    
    count = 0
    Xcritico = 36.42
    Xcalc = 0
    
    for _ in range(len(secuencia)-1):
        if count < (len(secuencia)-1):
            listaPares.append([secuencia[count],secuencia[count+1]])
            count+=2
    
    for i in range(len(listaPares)):  
        for j in range(5): 
            r = j*0.2
            if listaPares[i][0] < r+0.2:
                if listaPares[i][1] < 0.2:
                    FOseries[j][0] += 1
                    break
                elif listaPares[i][1] < 0.4:
                    FOseries[j][1] += 1
                    break
                elif listaPares[i][1] < 0.6:
                    FOseries[j][2] += 1
                    break
                elif listaPares[i][1] < 0.8:
                    FOseries[j][3] += 1
                    break
                elif listaPares[i][1] < 1:
                    FOseries[j][4] += 1
                    break

    FE = (len(secuencia)/2) / 25
    #print(FE)

    contadorAuxrango=1
    for i in range(len(FOseries)):
        rowAux = []
        rowAux2=[]
        rowAux.append(listaValoresRango[contadorAuxrango])
        rowAux2.append(listaValoresRango[contadorAuxrango])
        for j in range(len(FOseries)):
            chiCuadrado = round((FE - FOseries[i][j])**2 / FE,5)
            listaSeries[i][j] = chiCuadrado
            Xcalc += listaSeries[i][j]

            #Pa llanar las filas de las tablas 
            rowAux.append(FOseries[i][j])
            rowAux2.append(listaSeries[i][j])
        
        tablaFO.add_row(rowAux)
        tablaChicuadrado.add_row(rowAux2)
        tablaFE.add_row([listaValoresRango[contadorAuxrango], FE, FE, FE, FE, FE])
        
        contadorAuxrango+=1

    
    print('---------------------- PRUEBA INDEPENDENCIA: * SERIES * --------------------------------\n' )     
    if Xcalc <= Xcritico:
        print("PASA LA PRUEBA: No hay evidencia para rechazar la hipotesis de independencia, el valor calculado es menor o igual al valor critico")
        print('Valor calculado:', Xcalc)
        print('valor critico:',  Xcritico, '\n')
    else: 
        print("NO PASA LA PRUEBA: Se rechaza la hipotesis de independencia, el valor calculado es mayor al valor calculado")
        print('Valor calculado:', Xcalc)
        print('valor critico:',  Xcritico, '\n')

    print('++++++++++++++++++++++++++++++ Tabla FO ++++++++++++++++++++++++++++++++ \n')
    print(tablaFO,'\n')
    print('++++++++++++++++++++++++++++++ Tabla Chicuadrado ++++++++++++++++++++++++\n')
    print(tablaChicuadrado,'\n')
    print('++++++++++++++++++++++++++++++ Tabla FE +++++++++++++++++++++++++++++++++\n')
    print(tablaFE,'\n')

# Poker
def poker(secuencia,decimales):
    t = PrettyTable (['Rangos','FO ','FE', '|FE-FO|'])
    listaCasosP5=('TD','1P','2P','TP','T','P','Q')
    listaCasosP3=('TD','1P','T')
    #poker 3 ----------------------------------------------------
    if decimales == 3:
        for i in range(len(secuencia)):
            tresCifras = round(secuencia[i],3)
            secuenciaTresCifras.append(tresCifras)
            numero = str(secuenciaTresCifras[i])
            
            if numero < '1':
                numeroDec = numero.replace('0.','') 
            else: numeroDec = numero.replace('1.','')

            if len(numeroDec) == 1: 
                numeroDec = numeroDec + '0' + '0'
            elif len(numeroDec) == 2:
                numeroDec = numeroDec + '0'
        
            digitos = [int(i) for i in str(numeroDec)]

            if digitos[0] != digitos[1] and digitos[0] != digitos[2] and digitos[1] != digitos[2]:
                categiras_3[0] += 1
            elif digitos[0] == digitos[1] and digitos[0] == digitos[2]:
                categiras_3[2] += 1
            elif digitos[0] == digitos[1] or digitos[0] == digitos[2] or digitos[1] == digitos[2]:
                categiras_3[1] += 1
        
        s = len(secuencia)
        FO = categiras_3
        FE = [round(0.72*s,3), round(0.27*s,3), round(0.1*s,3)]
        Xcalc = 0
        Xcritico = 5.99

        for i in range(len(FO)):
            Xcalc = round(((FO[i]-FE[i])**2)/FE[i], 5)
            listaXcalc.append(Xcalc)
        
        for i in range(len(FO)):
            t.add_row([listaCasosP3[i], FO[i], FE[i], listaXcalc[i]])
        
        print('---------------------- PRUEBA INDEPENDENCIA: * POKER 3 * --------------------------------\n' )
        if sum(listaXcalc) <= Xcritico:
            print("PASA LA PRUEBA: se acepta la hipótesis que los datos tienen una independencia, el valor calculado es menor o gual al valor crítico")
            print('Valor calculado:', sum(listaXcalc))
            print('valor critico:',  Xcritico, '\n')
        else:
            print("NO PASA LA PRUEBA: No se acepta la hipótesis que los datos tienen una independencia, el valor calculado es mayor valor crítico")
            print('Valor calculado:', sum(listaXcalc))
            print('valor critico:',  Xcritico, '\n')
        #print(FO)
        #print(FE)
        #print(listaXcalc)
        print(t,'\n')

        #poker 5-------------------------------------------------------
    elif decimales == 5:
        for i in range(len(secuencia)):
            numero = str(secuencia[i])

            if numero < '1':
                numeroDec = numero.replace('0.','') 
            else: 
                numeroDec = numero.replace('1.','')
            
            if len(numeroDec) == 1: 
                numeroDec = numeroDec + '0' + '0' + '0' + '0'
            elif len(numeroDec) == 2: 
                numeroDec = numeroDec + '0' + '0' + '0'
            elif len(numeroDec) == 3: 
                numeroDec = numeroDec + '0' + '0'
            elif len(numeroDec) == 4:
                numeroDec = numeroDec + '0'
        
            digitos = [int(i) for i in str(numeroDec)] 
            listaDigitos.append(digitos)
            
        for _ in range(len(secuencia)):
            cantidad = [0]*10
            casos = [0]*5
            listaCantidad.append(cantidad)
            listaCasos.append(casos)

        for i in range(len(listaDigitos)):
            for j in range(5):
                if listaDigitos[i][j] == 0:   listaCantidad[i][0] += 1
                elif listaDigitos[i][j] == 1: listaCantidad[i][1] += 1
                elif listaDigitos[i][j] == 2: listaCantidad[i][2] += 1
                elif listaDigitos[i][j] == 3: listaCantidad[i][3] += 1
                elif listaDigitos[i][j] == 4: listaCantidad[i][4] += 1
                elif listaDigitos[i][j] == 5: listaCantidad[i][5] += 1
                elif listaDigitos[i][j] == 6: listaCantidad[i][6] += 1
                elif listaDigitos[i][j] == 7: listaCantidad[i][7] += 1
                elif listaDigitos[i][j] == 8: listaCantidad[i][8] += 1
                elif listaDigitos[i][j] == 9: listaCantidad[i][9] += 1
        
        for i in range(len(listaCantidad)):
            for j in range(10):
                if listaCantidad[i][j] == 1:   listaCasos[i][0] += 1
                elif listaCantidad[i][j] == 2: listaCasos[i][1] += 1
                elif listaCantidad[i][j] == 3: listaCasos[i][2] += 1
                elif listaCantidad[i][j] == 4: listaCasos[i][3] += 1
                elif listaCantidad[i][j] == 5: listaCasos[i][4] += 1

        for i in range(len(listaCasos)):
            if listaCasos[i][0] == 5:   categorias[0] += 1
            elif listaCasos[i][2] == 1 and listaCasos[i][1] == 1: 
                                        categorias[3] += 1
            elif listaCasos[i][1] == 1: categorias[1] += 1
            elif listaCasos[i][1] == 2: categorias[2] += 1
            elif listaCasos[i][2] == 1: categorias[4] += 1
            elif listaCasos[i][3] == 1: categorias[5] += 1
            elif listaCasos[i][4] == 1: categorias[6] += 1

        FO = categorias
        l = len(secuencia)
        FE = [round(0.3024*l,3), round(0.504*l,3), round(0.108*l,3),round(0.009*l,3),round(0.072*l,3),round(0.0045*l,3),round(0.0001*l,3)]
        Xcalc = 0
        Xcritico = 12.59

        for i in range(len(FO)):
            Xcalc = round(((FO[i]-FE[i])**2)/FE[i], 5)
            listaXcalc.append(Xcalc)
        
        for i in range(len(FO)):
            t.add_row([listaCasosP5[i], FO[i], FE[i], listaXcalc[i]])
        
        print('---------------------- PRUEBA INDEPENDENCIA: * POKER 5 * --------------------------------\n' )
        if sum(listaXcalc) <= Xcritico:
            print("PASA LA PRUEBA: se acepta la hipótesis que los datos tienen una independencia, el valor calculado es menor o gual al valor crítico")
            print('Valor calculado:', sum(listaXcalc))
            print('valor critico:',  Xcritico, '\n')
        else:
            print("NO PASA LA PRUEBA: No se acepta la hipótesis que los datos tienen una independencia, el valor calculado es mayor valor crítico")
            print('Valor calculado:', sum(listaXcalc))
            print('valor critico:',  Xcritico, '\n')
     
        print(t,'\n')
    else: print("Elija entre 3 o 5 decimales")