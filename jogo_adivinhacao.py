import random

# Função para gerar o número secreto
def gerar_numero_secreto():
    return random.randint(1, 100)

# Função para dar dicas ao usuário
def dar_dica(numero_secreto, palpite):
    if palpite < numero_secreto:
        return "Tente um número maior!"
    else:
        return "Tente um número menor!"

# Função principal do jogo
def jogo_adivinhacao():
    numero_secreto = gerar_numero_secreto()
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Você tem {max_tentativas} tentativas para adivinhar o número secreto entre 1 e 100.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            break
        else:
            print(dar_dica(numero_secreto, palpite))
            print(f"Tentativas restantes: {max_tentativas - tentativas}")

    if tentativas == max_tentativas:
        print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")

# Iniciar o jogo
jogo_adivinhacao()