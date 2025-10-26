"""
utils.py - Funções utilitárias para o projeto Caminho Hamiltoniano
"""
def eh_caminho_hamiltoniano(grafo, caminho):
    n = len(grafo)
    if len(caminho) != n:
        return False
    for i in range(n - 1):
        if grafo[caminho[i]][caminho[i+1]] == 0:
            return False
    if grafo[caminho[-1]][caminho[0]] == 0:
        return False
    return True
