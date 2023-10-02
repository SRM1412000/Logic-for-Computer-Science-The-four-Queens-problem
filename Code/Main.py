# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 07:58:36 2020

@author: David
"""

import Visualiza as v
import DPLL as dp
import Reglas as re
import FNC as fn
import sys
sys.setrecursionlimit(10000)

#------------------------------EJECUCION PRINCIPAL--------------------------------#



"""-Se crea la lista letrasproposicionalesA para mas adelante poder usar Tseitin-"""
letrasProposicionalesA=[chr(x) for x in range(97,113)]

"""--Del archivo reglas, usamos ReglaFinal que recibe cada regla del proyecto.--
-----luego Inorder, para tener ReglaFinal en forma de string------------------"""
formula=re.inorder(re.ReglaFinal(re.regla1(),re.regla2(),re.regla3()))


"""---Del archivo FNC, usamos Tseitin sobre formula y LetrasProposicionalesA.--
------A continuacion, FormaClausal sobre fFNC para obtener la forma clausal--"""
fFNC=fn.Tseitin(formula, letrasProposicionalesA)
fClaus=fn.formaClausal(fFNC)
print(fClaus)


"""--------Del archivo DPLL, usamos DPLL sobre fClaus para así obtener-----------
----un diccionario con la interpretacion correcta de cada letra proposicional---"""


n,m=dp.DPLL(fClaus,{})
#m es el diccionario


"""-Luego, de m tomamos unicamente las letras Proposicionales que nos interesan-"""

# #------PARA TOMAR UNICAMENTE LAS LETRAS QUE NOS INTERESAN------------# #
u={}

for i in range(97,113):
    u[chr(i)]=m.get(chr(i))
    
print("Diccionario importante: \n\n")
print(u)


"""---Finalmente, del archivo Visualiza usamos dibujar_tablero sobre u
----------para tener la solucion visual a nuestro proyecto-------------"""


v.dibujar_tablero(u,"Final")


