import heapq


# cria o grafo
grafo = {
    "A": [("B", 4), ("C", 4)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 5), ("E", 6)],
    "D": [("B", 5), ("C", 5), ("E", 3), ("F", 4)],
    "E": [("C", 6), ("D", 3), ("F", 2)],
    "F": [("D", 4), ("E", 2)]
}


def prim(grafo, inicio):
    # cidades ja conectadas
    visitados = set()

    # fila de prioridade
    fila = []

    # resultado final
    rota = []
    total = 0

    # adiciona a cidade inicial
    visitados.add(inicio)

    # coloca as arestas da cidade inicial na fila
    for destino, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, destino))

    # continua ate conectar todas as cidades
    while fila and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(fila)

        # ignora se a cidade ja foi conectada
        if destino in visitados:
            continue

        # adiciona a rota escolhida
        visitados.add(destino)
        rota.append((origem, destino, peso))
        total += peso

        # adiciona novas opcoes de cabo
        for proximo, novo_peso in grafo[destino]:
            if proximo not in visitados:
                heapq.heappush(fila, (novo_peso, destino, proximo))

    return rota, total


rota, total = prim(grafo, "A")

print("Cabos que devem ser instalados")

for origem, destino, peso in rota:
    print(origem, "->", destino, "-", peso, "km")

print("Total minimo de cabo", total, "km")
