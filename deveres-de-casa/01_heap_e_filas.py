"""
Desafio do Pronto-Socorro

Sistema simples de triagem hospitalar usando Max-Heap.

Regra:
- Quanto maior o nível de dor, maior a prioridade.
- Dor varia de 1 a 10.
- O paciente com maior dor é atendido primeiro.
"""


class MaxHeapTriagem:

    def __init__(self):
        self.heap = []
        self.posicao = {}
        self.ordem_chegada = 0

    def _pai(self, i):
        return (i - 1) // 2

    def _esquerda(self, i):
        return 2 * i + 1

    def _direita(self, i):
        return 2 * i + 2

    def _tem_maior_prioridade(self, paciente_a, paciente_b):
        """
        Retorna True se paciente_a tiver prioridade maior que paciente_b.

        Critério:
        1. Maior dor tem maior prioridade.
        2. Em caso de empate, quem chegou primeiro tem prioridade.
        """
        if paciente_a["dor"] > paciente_b["dor"]:
            return True

        if paciente_a["dor"] == paciente_b["dor"]:
            return paciente_a["ordem"] < paciente_b["ordem"]

        return False

    def _trocar(self, i, j):
        """Troca dois pacientes de posição no heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        self.posicao[self.heap[i]["id"]] = i
        self.posicao[self.heap[j]["id"]] = j

    def _subir(self, i):
        """
        Sift-Up.

        Usado quando um paciente é inserido ou quando sua prioridade aumenta.
        """
        while i > 0:
            pai = self._pai(i)

            if self._tem_maior_prioridade(self.heap[i], self.heap[pai]):
                self._trocar(i, pai)
                i = pai
            else:
                break

    def _descer(self, i):
        """
        Sift-Down.

        Usado quando o paciente da raiz é removido ou quando sua prioridade diminui.
        """
        tamanho = len(self.heap)

        while True:
            esquerda = self._esquerda(i)
            direita = self._direita(i)
            maior = i

            if (
                esquerda < tamanho
                and self._tem_maior_prioridade(self.heap[esquerda], self.heap[maior])
            ):
                maior = esquerda

            if (
                direita < tamanho
                and self._tem_maior_prioridade(self.heap[direita], self.heap[maior])
            ):
                maior = direita

            if maior != i:
                self._trocar(i, maior)
                i = maior
            else:
                break

    def inserir_paciente(self, id_paciente, nome, dor):
        """Insere um novo paciente na fila de prioridade."""
        if dor < 1 or dor > 10:
            print("Erro: a dor deve estar entre 1 e 10.")
            return

        if id_paciente in self.posicao:
            print("Erro: já existe um paciente com esse ID.")
            return

        paciente = {
            "id": id_paciente,
            "nome": nome,
            "dor": dor,
            "ordem": self.ordem_chegada
        }

        self.ordem_chegada += 1

        self.heap.append(paciente)
        indice = len(self.heap) - 1
        self.posicao[id_paciente] = indice

        self._subir(indice)

    def atender_paciente(self):
        """Remove e retorna o paciente com maior prioridade."""
        if len(self.heap) == 0:
            print("Não há pacientes na fila.")
            return None

        paciente_atendido = self.heap[0]

        ultimo = self.heap.pop()
        del self.posicao[paciente_atendido["id"]]

        if len(self.heap) > 0:
            self.heap[0] = ultimo
            self.posicao[ultimo["id"]] = 0
            self._descer(0)

        return paciente_atendido

    def ajustar_prioridade(self, id_paciente, nova_dor):
        """
        Ajusta a prioridade de um paciente já existente.

        Se a dor aumentar, aplica Sift-Up.
        Se a dor diminuir, aplica Sift-Down.
        """
        if nova_dor < 1 or nova_dor > 10:
            print("Erro: a dor deve estar entre 1 e 10.")
            return

        if id_paciente not in self.posicao:
            print("Erro: paciente não encontrado.")
            return

        indice = self.posicao[id_paciente]
        dor_antiga = self.heap[indice]["dor"]

        self.heap[indice]["dor"] = nova_dor

        if nova_dor > dor_antiga:
            self._subir(indice)
        elif nova_dor < dor_antiga:
            self._descer(indice)

        print("Prioridade ajustada com sucesso.")

    def ver_proximo(self):
        """Mostra o próximo paciente a ser atendido sem remover da fila."""
        if len(self.heap) == 0:
            print("Não há pacientes na fila.")
            return

        paciente = self.heap[0]
        print(
            f"Próximo paciente: {paciente['nome']} "
            f"| ID: {paciente['id']} "
            f"| Dor: {paciente['dor']}"
        )

    def listar_pacientes(self):
        """Lista os pacientes na estrutura atual do heap."""
        if len(self.heap) == 0:
            print("Não há pacientes na fila.")
            return

        print("\nFila atual no heap:")
        for paciente in self.heap:
            print(
                f"ID: {paciente['id']} | "
                f"Nome: {paciente['nome']} | "
                f"Dor: {paciente['dor']}"
            )


def ler_dor():
    """Lê e valida o nível de dor."""
    while True:
        dor = int(input("Nível de dor do paciente (1 a 10): "))

        if 1 <= dor <= 10:
            return dor

        print("Valor inválido. Digite um número entre 1 e 10.")


def main():
    """Função principal do programa."""
    triagem = MaxHeapTriagem()

    print("=== Sistema de Triagem Hospitalar ===")

    n = int(input("Quantos pacientes deseja cadastrar inicialmente? "))

    for i in range(n):
        print(f"\nPaciente {i + 1}")

        id_paciente = input("ID do paciente: ")
        nome = input("Nome do paciente: ")
        dor = ler_dor()

        triagem.inserir_paciente(id_paciente, nome, dor)

    while True:
        print("\n=== Menu ===")
        print("1 - Inserir novo paciente")
        print("2 - Ajustar prioridade de paciente")
        print("3 - Atender próximo paciente")
        print("4 - Ver próximo paciente")
        print("5 - Listar fila atual")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_paciente = input("ID do paciente: ")
            nome = input("Nome do paciente: ")
            dor = ler_dor()

            triagem.inserir_paciente(id_paciente, nome, dor)

        elif opcao == "2":
            id_paciente = input("ID do paciente que terá a dor alterada: ")
            nova_dor = ler_dor()

            triagem.ajustar_prioridade(id_paciente, nova_dor)

        elif opcao == "3":
            paciente = triagem.atender_paciente()

            if paciente is not None:
                print(
                    f"Paciente atendido: {paciente['nome']} "
                    f"| ID: {paciente['id']} "
                    f"| Dor: {paciente['dor']}"
                )

        elif opcao == "4":
            triagem.ver_proximo()

        elif opcao == "5":
            triagem.listar_pacientes()

        elif opcao == "0":
            print("Encerrando sistema.")
            break

        else:
            print("Opção inválida.")


main()
