import random
import os

vitorias = 0
derrotas = 0
empates = 0

nome = input('Digite o nome do jogador: ')

while nome != 'sair':
    os.system('cls')  

    rodadas = int(input('Digite a quantidade de jogadas: '))

    for i in range(rodadas):
        print('===JOGO===')
        print('1 - pedra')
        print('2 - papel')
        print('3 - tesoura')

        jogada = int(input('Sua jogada (1/2/3): '))

        if jogada < 1 or jogada > 3:
            print("Opção inválida. Escolha entre 1, 2 e 3.")
            continue

        computador = random.randint(1, 3)

        if jogada == computador:
            print('EMPATE')
            empates += 1
        elif (jogada == 1 and computador == 3) or (jogada == 2 and computador == 1) or (jogada == 3 and computador == 2):
            print('VITÓRIA!')
            vitorias += 1
        else:
            print('DERROTA')
            derrotas += 1

    print("===JOGO===")
    nome = input('Digite o nome do jogador: ')

print(f'Vitórias: {vitorias}')
print(f'Derrotas: {derrotas}')
print(f'Empates: {empates}')



total_partidas = vitorias + derrotas + empates
print(f'Relatório da Partida:')
print(f'Número total de partidas: {total_partidas}')
print(f'Vitórias: {vitorias}')
print(f'Derrotas: {derrotas}')
print(f'Empates: {empates}')