# Desafio Calculadora de Partidas Rankeadas - Formação Lógica de Programação/DIO/Felipão

# Declara uma função de nome "desempenho" que recebe como parâmetros as quantidades de vitórias e de derrotas de um jogador 
# e retorna o resultado da função para a variável "saldo".
def desempenho (vitórias, derrotas):
    saldo = vitórias - derrotas
    return saldo

# Lê os valores das variáveis informados pelo usuário.
vitórias = int(input('Informe o número de vitórias: ').strip())
derrotas = int(input('Informe o número de derrotas: ').strip())

# Cria uma estrutura de decisão para definir o nível do jogador.
saldo = desempenho(vitórias,derrotas)

if saldo < 10:
    nivel = "Ferro"
elif 11 <= saldo <= 20:
     nivel = "Bronze"
elif 21 <= saldo <= 50:
     nivel = "Prata"
elif 51 <= saldo <= 80:
     nivel = "Ouro"
elif 81 <= saldo <= 90:
     nivel = "Diamante"
elif 91 <= saldo <= 100:
     nivel = "Lendário"
elif 101 <= saldo:
     nivel = "Imortal"

print(f'O Herói tem de saldo de {saldo} e está no nível {nivel}')