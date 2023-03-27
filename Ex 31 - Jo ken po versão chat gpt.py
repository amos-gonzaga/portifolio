import random

print("Vamos jogar Jo-ken-po!")
jogadas = ["Pedra", "Papel", "Tesoura"]
jogador = int(input("Escolha 1 para Pedra, 2 para Papel, ou 3 para Tesoura: ")) - 1
maquina = random.randint(0, 2)

if jogador == maquina:
    print(f"Você e a máquina jogaram {jogadas[jogador]}, jogo empatado!")
elif (jogador - maquina) % 3 == 1:
    print(f"{jogadas[maquina]} vence {jogadas[jogador]}, você perdeu!")
else:
    print(f"{jogadas[jogador]} vence {jogadas[maquina]}, você venceu!")
