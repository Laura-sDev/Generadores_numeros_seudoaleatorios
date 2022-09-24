# Librerias
import math
from prettytable import PrettyTable
rangos=('0 - 0.1', '0.1 - 0.2', '0.2 - 0.3','0.3 - 0.4','0.4 - 0.5','0.5 - 0.6','0.6 - 0.7','0.7 - 0.8','0.8 - 0.9','0.9 - 1')
# Variables Chi Cuadrado
listaChiCuadrado = list()

# Variables kolmogorov
listaKolmogorov = list()

# Prueba chi cuadrado
def PCC(secuencia,frecuenciaObtenida):
    t = PrettyTable (['Rangos','FO ','FE','(FE-FO)^2/FE'])
    chiCritico = 16.92
    FE = len(secuencia)/10
    rangoaux=0

    for FO in frecuenciaObtenida:
        chiCuadrado = round((FE - FO)**2/FE,5)
        listaChiCuadrado.append(chiCuadrado)
        
        t.add_row([rangos[rangoaux],FO, FE, chiCuadrado])
        rangoaux+=1
    
    print('-------------------------------- PRUEBA CHI CUADRADO ----------------------- \n')
    if sum(listaChiCuadrado) <= chiCritico:
        print("El generador es bueno en cuanto a uniformidad, el valor calculado es menor o igual al critico")
        print('Valor calculado:', sum(listaChiCuadrado))
        print('Chi critico:', chiCritico, '\n')
    else: 
        print("No pasa la prueba Chi cuadrado, se pone en duda su uniformidad el valor calculado es mayor al critico")
        print('Valor calculado:', sum(listaChiCuadrado))
        print('Chi critico:', chiCritico, '\n')
    print(t, '\n')

# Prueba kolmogorov
def kolmogorov(secuencia,frecuenciaObtenida):
    t = PrettyTable (['Rangos','FO ','FOA', 'POA', 'PEA', '|PEA-POA|'])
    DMcritico  = 1.36/math.sqrt(len(secuencia))
    acumulado2 = 0
    FOA = 0
    POA = 0
    PEA = 0
    rangoaux=0
    
    for FO in frecuenciaObtenida:
        FOA += FO
        POA = round((FOA/len(secuencia)),5)
        acumulado2 = round((len(secuencia)/10)/len(secuencia),5)
        PEA += acumulado2
        PEAmenosPOA = round(abs(PEA - POA),5)
        listaKolmogorov.append(PEAmenosPOA)

        t.add_row([rangos[rangoaux],FO,FOA,POA,PEA,PEAmenosPOA])
        rangoaux+=1

    print('------------------------- PRUEBA KOLMOGOROV - SMIRNOV ----------------------------------\n')
    if max(listaKolmogorov) <= DMcritico:
        print("El generador es bueno en cuanto a uniformidad, el valor calculado es menor o igual al critico")
        print('Valor calculado:', max(listaKolmogorov))
        print('DMcritico:', DMcritico, '\n')
    else:
        print("No pasa la prueba kolmogorov, se pone en duda su uniformidad el valor calculado es mayor al critico")
        print('Valor calculado:', max(listaKolmogorov))
        print('DMcritico:', DMcritico, '\n')
    print(t, '\n')
   