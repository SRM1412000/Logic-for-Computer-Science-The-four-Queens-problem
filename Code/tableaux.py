#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []
#conectivos binarios
ConectivosBinarios = ['Y','O','>','<->']

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

            
def imprime_listaHojas(L):
    for h in L:
        print(imprime_hoja(h))



def String2Tree(A):
	# Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
	# Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
	#        - letrasProposicionales, lista de letras proposicionales
	#        - conectivos, lista de conectivos
	# Output: formula como tree
	pila = []
	for c in A:
		# print("Examinando " + str(c))
		if c in letrasProposicionales:
			# print(u"El símbolo es letra proposicional")
			pila.append(Tree(c, None, None))
		elif c == '-':
			# print("Negamos")
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in ConectivosBinarios:
			# print("Unimos mediante conectivo")
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		else:
			print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
	return pila[-1]


def Inorder2Tree(A):
	if len(A) == 1:
		return Tree(A[0], None, None)
	elif A[0] == '-':
		return Tree(A[0], None, Inorder2Tree(A[1:]))
	elif A[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(A)):
			if A[i] == "(":
				counter += 1
			elif A[i] == ")":
				counter -=1
			elif (A[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(A[i], Inorder2Tree(A[1:i]), Inorder2Tree(A[i + 1:-1]))
	else:
		return -1


def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label




         
def complemento(f):
    if f.label not in ConectivosBinarios:
        if f.label == '-' and (f.right).label != '-' and (f.right).label not in ConectivosBinarios:
            return ((Tree((f.right).label,None,None)))
        elif f.right == None:
            return (Tree('-',None,Tree(f.label,None,None)))
        


def par_complementario(l):
    for i in range(0,len(l)):
        for j in range(1,len(l)):
            if Inorder(l[i])==Inorder(complemento(l[j])):
                return True
    return False
                



def es_literal(f):
    if f.label=='-' and (f.right).right==None:
        return True
    elif f.right==None:
        return True
    else:
         return False
    



def no_literales(l):
    for i in l:
       if es_literal(i)==False:
           return i
    return None
        



def clasificacion(a):
    if a.label=='-':
        if (a.right).label=='-':
            return '1ALFA'
        elif (a.right).label=='O':
            return '3ALFA'
        elif (a.right).label=='>':
            return '4ALFA'
        elif (a.right).label =='Y':
            return '1BETA'
    else:
        if a.label=='Y':
            return '2ALFA'
        elif a.label == 'O':
            return '2BETA'
        elif a.label=='>':
            return '3BETA'
        


         
def clasifica_y_extiende(f,h):
    
    # Extiende listaHojas de acuerdo a la regla respectiva
     
  	# Input: f, una fórmula como árbol
	# 		 h, una hoja (lista de fórmulas como árboles)
	# Output: no tiene output, pues modifica la variable global listaHojas
    global listaHojas
    print("Formula: ",Inorder(f))
    print("Hoja",imprime_hoja(h))
    
    assert(f in h), "La formula no esta en la lista!"
    clase=clasificacion(f)
    print("Clasificada como: ",clase)
    assert(clase!=None), "formula incorrecta "+imprime_hoja(h)
    
    if clase == '1ALFA':
         aux = [x for x in h]
         listaHojas.remove(h)
         aux.remove(f)
         aux += [f.right.right]
         listaHojas.append(aux)
         
    elif clase == '2ALFA':
         aux=[x for x in h]
         listaHojas.remove(h)
         aux.remove(f)
         aux += [f.left,f.right]
         listaHojas.append(aux)
         
    elif clase=='3ALFA':
        aux=[x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        aux += [Tree('-',None,(f.right).left),Tree('-',None,(f.right).right)]
        listaHojas.append(aux)
         
    elif clase=='4ALFA':
        aux=[x for x in h if x != f]
        listaHojas.remove(h)
        # aux.remove(f)
        aux+=[(f.right).left,Tree('-',None,(f.right).right)]
        listaHojas.append(aux)
    
    elif clase=='1BETA':
        aux=[x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        # aux1=[]
        listaHojas.append([x for x in aux+[Tree('-',None,(f.right).left)]])
        listaHojas.append([x for x in aux+[Tree('-',None,(f.right).right)]])
        # listaHojas.append(aux1)
     
    elif clase=='2BETA':    
        aux=[x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        # aux1=[]
        listaHojas.append([x for x in aux+[f.right]])
        listaHojas.append([x for x in aux+[f.left]])
        # listaHojas.append(aux1)
    
    elif clase=='3BETA':
        aux=[x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        # aux1=[]
        listaHojas.append([x for x in aux+[Tree('-',None,f.right)]])
        listaHojas.append([x for x in aux+[f.left]])
        # listaHojas.append(aux1)
        


def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f

	global listaHojas
	global listaInterpsVerdaderas

	A = String2Tree(f)
	print(u'La fórmula introducida es:\n', Inorder(A))

	listaHojas = [[A]]

	while (len(listaHojas) > 0):
		h = choice(listaHojas)
		print("Trabajando con hoja:\n", imprime_hoja(h))
		x = no_literales(h)
		if x == None:
			if par_complementario(h):
				listaHojas.remove(h)
			else:
				listaInterpsVerdaderas.append(h)
				listaHojas.remove(h)
		else:
			clasifica_y_extiende(x, h)

	return listaInterpsVerdaderas



	

    