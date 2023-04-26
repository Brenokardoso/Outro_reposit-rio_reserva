import random

def cria_tabuleiro():
    return [""] * 9

def mostra_tabuleiro(tabuleiro):
    print(f"|{tabuleiro[0]}|{tabuleiro[1]}|{tabuleiro[2]}|")
    print("-"*9)
    print(f"|{tabuleiro[3]}|{tabuleiro[4]}|{tabuleiro[5]}|")
    print("-"*9)
    print(f"|{tabuleiro[6]}|{tabuleiro[7]}|{tabuleiro[8]}|")

def faz_jogada(tabuleiro, posicao, caractere):
    posicao = posicao - 1
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = caractere
        return True
    else:
        return False

def escolhe_posicao(tabuleiro):
    posicoes_vazias = []
    for i in range(0,9):
        if tabuleiro[i] == " ":
            posicoes_vazias.append(i)
    return random.choice(posicoes_vazias)

def verifica_vencedor(tabuleiro):
    combinacoes_vencedoras = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)
    ]
    
    for c1, c2, c3 in combinacoes_vencedoras:
        if tabuleiro[c1] == tabuleiro[c2] == tabuleiro[c3] != "":
            return True
    return False

def jogo():
    tabuleiro = cria_tabuleiro()
    jogadores = ["X", "O"]
    jogador_atual = jogadores[0]
    jogador1 = "Jogador 1"
    jogador2 = "Máquina"
    mostra_tabuleiro(tabuleiro)
    
    while True:
        if jogador_atual == jogador1:
            posicao = int(input(f"{jogador_atual}, digite a posição (1-9): "))
        else:
            posicao = escolhe_posicao(tabuleiro) + 1
            print(f"{jogador2} escolheu a posição {posicao}")
        if faz_jogada(tabuleiro, posicao, jogador_atual):
            mostra_tabuleiro(tabuleiro)
            
            if verifica_vencedor(tabuleiro):
                print(f"{jogador_atual} ganhou!")
                break
            
            jogador_atual = jogadores[(jogadores.index(jogador_atual) + 1) % 2]
            
            if jogador_atual == jogadores[0]:
                jogador_atual = jogador1
            else:
                jogador_atual = jogador2
                
        else:
            print("Posição inválida. Tente novamente.")

jogo()
