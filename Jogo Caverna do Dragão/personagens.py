#by Lucas Rocha 777

import random
import time

class Personagem:
    def __init__(self, nome, sorte, energia=10):
        self._nome = nome
        self._energia = energia
        self._sorte = sorte
        self._historico = []

    @property
    def nome(self):
        return self._nome

    @property
    def energia(self):
        return self._energia

    @property
    def sorte(self):
        return self._sorte

    @property
    def historico(self):
        return self._historico

    def incremento(self, quantidade):
        #Aumenta a energia do personagem.
        self._energia += quantidade

    def decremento(self, quantidade):
        #Diminui a energia do personagem, garantindo que não fique negativa.
        self._energia -= quantidade
        if self._energia < 0:
            self._energia = 0

    def sortear_sorte(self):
        #Sorteia um valor de sorte entre 1 e 6.
        return random.randint(1, 6)

    def adicionar_historico(self, mensagem):
        #Adiciona uma mensagem ao histórico do personagem.
        self._historico.append(mensagem)


class Mocinho(Personagem):
    def __init__(self, nome, sorte, energia=10):
        super().__init__(nome, sorte, energia)

    def alimentar(self):
        #Aumenta a energia em 2 pontos.
        if self._energia <= 0:
            mensagem = f"{self._nome} está morto e não pode ser alimentado!"
            time.sleep(2)
        else:
            self.incremento(2)
            mensagem = f"{self._nome} se alimentou e ganhou 2 pontos de energia!"
        self.adicionar_historico(mensagem)
        time.sleep(2)
        return mensagem

    def lutar(self, outro):
        #Realiza um combate entre o mocinho e outro personagem.
        resultado = self.sortear_sorte()
        outro_resultado = outro.sortear_sorte()
    
        if resultado > outro_resultado:
            self.incremento(2)
            outro.decremento(2)
            mensagem = f"Apos um arduo combate, {self._nome} derrotou o {outro._nome} em batalha !"

        elif resultado < outro_resultado:
            self.decremento(2)
            mensagem = f"{self._nome} perdeu o combate para {outro._nome}."

        else:
            self.decremento(1)
            outro.decremento(1)
            mensagem = f"O duelo entre {self._nome} e {outro._nome} terminou em empate!"
        
        self.adicionar_historico(mensagem)
        outro.adicionar_historico(mensagem)
        return mensagem

    def interagir(self, outro_personagem):
        if self._energia <= 0:
            mensagem = f"{self._nome} esta morto e não pode interagir!"
        else:
            outro_personagem.incremento(1)  # Mocinho aumenta energia do alvo
            mensagem = f"{self._nome} conversou amigavelmente com {outro_personagem._nome}."
        self.adicionar_historico(mensagem)
        outro_personagem.adicionar_historico(mensagem)
        return mensagem



class Vilao(Personagem):
    def __init__(self, nome, sorte, energia=10):
        super().__init__(nome, sorte, energia)

    def alimentar(self):
        # Aumenta a energia em 3 pontos.
        if self._energia <= 0:
            mensagem = f"{self._nome} está morto e não pode ser alimentado!"
            time.sleep(2)
        else:
            self.incremento(3)
            mensagem = f"{self._nome} se alimentou e ganhou 3 pontos de energia!"
        self.adicionar_historico(mensagem)
        time.sleep(2)
        return mensagem

    def lutar(self, outro):
        # Realiza um combate entre o vilão e outro personagem.
        resultado = self.sortear_sorte()
        outro_resultado = outro.sortear_sorte()
        
        if resultado > outro_resultado:
            self.incremento(2)
            outro.decremento(2)
            mensagem = f"Apos um duelo mortal, {self._nome} derrotou o {outro._nome} em combate!"
        elif resultado < outro_resultado:
            self.decremento(2)
            mensagem = f"{self._nome} foi derrotado por {outro._nome} em batalha."
        else:
            self.decremento(1)
            outro.decremento(1)
            mensagem = f"O duelo entre {self._nome} e {outro._nome} terminou em empate!"

        self.adicionar_historico(mensagem)
        outro.adicionar_historico(mensagem)
        return mensagem

    def interagir(self, outro_personagem):
        # Vilão zomba do outro personagem, reduzindo sua energia.
        if self._energia <= 0:
            mensagem = f"{self._nome} está morto e não pode interagir!"
        else:
            outro_personagem.decremento(1)
            mensagem = f"{self._nome} zombou de {outro_personagem._nome}, tirando 1 ponto de energia!"
        self.adicionar_historico(mensagem)
        outro_personagem.adicionar_historico(mensagem)
        return mensagem

