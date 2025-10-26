
# Projeto Caminho Hamiltoniano

Este projeto implementa um algoritmo para encontrar Caminhos Hamiltonianos em grafos, utilizando busca exaustiva com backtracking.

## Descrição do Projeto

O objetivo é determinar se existe um caminho Hamiltoniano em um grafo, ou seja, um caminho que visita todos os vértices exatamente uma vez e retorna ao ponto inicial. O algoritmo foi implementado em Python, com a seguinte lógica:

### Explicação do Algoritmo (linha a linha)

Arquivo: `src/hamiltonian.py`

1. `def encontrar_caminho_hamiltoniano(grafo):`
	- Função principal que inicia a busca pelo caminho Hamiltoniano.
2. `n = len(grafo)`
	- Calcula o número de vértices do grafo.
3. `caminho = [0]`
	- Começa o caminho pelo vértice 0.
4. `visitados = set([0])`
	- Marca o vértice 0 como visitado.
5. `if busca(grafo, caminho, visitados, n):`
	- Chama a função recursiva de busca.
6. `return caminho`
	- Se encontrar, retorna o caminho.
7. `return None`
	- Se não encontrar, retorna None.

Função recursiva:

1. `def busca(grafo, caminho, visitados, n):`
	- Função que tenta expandir o caminho atual.
2. `if len(caminho) == n:`
	- Se todos os vértices foram visitados...
3. `if grafo[caminho[-1]][caminho[0]] == 1:`
	- ...e existe aresta de volta ao início, retorna True.
4. Para cada vértice `v` não visitado e conectado ao último do caminho:
	- Adiciona `v` ao caminho e marca como visitado.
	- Chama recursivamente a busca.
	- Se não encontrar, desfaz (backtrack) e tenta outro vértice.
5. Se nenhum caminho válido for encontrado, retorna False.

Arquivo: `src/main.py`

1. Define um grafo de exemplo (matriz de adjacência).
2. Chama `encontrar_caminho_hamiltoniano` e imprime o resultado.

Arquivo: `src/utils.py`

1. Função auxiliar para validar se um caminho é Hamiltoniano.

## Como executar o projeto

1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta do projeto.
3. Execute o comando:

```bash
python src/main.py
```

O resultado será exibido no terminal, mostrando se existe ou não um caminho Hamiltoniano para o grafo definido.

## Relatório Técnico

### Análise da Complexidade Computacional

#### Classes P, NP, NP-Completo e NP-Difícil
1. O problema do Caminho Hamiltoniano pertence à classe NP-Completo. Isso significa que:
	- Está em NP: Dado um caminho, é possível verificar em tempo polinomial se ele é Hamiltoniano.
	- É NP-Completo: Não existe algoritmo conhecido que resolva todos os casos em tempo polinomial, e qualquer problema em NP pode ser reduzido a ele em tempo polinomial.
2. Justificativa:
	- O Caminho Hamiltoniano é similar ao Problema do Caixeiro Viajante (TSP), que também é NP-Completo. Ambos envolvem encontrar um caminho que visita todos os vértices, mas o TSP busca o caminho de menor custo.

#### Análise da Complexidade Assintótica de Tempo
1. O algoritmo implementado (busca exaustiva/backtracking) possui complexidade temporal O(n!), onde n é o número de vértices do grafo.
2. Explicação:
	- Para cada vértice inicial, o algoritmo tenta todas as permutações possíveis dos vértices restantes, resultando em n! possibilidades.
	- Método utilizado: contagem de operações e análise combinatória das permutações.

#### Aplicação do Teorema Mestre
O Teorema Mestre é aplicável a recorrências do tipo T(n) = aT(n/b) + f(n), comuns em algoritmos de divisão e conquista. O algoritmo do Caminho Hamiltoniano não se encaixa nesse padrão, pois explora todas as permutações (não divide o problema em subproblemas de tamanho reduzido de forma regular). Portanto, o Teorema Mestre não é aplicável aqui.

#### Análise dos Casos de Complexidade
1. Pior caso: O algoritmo explora todas as permutações possíveis sem encontrar um caminho Hamiltoniano, resultando em O(n!) operações.
2. Caso médio: Depende da estrutura do grafo; em grafos densos, pode encontrar soluções mais rapidamente, mas ainda é exponencial.
3. Melhor caso: O caminho Hamiltoniano é encontrado nas primeiras tentativas, reduzindo o número de operações, mas ainda é O(n!) no pior cenário.
4. Impacto: A diferença entre os casos afeta diretamente o tempo de execução. Em grafos grandes, o algoritmo torna-se impraticável devido ao crescimento exponencial do número de possibilidades.

---
