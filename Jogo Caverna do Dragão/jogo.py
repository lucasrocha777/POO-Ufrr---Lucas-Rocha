#by Lucas Rocha 777

from personagens import Mocinho, Vilao
import random
import time

def menu():
    print("===- 𝕵𝖔𝖌𝖔 𝕮𝖆𝖛𝖊𝖗𝖓𝖆 𝖉𝖔 𝕯𝖗𝖆𝖌𝖆𝖔 -===")
    print("================================")
    print("   ===== 𝕸𝖊𝖓𝖚 𝕻𝖗𝖎𝖓𝖈𝖎𝖕𝖆𝖑 =====")
    print("   |1. 𝕮𝖗𝖎𝖆𝖗 𝖕𝖊𝖗𝖘𝖔𝖓𝖆𝖌𝖊𝖒")
    print("   |2. 𝕸 𝖔𝖘𝖙𝖗𝖆𝖗 𝖕𝖊𝖗𝖘𝖔𝖓𝖆𝖌𝖊𝖓𝖘")
    print("   |3. 𝕴𝖓𝖎𝖈𝖎𝖆𝖗 𝖉𝖚𝖊𝖑𝖔")
    print("   |4. 𝕽𝖊𝖆𝖑𝖎𝖟𝖆𝖗 𝖙𝖔𝖗𝖓𝖊𝖎𝖔")
    print("   |5. 𝕬 𝖑𝖎𝖒𝖊𝖓𝖙𝖆𝖗 𝖕𝖊𝖗𝖘𝖔𝖓𝖆𝖌𝖊𝖒")
    print("   |6. 𝕴 𝖓𝖙𝖊𝖗𝖆𝖌𝖎𝖗 𝖈𝖔𝖒 𝖔𝖚𝖙𝖗𝖔 𝖕𝖊𝖗𝖘𝖔𝖓𝖆𝖌𝖊𝖒")
    print("   |7. 𝕾 𝖆𝖎𝖗")

def main():
    personagens = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do personagem: ")
            tipo = input("Tipo (Mocinho/Vilao): ").lower()
            sorte = random.randint(1, 6)  # Sorte gerada automaticamente

            if tipo == "mocinho":
                personagens.append(Mocinho(nome, sorte))
                print(f"Personagem Mocinho '{nome}' criado com sorte {sorte}.")
                time.sleep(2)
            elif tipo == "vilao":
                personagens.append(Vilao(nome, sorte))
                print(f"Personagem Vilão '{nome}' criado com sorte {sorte}.")
                time.sleep(2)
            else:
                print("Tipo inválido!")
                time.sleep(2)

        elif opcao == "2":
            if len(personagens) > 0:
                for p in personagens:
                    print(f"\nNome: {p.nome}, Energia: {p.energia}, Sorte: {p.sorte}")
                    print("Histórico:")
                    for evento in p.historico:
                        print(f" - {evento}")
                    time.sleep(1)
            else:
                print("Nenhum personagem criado ainda.")
                time.sleep(2)


        elif opcao == "3":
            if len(personagens) < 2:
                print("Crie ao menos 2 personagens.")
                time.sleep(2)
            else:
                p1 = personagens[0]
                p2 = personagens[1]
                print(p1.lutar(p2))
                time.sleep(2)

        elif opcao == "4":
            print("Torneio iniciado...")
            time.sleep(1)
            while len(personagens) > 1:
                p1, p2 = random.sample(personagens, 2)
                print(f"\n{p1.nome} está lutando contra {p2.nome}!")
                time.sleep(1)
                print(p1.lutar(p2))

                # Remover personagens com energia 0
                if p1.energia == 0:
                    personagens.remove(p1)
                    print(f"{p1.nome} foi eliminado do torneio!")

                if p2.energia == 0:
                    personagens.remove(p2)
                    print(f"{p2.nome} foi eliminado do torneio!")


            vencedor = personagens[0]
            print(f"\nO vencedor do torneio é: {vencedor.nome} com {vencedor.energia} pontos de energia!")
            print("Histórico de batalhas:")
            time.sleep(2)
            for mensagem in vencedor.historico:
                print(mensagem)


        elif opcao == "5":
            nome = input("Nome do personagem a alimentar: ")
            for p in personagens:
                if p.nome == nome:
                    p.alimentar()
                    print(f"{p.nome} foi alimentado. Energia: {p.energia}")
                    time.sleep(2)

        elif opcao == "6":
            nome1 = input("Nome do personagem que interage: ")
            nome2 = input("Nome do outro personagem: ")
            p1 = next((p for p in personagens if p.nome == nome1), None)
            p2 = next((p for p in personagens if p.nome == nome2), None)
            if p1 and p2:
                print(p1.interagir(p2))
                time.sleep(3)
            else:
                print("Personagem não encontrado.")
                time.sleep(2)

        elif opcao == "7":
            print("Saindo do jogo...")
            time.sleep(2)
            break

        else:
            print("Opção inválida!")
            time.sleep(2)

if __name__ == "__main__":
    main()
