import heapq

# cria o grafo
grafo = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (4, 5)],
    3: [(4, 1)],
    4: []
}


def dijkstra(grafo, inicio, destino):
    # guarda as menores distancias
    distancias = {}

    # guarda o caminho anterior
    predecessores = {}

    # guarda os nos visitados
    visitados = set()

    # inicia as distancias
    for no in grafo:
        distancias[no] = float("inf")
        predecessores[no] = None

    distancias[inicio] = 0

    # fila de prioridade
    fila = [(0, inicio)]

    print("Execucao passo a passo")
    print()

    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)

        if no_atual in visitados:
            continue

        visitados.add(no_atual)

        print("No visitado", no_atual)

        # verifica os vizinhos
        for vizinho, peso in grafo[no_atual]:
            nova_distancia = distancia_atual + peso

            print("Verificando", no_atual, "para", vizinho, "peso", peso)

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila, (nova_distancia, vizinho))
                print("Atualizou distancia do no", vizinho)
            else:
                print("Nao atualizou distancia do no", vizinho)

        print("Distancias", distancias)
        print("Predecessores", predecessores)
        print()

    # monta o caminho final
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]

    caminho.reverse()

    return caminho, distancias[destino]


caminho, custo = dijkstra(grafo, 0, 4)

print("Caminho minimo")
print(caminho)

print("Custo minimo total")
print(custo)
