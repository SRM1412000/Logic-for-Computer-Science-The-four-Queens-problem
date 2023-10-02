#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./4
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(\
                                    (0, step), \
                                    step, \
                                    step,\
                                    facecolor='cornsilk')\
                                    )
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(0, 3*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step*2, 3 * step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step*3, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step*3, step*2), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step, step*3), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step*3, step), step, step],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step*3, step*3), step, step],\
            facecolor='lightslategrey'))


    # Creo las líneas del tablero
    for j in range(4):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen de caballo
    arr_img = plt.imread("dama80x80.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.5)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones['a'] = [0.125, 0.125]
    direcciones['b'] = [0.375, 0.125]
    direcciones['c'] = [0.625, 0.125]
    direcciones['d'] = [0.875, 0.125]
    direcciones['e'] = [0.125, 0.375]
    direcciones['f'] = [0.375, 0.375]
    direcciones['g'] = [0.625, 0.375]
    direcciones['h'] = [0.875, 0.375]
    direcciones['i'] = [0.125, 0.625]
    direcciones['j'] = [0.375, 0.625]
    direcciones['k'] = [0.625, 0.625]
    direcciones['l'] = [0.875, 0.625]
    direcciones['m'] = [0.125, 0.875]
    direcciones['n'] = [0.375, 0.875]
    direcciones['o'] = [0.625, 0.875]
    direcciones['p'] = [0.875, 0.875]

    for l in f:
        if f[l] != 0:
            ab = AnnotationBbox(imagebox, direcciones[l], frameon=False)
            axes.add_artist(ab)

    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")
   


f = {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 1, 'o': 0, 'p': 0}
dibujar_tablero(f,121)