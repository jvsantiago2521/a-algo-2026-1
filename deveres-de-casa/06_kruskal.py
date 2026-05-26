class Grafo:
    def __init__(self, vertices):
        # guarda a quantidade de vertices
        self.v = vertices

        # guarda as arestas do grafo
        self.grafo = []

    def adicionar_aresta(self, u, v, peso):
        # adiciona uma aresta no grafo
        self.grafo.append([u, v, peso])

    def buscar_raiz(self, pai, i):
        # busca a raiz do conjunto
        if pai[i] == i:
            return i

        # compressao de caminho
        pai[i] = self.buscar_raiz(pai, pai[i])
        return pai[i]

    def unir_redes(self, pai, rank, x, y):
        # une dois conjuntos
        raiz_x = self.buscar_raiz(pai, x)
        raiz_y = self.buscar_raiz(pai, y)

        # evita arvores grandes
        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def executar_kruskal_maximo(self):
        # guarda o resultado final
        resultado = []

        # guarda o custo total
        custo_total = 0

        # ordena da maior aresta para a menor
        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=True)

        # cria os conjuntos separados
        pai = []
        rank = []

        for no in range(self.v):
            pai.append(no)
            rank.append(0)

        # controla a quantidade de arestas escolhidas
        arestas_escolhidas = 0

        # percorre todas as arestas
        for u, v, peso in self.grafo:
            if arestas_escolhidas == self.v - 1:
                break

            raiz_u = self.buscar_raiz(pai, u)
            raiz_v = self.buscar_raiz(pai, v)

            # se as raizes forem diferentes nao forma ciclo
            if raiz_u != raiz_v:
                resultado.append([u, v, peso])
                custo_total += peso
                arestas_escolhidas += 1
                self.unir_redes(pai, rank, raiz_u, raiz_v)

        return resultado, custo_total


# caso de teste
g = Grafo(8)

g.adicionar_aresta(4, 7, 1)
g.adicionar_aresta(5, 6, 2)
g.adicionar_aresta(4, 5, 3)
g.adicionar_aresta(6, 7, 4)
g.adicionar_aresta(0, 1, 5)
g.adicionar_aresta(3, 7, 6)
g.adicionar_aresta(2, 5, 7)
g.adicionar_aresta(2, 6, 8)
g.adicionar_aresta(1, 2, 9)
g.adicionar_aresta(1, 6, 10)
g.adicionar_aresta(1, 5, 11)
g.adicionar_aresta(1, 7, 13)
g.adicionar_aresta(1, 4, 14)
g.adicionar_aresta(0, 4, 15)
g.adicionar_aresta(0, 3, 16)
g.adicionar_aresta(3, 6, 17)
g.adicionar_aresta(0, 7, 18)

caminho_final, custo_final = g.executar_kruskal_maximo()

print("Resultado da arvore geradora maxima")
print("Rotas escolhidas")

for u, v, peso in caminho_final:
    print("Cidade", u, "para cidade", v, "custo", peso)

print("Custo total maximo", custo_final)
