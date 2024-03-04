#Desafio Classificador de nível de herói - Formação Lógica de Programação/DIO/Felipão

#Ler o nome digitado e guardar na variável "Nome".
Nome=input('Digite um nome para o seu herói: ').strip()

#Ler o valor informado e guardar na variável "XP".
XP=int(input('Quantos pontos de experiência (XP) o seu herói acumulou? ').strip())

#Classificar o herói com base no total de XP acumulada.
if XP < 1001:
    nivel = "Ferro"
elif 1001 <= XP <= 2000:
     nivel = "Bronze"
elif 2001 <= XP <= 5000:
    nivel = "Prata"
elif 5001 <= XP <= 7000:
    nivel = "Ouro"
elif 7001 <= XP <= 8000:
    nivel = "Platina"
elif 8001 <= XP <= 9000:
    nivel = "Ascendente"
elif 9001 <= XP <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"
        
#Mostrar na tela mensagem informando o nome e o nível do herói.
print(f'O herói de nome {Nome} tem {XP}XP e está no nível {nivel}.')