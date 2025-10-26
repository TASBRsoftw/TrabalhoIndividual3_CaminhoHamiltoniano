"""
hamiltonian.py - Algoritmo para encontrar Caminho Hamiltoniano
"""
from utils import eh_caminho_hamiltoniano

def encontrar_caminho_hamiltoniano(grafo):
    n = len(grafo)
    caminho = [0]
    visitados = set([0])
    if busca(grafo, caminho, visitados, n):
        return caminho
    return None

def busca(grafo, caminho, visitados, n):
    if len(caminho) == n:
        if grafo[caminho[-1]][caminho[0]] == 1:
            return True
        return False
    for v in range(n):
        if grafo[caminho[-1]][v] == 1 and v not in visitados:
            caminho.append(v)
            visitados.add(v)
            if busca(grafo, caminho, visitados, n):
                return True
            caminho.pop()
            visitados.remove(v)
    return False
