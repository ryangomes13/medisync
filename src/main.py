import json
import os


class MedicamentoManager:
    def __init__(self):
        self.medicamentos = []

    def adicionar_medicamento(self, nome, horario):
        if not nome or not horario:
            return False
        self.medicamentos.append({"nome": nome, "horario": horario})
        return True

    def listar_medicamentos(self):
        return self.medicamentos


def main():
    manager = MedicamentoManager()
    print("--- MediSync: Seu Assistente de Saúde ---")

    while True:
        print("\n1. Adicionar Medicamento\n2. Listar Todos\n3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do remédio: ")
            horario = input("Horário (ex: 08:00): ")
            if manager.adicionar_medicamento(nome, horario):
                print("✅ Medicamento salvo!")
            else:
                print("❌ Erro: Dados inválidos.")
        elif opcao == "2":
            lista = manager.listar_medicamentos()
            if not lista:
                print("Nenhum medicamento agendado.")
            for item in lista:
                print(f"💊 {item['nome']} - Horário: {item['horario']}")
        elif opcao == "3":
            break


if __name__ == "__main__":
    main()
