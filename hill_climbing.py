import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Calcular la distancia correcta por una ruta
def evalua_ruta(ruta):
    total = 0
    for i in range(0, len(ruta)-1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total = total + distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[i + 1]
    ciudad2 = ruta[0]
    return total

def i_hill_climbing():
    # Crear ruta inicial aleatoria
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        max_iteraciones -= 1
        mejora = False
        # Generar nueva ruta aleatoria
        random.shuffle(ruta)
        for i in range(0,len(ruta)):
            for j in range(0, len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_ruta(ruta_tmp)
                    if dist < evalua_ruta(mejor_ruta):
                        # Se encontró un vecino que mejora el resultado
                        mejor_ruta = ruta_tmp[:]
                        mejora = True
        if not mejora:
            break
    return mejor_ruta

def imprimir():
    global coord
    coord = {
        'Jiloyork' :(19.916012, -99.580580),
        'Toluca':(19.289165, -99.655697),
        'Atlacomulco':(19.799520, -99.873844),
        'Guadalajara':(20.677754472859146, -103.34625354877137),
        'Monterrey':(25.69161110159454, -100.321838480256),
        'QuintanaRoo':(21.163111924844458, -86.80231502121464),
        'Michohacan':(19.701400113725654, -101.20829680213464),
        'Aguascalientes':(21.87641043660486, -102.26438663286967),
        'CDMX':(19.432713075976878, -99.13318344772986),
        'QRO':(20.59719437542255, -100.38667040246602)
    }
    
    ruta = i_hill_climbing()
    return ("Ruta: "+ str(ruta) + "/n Distancia Total:", evalua_ruta(ruta))
