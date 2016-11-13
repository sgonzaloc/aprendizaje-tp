# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:06:31 2016

@author: Agus
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from publib import set_style, fix_style

set_style('article')

#%%

def listar_archivos():
    return os.listdir('Resultados/')

def cargar_partidas(fileName):
    datos = np.loadtxt('Resultados/'+fileName)
    partidas = datos[:, 0]
    Qganadas = datos[:, 1]
    Rganadas = datos[:, 2]
    
    return partidas, Qganadas, Rganadas

def ratio(partidas, Qganadas, Rganadas, bineado):
    # una funcion q calcule el ratios de ganadas por cada uno cada bienado partidas
    indices = np.arange(0, len(Qganadas), bineado)
    Q = Qganadas[indices]
    R = Rganadas[indices]
    Q = np.insert(Q, 0, 0)
    R = np.insert(R, 0, 0)
    Qratio = np.diff(Q)/bineado
    Rratio = np.diff(R)/bineado
    return indices, Qratio, Rratio

def promedio(tipo, var):
    if not isinstance(var, str):
        var = str(int(10*var))
    
    ns = range(6)
    Qs = []
    Rs = []
    for n in ns:
        file = FileDictionary[(tipo, var, str(n))]
        partidas, Qganadas, Rganadas = cargar_partidas(file)
        partidas_r, Q_r, R_r = ratio(partidas, Qganadas, Rganadas, 500)
        Qs.append(Q_r)
        Rs.append(R_r)
    
    Q = np.mean(Qs, axis=0)
    R = np.mean(Rs, axis=0)
    return partidas_r, Q, R

#%%

Files = listar_archivos()

# Este diccionario no se fija si se vario epsilon, alfa o gamma
FileDictionary = {}
for file in Files:
    file_parts = file.split('_')
    tipo = file_parts[0]
    var = file_parts[1].split('.')[0][1:]
    n_usado = file_parts[2].split('.')[0][1:]
    FileDictionary[(tipo, var, n_usado)] = file

#%% Contraste entre graficar ratio, diferencia o totales

partidas, Qganadas, Rganadas = cargar_partidas(Files[12])

partidas_r, Q_r, R_r = ratio(partidas, Qganadas, Rganadas, 500)

# Ploteo totalidad de partidas
plt.plot(Qganadas, 'r', label='Qplayer')
plt.plot(Rganadas, 'b', label='Random')
plt.legend(loc=4)
plt.title('Ploteo todas las partidas')
plt.show()

# Ploteo la diferencia entre uno y otro
plt.plot(Qganadas - Rganadas, 'b', label='Diferencia')
plt.legend(loc=2)
plt.title('Diferencia entre random y Q')
plt.show()

# Ploteo los ratios de ganadas
plt.plot(partidas_r, Q_r, 'r', label='Qplayer')
plt.plot(partidas_r, R_r, 'b', label='Random')
plt.legend(loc=3)
plt.title('Ploteo ratios')
plt.show()

#%% Comparamos para epsilon 0.2 las representaciones de ratio para ver si vale la pena promediar

eps = 0.2
ns = range(0,6)

Qs = []
Rs = []
for n in ns:
    file = FileDictionary[('Optimizacion', str(int(eps*10)), str(n))]
    partidas, Qganadas, Rganadas = cargar_partidas(file)
    partidas_r, Q_r, R_r = ratio(partidas, Qganadas, Rganadas, 500)
    Qs.append(Q_r)
    Rs.append(R_r)

Q = np.mean(Qs, axis=0)
R = np.mean(Rs, axis=0)

# Ploteo superpuestos
for n in ns:
    plt.plot(partidas_r, Qs[n], alpha=0.7)
plt.title('Superpongo ratios')
plt.show()

plt.plot(partidas_r, Q)
plt.title('Promedio de los ratios')
plt.show()

#%%
epsilons = np.arange(0, 1.1, 0.2)

for eps in epsilons:
    partidas_r, this_Q, this_R = promedio('Optimizacion', eps)
    plt.plot(partidas_r, this_Q, alpha=0.7, label='$\epsilon$ = '+str(eps))

plt.legend(loc=2)
plt.title('Barrido en $\epsilon$-greedy')
plt.ylim((0.45, 1))
fix_style('article')
plt.savefig('Figuras/BarridoEpsilon.png')
plt.show()