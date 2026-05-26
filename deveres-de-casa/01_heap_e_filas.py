"""
Dever de casa
Max Heap com passo a passo

Lista usada
13 2 6 25 8 40 1
"""


def mostrar_arvore(heap):
    # mostra a heap em niveis
    print("Array da heap", heap)

    indice = 0
    nivel = 0
    quantidade = 1

    while indice < len(heap):
        linha = heap[indice:indice + quantidade]
        print("Nivel", nivel, linha)

        indice += quantidade
        quantidade *= 2
        nivel += 1

    print()


def inserir(heap, valor):
    # insere um valor na heap
    print("Inserindo", valor)

    heap.append(valor)
    indice = len(heap) - 1

    print("Valor inserido no final")
    mostrar_arvore(heap)

    # sobe enquanto o filho for maior que o pai
    while indice > 0:
        pai = (indice - 1) // 2

        print("Comparando filho", heap[indice], "com pai", heap[pai])

        if heap[indice] > heap[pai]:
            print("Swap", heap[indice], "com", heap[pai])
            heap[indice], heap[pai] = heap[pai], heap[indice]
            indice = pai
            mostrar_arvore(heap)
        else:
            print("Nao precisa trocar")
            break

    print("Heap depois da insercao de", valor)
    mostrar_arvore(heap)


def remover_maior(heap):
    # remove a raiz da heap
    if len(heap) == 0:
        print("Heap vazia")
        return

    print("Removendo maior elemento", heap[0])

    maior = heap[0]
    ultimo = heap.pop()

    if len(heap) > 0:
        heap[0] = ultimo
        print("Ultimo elemento foi para a raiz")
        mostrar_arvore(heap)

        indice = 0

        # desce enquanto algum filho for maior
        while True:
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2
            maior_indice = indice

            if esquerda < len(heap):
                print("Comparando pai", heap[indice], "com filho esquerdo", heap[esquerda])

                if heap[esquerda] > heap[maior_indice]:
                    maior_indice = esquerda

            if direita < len(heap):
                print("Comparando maior atual", heap[maior_indice], "com filho direito", heap[direita])

                if heap[direita] > heap[maior_indice]:
                    maior_indice = direita

            if maior_indice != indice:
                print("Swap", heap[indice], "com", heap[maior_indice])
                heap[indice], heap[maior_indice] = heap[maior_indice], heap[indice]
                indice = maior_indice
                mostrar_arvore(heap)
            else:
                print("Nao precisa trocar")
                break

    print("Elemento removido", maior)
    print("Heap depois da remocao")
    mostrar_arvore(heap)


# lista do dever
valores = [13, 2, 6, 25, 8, 40, 1]
heap = []

print("Inicio da insercao")
print()

for valor in valores:
    inserir(heap, valor)

print("Inicio da remocao")
print()

while len(heap) > 0:
    remover_maior(heap)
