# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:58:19 2016

@author: Agus
"""


import os
import numpy as np
import matplotlib.pyplot as plt

from publib import set_style, fix_style

set_style('article')

#%%

def listar_archivos():
    return os.listdir('Resultados_QvsQ/')

def cargar_partidas(fileName):
    datos = np.loadtxt('Resultados_QvsQ/'+fileName)
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
        var = str(var)
    
    ns = range(6)
    Qs = []
    Rs = []
    for n in ns:
        file = FileDictionary[(tipo, str(n))]
        partidas, Qganadas, Rganadas = cargar_partidas(file)
        partidas_r, Q_r, R_r = ratio(partidas, Qganadas, Rganadas, 500)
        Qs.append(Q_r)
        Rs.append(R_r)
    
    Q = np.mean(Qs, axis=0)
    denom = np.sqrt(len(Qs))
    Q_err = np.std(Qs, axis=0)/denom
    R = np.mean(Rs, axis=0)
    R_err = np.std(Rs, axis=0)/denom
    return partidas_r, Q, R, Q_err, R_err

#%%

Files = listar_archivos()

# Este diccionario no se fija si se vario epsilon, alfa o gamma
FileDictionary = {}
for file in Files:
    file_parts = file.split('_')
    tipo = file_parts[0]
    n_usado = file_parts[1].split('.')[0][1:]
    FileDictionary[(tipo, n_usado)] = file

#%% Gráfico de QvsQ
partidas_r, this_Q, this_R, this_Q_err, this_R_err = promedio('QvsQ', np.nan)
plt.plot(partidas_r, this_Q, alpha=0.7, label='Player 1')
plt.plot(partidas_r, this_R, alpha=0.7, label='Player 2')

plt.fill_between(partidas_r, this_Q+this_Q_err, this_Q-this_Q_err, color='0.6', alpha=0.75)
plt.fill_between(partidas_r, this_R+this_R_err, this_R-this_R_err, color='0.6', alpha=0.75)

plt.legend(loc=2)
plt.xlabel('Partidas')
plt.ylabel('Porcentaje Ganadas')
#plt.title('$\epsilon$-greedy')
plt.ylim((0.45, 1))
fix_style('article')
plt.savefig('Figuras/QvsQ.png')
plt.show()

