"""
main.py - Entrada principal do projeto Caminho Hamiltoniano
"""
from hamiltonian import encontrar_caminho_hamiltoniano

def main():
    # Grafo mais complexo (6 vértices)
    grafo = [
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0]
    ]
    caminho = encontrar_caminho_hamiltoniano(grafo)
    if caminho:
        print("Caminho Hamiltoniano encontrado:", caminho)
    else:
        print("Não existe caminho Hamiltoniano para o grafo fornecido.")

if __name__ == "__main__":
    main()
