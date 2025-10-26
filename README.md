
# Projeto Caminho Hamiltoniano

Este projeto implementa um algoritmo para encontrar Caminhos Hamiltonianos em grafos, conforme proposto no trabalho individual.

## Estrutura
- `src/main.py`: Ponto de entrada do projeto.
- `src/hamiltonian.py`: Algoritmo de busca do caminho Hamiltoniano.
- `src/utils.py`: Funções auxiliares para validação de caminhos.

## Como executar

```bash
python src/main.py
```

## Exemplo de uso
O projeto já inclui um exemplo de grafo no arquivo `main.py`. Basta executar para ver o resultado.

---

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
