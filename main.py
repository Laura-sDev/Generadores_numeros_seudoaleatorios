from PruebasIndependencia import *
from PruebasUnformidad import *
from MiGenerador import *

def main(a=0,c=0,m=0,x0=0,generator='GLC',activar_chiCuadrado=True, activar_kolmogorov=True, activar_corridas=True, activar_series=True, activar_poker=True):
    
    if a<0 or c<0 or m<0 or x0<0 :
        print('------------------------------------------------------------ \n \n Rodas por favor, ¿Ese valor como va a ser negativo? !!! \n \n ------------------------------------------------------------ ')
        return 0
    
    RELACION=[]
    FRECUENCIA=[]
    SECUENCIA=[] #lo del generador hasta la semilla 
    if generator == 'GLC':
        print('entro en GLC')
        SECUENCIA, FRECUENCIA, RELACION = GLC(a,c,m,x0)
    elif generator == 'GEM': 
        print('entro en GEM')
        SECUENCIA, FRECUENCIA, RELACION = GEM(a,m,x0)
    elif generator == 'GPY':
        SECUENCIA, FRECUENCIA, RELACION = GPY(m)
    else:
        print('error: El generador solo soporta "GLC" "GEM" "GPY"')
        return 
    if len(RELACION):
        if activar_chiCuadrado:
            PCC(SECUENCIA,FRECUENCIA)
        if activar_kolmogorov:
            kolmogorov(SECUENCIA,FRECUENCIA)
        if activar_corridas:
            corridas(RELACION)
        if activar_series:
            series(RELACION)
        if activar_poker:
            poker(RELACION,3)
            poker(RELACION,5)
    else: print('generador retorno lista vacia')

#main(a=255, generator='GLC', c=100,m=10033,x0=5,activar_chiCuadrado=False, activar_kolmogorov=False, activar_corridas=False, activar_series=False)
#main(a=255, generator='GEM', c=100,m=1033,x0=5,activar_chiCuadrado=False, activar_kolmogorov=False, activar_corridas=False, activar_series=False)
#main(a=255, generator='GEM', c=100,m=1033,x0=5)
main(a=23, generator='GLC', c=1000,m=10033,x0=5)
#main(m = 500,generator='GPY',activar_chiCuadrado=False, activar_kolmogorov=False, activar_corridas=False, activar_series=False)
#main(m = 5000,generator='GPY')