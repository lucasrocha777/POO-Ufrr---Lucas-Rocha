""" 
    Atividade Tratamento de Exceções
    Discente: Lucas Gabriel
"""

from datetime import datetime
import time

# Erro para quando o livro estiver indisponivel para aluguel
class LivroIndisponivelError(Exception):
    def __init__(self, titulo_livro, motivo):
        self.titulo_livro = titulo_livro
        self.motivo = motivo
        mensagem_erro = f"O liver {titulo_livro} não pode ser alugado pois: {motivo}!"
        super().__init__(mensagem_erro)

# Erro para devolução invalida do livro
class DevolucaoInvalidaError(Exception):
    def __init__(self, nome_usuario, livro):
        self.nome_usuario = nome_usuario
        self.livro = livro
        mensagem_erro = f"{nome_usuario} tentou devolver o livro {livro}, mas ele não alugou esse livro!"
        super().__init__(mensagem_erro)

# Erro para o atraso na devolução do livro
class EmprestimoAtrasadoError(Exception):
    def __init__(self, nome_usuario, livro, quant_dias_atrasa):
        self.nome_usu = nome_usuario
        self.livro = livro
        self.dias_atrasados = quant_dias_atrasa
        multa = quant_dias_atrasa*2.50
        mensagem_erro = f"{nome_usuario} devolveu o livro {livro} com {quant_dias_atrasa} dias atrasados, resultando numa multa de: {multa:.2f}"
        super().__init__(mensagem_erro)


class Biblioteca_sys:
    def __init__(self):
        self.prateleira_livros = {'Python Iniciantes': 2, 'Python Intermediario': 2,
                                  'Python Avancado': 2, 'POO em Python I': 2, 
                                  'POO em Python II':2, 'POO em Python III': 2}
        
# Metodo para adicionar livros a prateleira de livros disponiveis na biblioteca
    def add_livro(self, titulo, quantidade):
        if not isinstance(titulo, str):# Verifica se o titulo do livro está em string mesmo, se não estiver lança um TypeError
            raise TypeError("O titulo do livro tem que ser uma String.")
        
        if titulo in self.prateleira_livros:
            self.prateleira_livros[titulo] += quantidade
        else:
            self.prateleira_livros[titulo] = quantidade


# Esse metodo verifica a disponibilidade de livros na prateleira
    def disponibilidade_livros(self, titulo):
        return self.prateleira_livros.get(titulo, 0) > 0

# Este metodo remove 1 unidade do livro na prateleira de livros
    def emprestar_livro(self, titulo):
        if not self.disponibilidade_livros(titulo):
            raise LivroIndisponivelError(titulo, "Já está emprestado ou reservado")
        self.prateleira_livros[titulo] -= 1

# Acrescenta o livro de novo na prateleira de livros
    def devolver_livro(self, titulo):
        if titulo in self.prateleira_livros:
            self.prateleira_livros[titulo] += 1
        else:
            self.prateleira_livros[titulo] = 1


class Usuario:
    def __init__(self, nome, email, numero_contato, biblioteca):
        self.nome = nome
        self.email = email
        self.numero_contato = numero_contato
        self.biblioteca = biblioteca
        self.livros_alugados = {}
        self._historico = []

    def historico(self):
        return self._historico
    
    def add_historico(self, mensagem):
        self._historico.append(mensagem)

    def emprestimo_livro(self, livro):
        try:
            if not isinstance(livro, str): # Verifica se o titulo do livro está em string mesmo, se não estiver lança um TypeError
                raise TypeError("O titulo do livro deve ser uma String.")

            self.biblioteca.emprestar_livro(livro)
            self.livros_alugados[livro] = datetime.now()
            print(f"O {self.nome} pegou o livro {livro} alugado.")
            mensagem=(f"O {self.nome} pegou o livro {livro} alugado.")
            self.add_historico(mensagem)
        except LivroIndisponivelError as e:
            print(e)
        except TypeError as e:
            print(e)


    def devolucao_livro(self, livro):
        try:
            if livro not in self.livros_alugados:
                raise DevolucaoInvalidaError(self.nome, livro)
        
            data_emprestimo = self.livros_alugados.pop(livro)
            dias_atraso = (datetime.now() - data_emprestimo).days

            if dias_atraso > 0:
                raise EmprestimoAtrasadoError(self.nome, livro, dias_atraso)
        
            self.biblioteca.devolver_livro(livro)
            print(f"O {self.nome} devolveu o livro {livro} sem atraso!")
            self.add_historico(mensagem=(f"O {self.nome} devolveu o livro {livro} sem atraso!"))

        except (DevolucaoInvalidaError, EmprestimoAtrasadoError) as e:
            print(e)
        except Exception:
            print("Erro inesperado! Entre em contato com a adiminstração da biblioteca.")

def menu():
    print("===================================")
    print("=== 📚 Sistema de Biblioteca ===")
    print("1. Cadastrar Usuário")
    print("2. Emprestar Livro")
    print("3. Devolver Livro")
    print("4. Adicionar Livro à Biblioteca")
    print("5. Verificar Disponibilidade de um Livro")
    print("6. Ver historico do Usuario")
    print("7. Sair")

def main():
    biblioteca = Biblioteca_sys()
    usuarios = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Cadastrar usuário
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            usuarios[nome] = Usuario(nome, email, telefone, biblioteca)
            print(f"Usuário {nome} cadastrado com sucesso!")
            time.sleep(2)

        elif opcao == "2":  # Emprestar livro
            nome = input("Nome do usuário: ")
            if nome in usuarios:
                livro = input("Título do livro: ")
                usuarios[nome].emprestimo_livro(livro)
                time.sleep(2)
            else:
                print("Usuário não encontrado!")
                time.sleep(2)

        elif opcao == "3":  # Devolver livro
            nome = input("Nome do usuário: ")
            if nome in usuarios:
                livro = input("Título do livro: ")
                usuarios[nome].devolucao_livro(livro)
                time.sleep(2)
            else:
                print("Usuário não encontrado!")
                time.sleep(2)

        elif opcao == "4":  # Adicionar livro à biblioteca
            titulo = input("Título do livro: ")
            try:
                quantidade = int(input("Quantidade: "))
                biblioteca.add_livro(titulo, quantidade)
                print(f"{quantidade} cópia(s) do livro '{titulo}' adicionadas à biblioteca.")
                time.sleep(2)
            except ValueError:
                print("Erro: Digite um número válido para a quantidade.")
                time.sleep(2)

        elif opcao == "5":  # Verificar disponibilidade de um livro
            titulo = input("Título do livro: ")
            if biblioteca.disponibilidade_livros(titulo):
                print(f"O livro '{titulo}' está disponível para empréstimo.")
                time.sleep(2)
            else:
                print(f"O livro '{titulo}' está indisponível no momento.")
                time.sleep(2)

        elif opcao == "6":  # Exibi o historico do usuario
            nome_usuario = input("Digite o nome do Usuario: ")
            if nome_usuario in usuarios:
                historico = usuarios[nome_usuario].historico()
                if historico:
                    print(f"Historico do Ususario {nome_usuario}:\n")
                    time.sleep(1)
                    for evento in historico:
                        print(f"- {evento}")

                else:
                    print("Usuario ainda não possui historico!")
                    time.sleep(2)
            else:
                print(f"Usuario {nome_usuario} não encontrado.")
            time.sleep(2)

        elif opcao == "7":  
            print("Saindo do sistema de biblioteca. Até logo!")
            time.sleep(2)
            break

        else:
            print("Opção inválida! Escolha uma opção entre 1 e 6.")
            time.sleep(2)
# Chamando a função principal
if __name__ == "__main__":
    main()
