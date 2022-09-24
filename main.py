from PruebasIndependencia import *
from PruebasUnformidad import *
from MiGenerador import *

def main(a=0,c=0,m=0,x0=0,generator='GLC', chiCuadrado=False, kolmogorov=False, corridas=False, series=False, poker=False):
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
        if chiCuadrado:
            PCC(SECUENCIA,FRECUENCIA)
        elif kolmogorov:
            kolmogorov(SECUENCIA,FRECUENCIA)
        elif corridas:
            corridas(SECUENCIA,FRECUENCIA)
        elif series:
            series(SECUENCIA)
        elif poker:
            poker(SECUENCIA,3)
            poker(SECUENCIA,5)
    else: print('generador retorno lista vacia')

main(a=255, generator='GEM', c=100,m=1033,x0=5)
