from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# carrega os dados
dados = load_breast_cancer()

# separa atributos e classes
x = dados.data
y = dados.target

# separa treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# normaliza os dados
normalizador = StandardScaler()
x_treino = normalizador.fit_transform(x_treino)
x_teste = normalizador.transform(x_teste)

# valores de k
valores_k = [1, 3, 5]

# metricas de distancia
metricas = [
    ("euclidiana", "euclidean"),
    ("manhattan", "manhattan")
]

# guarda os resultados
resultados = []

# testa cada combinacao
for k in valores_k:
    for nome_metrica, metrica in metricas:

        # cria o modelo
        modelo = KNeighborsClassifier(
            n_neighbors=k,
            metric=metrica
        )

        # treina o modelo
        modelo.fit(x_treino, y_treino)

        # faz a previsao
        previsoes = modelo.predict(x_teste)

        # calcula a acuracia
        acuracia = accuracy_score(y_teste, previsoes)

        # salva o resultado
        resultados.append((k, nome_metrica, acuracia))

        print("K", k)
        print("Metrica", nome_metrica)
        print("Acuracia", round(acuracia * 100, 2), "%")
        print()


# encontra o melhor resultado
melhor = max(resultados, key=lambda item: item[2])

print("Melhor resultado")
print("K", melhor[0])
print("Metrica", melhor[1])
print("Acuracia", round(melhor[2] * 100, 2), "%")

# Qual K teve melhor desempenho?
# O melhor desempenho foi com K = 3.

# Qual métrica obteve melhor resultado?
# A melhor métrica foi a euclidiana, com acurácia de aproximadamente 98.25%.

# O que aconteceu com K muito pequeno?
# Com K = 1, o modelo ficou mais sensível a ruídos e casos isolados. Isso pode causar overfitting, porque o modelo depende apenas do vizinho mais próximo.

# Por que normalizar é importante?
# A normalização é importante porque o K-NN calcula distâncias. Se uma coluna tiver valores muito maiores que outra, ela pode dominar o cálculo da distância. Com StandardScaler, os atributos ficam na mesma escala e a comparação entre os vizinhos fica mais justa.
