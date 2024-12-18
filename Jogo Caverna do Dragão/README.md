
# 🐉 Jogo Caverna do Dragão

Um jogo baseado na série de desenho animado dos anos 80, **Caverna do Dragão**, desenvolvido como parte de uma prova prática de Programação Orientada a Objetos (POO). O objetivo é simular duelos e interações entre **Mocinhos** e **Vilões**, utilizando conceitos de POO como herança, polimorfismo, encapsulamento e abstração.

---

## 🚀 Funcionalidades

- **Criação de personagens:** Crie mocinhos e vilões com atributos personalizados.
- **Mostrar personagens:** Liste os personagens criados com seus atributos e histórico de batalhas.
- **Duelos:** Inicie combates entre mocinhos e vilões com base nos valores de sorte.
- **Torneios:** Realize torneios com múltiplos personagens até que reste apenas um vencedor.
- **Alimentação:** Alimente personagens para restaurar energia, respeitando as regras de cada tipo.
- **Interação:** Mocinhos podem conversar, e vilões podem zombar, afetando a energia do alvo.
- **Histórico de ações:** Registra os resultados das batalhas e interações para cada personagem.

---

## 🧑‍💻 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Conceitos de POO:** 
  - Herança
  - Polimorfismo
  - Encapsulamento
  - Abstração
  - Duck Typing
- **Modularização:**
  - `personagens.py`: Contém as classes e a lógica dos personagens.
  - `jogo.py`: Contém o menu e a lógica principal do jogo.

---

## 🏗️ Estrutura do Projeto

```
Jogo_Caverna_Dragao/
│
├── personagens.py  # Classes: Personagem, Mocinho, Vilao
├── jogo.py         # Lógica do jogo e menu principal
└── README.md       # Documentação do projeto
```

---

## 🎮 Como Jogar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Jogo_Caverna_Dragao.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd Jogo_Caverna_Dragao
   ```
3. Execute o jogo:
   ```bash
   python jogo.py
   ```

4. Siga as opções do menu principal para criar personagens, iniciar duelos, realizar torneios e interagir.

---

## 📖 Regras do Jogo

### 🎲 Criação de Personagens
- **Atributos:**
  - Nome (string)
  - Energia (10 inicialmente)
  - Sorte (valor aleatório entre 1 e 6)
  - Histórico de batalhas (lista de strings)

### ⚔️ Combate
- Mocinhos e vilões duelam, sorteando valores de sorte:
  - Vencedor: ganha 2 pontos de energia.
  - Perdedor: perde 2 pontos de energia.
  - Empate: ambos perdem 1 ponto de energia.
- Resultados são armazenados no histórico de ambos os personagens.

### 🍴 Alimentação
- Mocinhos ganham 2 pontos de energia.
- Vilões ganham 3 pontos de energia.
- Personagens com energia 0 (mortos) não podem ser alimentados.

### 🤝 Interações
- **Mocinhos:** Conversam, aumentando 1 ponto de energia do alvo.
- **Vilões:** Zombam, reduzindo 1 ponto de energia do alvo.
- Personagens mortos não podem interagir.

---

## 📝 Histórico de Batalhas

- Todas as batalhas e interações são registradas no histórico de cada personagem.
- O histórico pode ser exibido ao listar os personagens.

---

## 📂 Exemplo de Uso

### 🎮 Menu Principal
```text
===- 𝕵𝖔𝖌𝖔 𝕮𝖆𝖛𝖊𝖗𝖓𝖆 𝖉𝖔 𝕯𝖗𝖆𝖌𝖆𝖔 -===
=== 𝕸𝖊𝖓𝖚 𝕻𝖗𝖎𝖓𝖈𝖎𝖕𝖆𝖑 ===
1. Criar personagem
2. Mostrar personagens
3. Iniciar duelo
4. Realizar torneio
5. Alimentar personagem
6. Interagir com outro personagem
7. Sair
```

### 🛡️ Exemplo de Duelo
```text
Herói está lutando contra Vilão Malvado!
Apos um duelo mortal, Vilão Malvado derrotou o Herói em combate!
```

---

## 📚 Aprendizados

Este projeto consolidou os seguintes conceitos de POO:
- Herança para especializar Mocinhos e Vilões a partir de uma classe base.
- Polimorfismo, permitindo que objetos compartilhem métodos como `lutar` e `interagir` de forma distinta.
- Encapsulamento para proteger atributos internos dos objetos.
- Modularização para organização do código em diferentes arquivos.

---

## 👤 Autor

- **Nome:** Lucas G. R. Constancio
- **Contato:** [Seu Email](lucasgabrielrochapro7@gmail.com)
- **GitHub:** [Seu GitHub](https://github.com/lucasrocha777)

---

## 📜 Licença

Este projeto é de uso acadêmico e foi desenvolvido para a disciplina de Programação Orientada a Objetos (UFRR). Licença para fins de aprendizado.
