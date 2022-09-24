from PruebasIndependencia import *
from PruebasUnformidad import *
from MiGenerador import *

def main(a=0,c=0,m=0,x0=0,generator='GLC',activar_chiCuadrado=True, activar_kolmogorov=True, activar_corridas=True, activar_series=True, activar_poker=True):
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
        print('Generador no soportado o erroneo')
        return 
    if len(RELACION):
        if activar_chiCuadrado:
            PCC(SECUENCIA,FRECUENCIA)
        if activar_kolmogorov:
            kolmogorov(SECUENCIA,FRECUENCIA)
        if activar_corridas:
            corridas(SECUENCIA)
        if activar_series:
            series(SECUENCIA)
        if activar_poker:
            poker(SECUENCIA,3)
            poker(SECUENCIA,5)
    else: print('generador retorno lista vacia')

#main(a=255, generator='GLC', c=100,m=1033)
#main(a=255, generator='GEM', c=100,m=1033,x0=5,activar_chiCuadrado=False, activar_kolmogorov=False, activar_corridas=False, activar_series=False, activar_poker=False)
