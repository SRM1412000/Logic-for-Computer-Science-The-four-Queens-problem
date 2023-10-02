# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:57:35 2020

@author: David
"""


import sys
sys.setrecursionlimit(10000)
from itertools import combinations
import time


class Tree(object):
    def __init__(self,label,left,right):
        self.label = label
        self.left = left 
        self.right = right

def inorder(f):
    resultado = ""
    if f.label in letrasProposicionales:
        resultado = resultado + f.label
        return resultado
    elif f.label in negacion:
        resultado = resultado + "" + negacion[0] + inorder(f.right)
        return resultado
    elif f.label in conectivosBinarios:
        resultado = resultado+"("+inorder(f.left)+f.label+inorder(f.right)+")"
        return resultado

conectivosBinarios = ["Y","O",">","<->","*"]
negacion = ["-"]

def codifica(f, c):
   if ((f < 1) or (f > Nf)):
     print("Fila incorrecta! Debe ser un numero entre 1 y", Nf)
     return None
   elif ((c < 1) or (c > Nc)):
     print("Columna incorrecta! Debe ser un numero entre 1 y", Nc)
     return None
   else:
     return chr(92 + f*Nf + c)
 
def decodifica(x, Nf, Nc):
    n = ord(x) - 96
    if ((n < 1) or (n > Nc*Nf)):
     print("Caracter incorrecto!")
     return None
    else:
     for i in range(1,Nf + 1):
        if(ord(x) < 97 + Nf*i):
            f = i
            c = ord (x) - 92 - Nf*i
            return f, c
        

Nf=4
Nc=4

letrasProposicionales= []

for i in range(97,97+(Nf*Nc)):
        letrasProposicionales.append(chr(i))
u=(set(letrasProposicionales))

# print("letrasProposicionales")
for i in range(Nc):
    print(letrasProposicionales[Nf*(i):Nc*(i+1)])

fila = 2
columna = 1
print("La fila es", fila)
print("La columna es", columna)
n = codifica(fila, columna)
print("La codificacion es", n)
f, c = decodifica(n, Nf, Nc)
print("La decodificacion es Dama en fila", f, "columna", c)
# x=time.perf_counter()
combinaciones = list(combinations(letrasProposicionales,4))
# y=time.perf_counter()

# print(combinaciones)
# print("El tiempo es: ",x-y )
print("Len combinaciones: ",len(combinaciones))

lista1=[]
# lista_aux=[]



for i in combinaciones:

    a=set(i)
    lista1.append(sorted((u-a)))

# w=permutaciones[0]
# print(w)
# print(permutaciones[1])
# print(lista_aux)
print("Len lista1: ",len(lista1))

# for j in letrasProposicionales:
#     if (j not in w):
#         lista1.append(j)
    # y=set(letrasProposicionales)
    # x=set(i)
    # a= set(y-x)
    # print(a)
    # lista1.append(a)
    
    
# lista1=[]
# for i in permutaciones:
#     for j in letrasProposicionales:
#         if (j not in i):
#             lista1.append(j)
    # lista_aux.append(lista1)

    # lista1.append(lista_aux)

# print(lista1)
# print(len(lista1))

def regla1():
    primera=True
    # cont =0
    for i in range(0,(len(combinaciones))):
        primeravez=True
        primeravez2=True
        for j in combinaciones[i]:
              # primeravez=True
            if (primeravez):
                tot = Tree(j,None,None)
                primeravez=False
            else:
                tot = Tree("Y",tot,Tree(j,None,None))
            # print("tot: ",inorder(tot))
        for k in lista1[i]:
            if(primeravez2):
                total1=Tree("Y",tot,Tree('-',None,Tree(k,None,None)))
                # print("total",inorder(total1))
                primeravez2=False
            else:
                total1=Tree('Y',total1,Tree('-',None,Tree(k,None,None)))
                #print(inorder(total1))
                # print("total",inorder(total1))       
        if primera:
            #respuesta=inorder(total1)
            respuesta=total1
            #print(inorder(respuesta))
            # print("Respuesta: ",respuesta)
            primera=False
            # cont+=1
        else:
            #respuesta+='O'+inorder(total1)
            respuesta=Tree("O",respuesta,total1)
            #print(inorder(respuesta))
            # cont+=1
            # print(cont)
    return (respuesta)

# print("Regla No1: ",'\n')
# print(regla1())
# print('\n\n\n')



def regla2():              
  PrimeraVez1 = True
  for i in range(0,len(letrasProposicionales)):
      PrimeraVez = True
      diag1 = 1
      diag2 = 1
      diag3= 1
      diag4 = 1
      attacked=""
      f,c = decodifica(letrasProposicionales[i],4,4)
      for j in range(0,len(letrasProposicionales)):
        a,b = decodifica(letrasProposicionales[j],4,4)
        if letrasProposicionales[j] != letrasProposicionales[i]:
         if a == f or c == b:
             if PrimeraVez == False :
               attacked = Tree("Y",attacked,Tree("-",None,Tree(letrasProposicionales[j],None,None)))
             else:
                 attacked = Tree("-",None,Tree(letrasProposicionales[j],None,None))
                 PrimeraVez = False 
         if (a==f+diag1 and b==c+diag1):
                attacked = Tree("Y",attacked,Tree("-",None,Tree(letrasProposicionales[j],None,None)))
                diag1+=1
         if (a==f+diag2 and b==c-diag2):
             attacked = Tree("Y",attacked,Tree("-",None,Tree(letrasProposicionales[j],None,None)))
             diag2+=1
             
      for k in range(len(letrasProposicionales)-1,-1,-1):
          a,b = decodifica(letrasProposicionales[k],4,4)
          if (a==f-diag3 and b==c+diag3):
              attacked = Tree("Y",attacked,Tree("-",None,Tree(letrasProposicionales[k],None,None)))
              diag3+=1
          if (a==f-diag4 and b==c-diag4):
               attacked = Tree("Y",attacked,Tree("-",None,Tree(letrasProposicionales[k],None,None)))
               diag4+=1
             
      respuesta = (Tree(">",Tree(letrasProposicionales[i],None,None),attacked))
      if (PrimeraVez1):
          respuestafinal=respuesta
          PrimeraVez1=False
      else:
          respuestafinal=Tree("Y",respuestafinal,respuesta)
  return (respuestafinal)
    
# print("Regla No2: ",'\n')
# print(regla2())
# print("\nReina en condicion inicial: ",regla3())

def regla3():   
    return Tree(codifica(4,3),None,None)



def ReglaFinal(i,j,k):
    return Tree("Y",i,Tree("Y",j,k))

#print(inorder(ReglaFinal(regla1(), regla2(), regla3())))



