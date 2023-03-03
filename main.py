import time
import actions
import rooms
import os


# Declarando a lista chracter, espécies, classes e definindo seus atributos
character = []

name = 0

atributes = { 
    "strenght" : 0,   
    "inteligence": 0,
    "agility": 0,
    "endurance": 0
}

breeds = ['Humano', 'Elfo', 'Ciborgue', 'Anfíbio', 'Golem']

classes = ['Guerreiro', 'Caçador', 'Ladrão', 'Druida', 'Mago', 'Bardo']


#Inicio da história, primeira interação com o usuário

print('\n \nOlá aventureiro, seja bem-vindo ao 4-rooms. \n')

#time.sleep(3)

print('Seu objetivo aqui é entrar nas masmorras, enfrentar 4 desafios diferentes em 4 salas aleatórias e encontrar o tesouro!\n')

actions.insert_name()

print('\nPara iniciarmos, escolha sua espécie, sua classe e role o dado de 1 a 20 para sortear seus pontos de FORÇA, INTELIGÊNCIA, AGILIDADE e RESISTÊNCIA \n')

print('Lembrando que cada espécie e cada classe tem seus pontos fortes e fracos, escolha com cuidado!\n')


#time.sleep(10)


character.append(breeds[int(input('1. Humano \n \n2. Elfo \n \n3. Ciborgue \n \n4. Anfíbio \n \n5. Golem \n \nDigite o número da sua raça/espécie: '))-1])

character.append(classes[int(input('\n1. Guerreiro \n \n2. Caçador \n \n3. Ladrão \n \n4. Druida \n \n5. Mago\n \n6. Bardo \n \nDigite o número da sua classe: '))-1])


print('\nVocê é um {} {} \n'.format(character[0], character[1]))


time.sleep(3)

os.system('cls')

print('\nAgora vamos rolar os dados para sortear seus atributos de FORÇA, INTELIGÊNCIA, AGILIDADE e RESISTÊNCIA')
print('\n')

#time.sleep(4)
print('Sorteando.')
#time.sleep(1)
print('Sorteando..')
#time.sleep(1)
print('Sorteando...')
#time.sleep(1)

for atribute in atributes:
    atributes[atribute] = actions.roll_dice()

print('\nParabéns {}! seu {} {} possui os seguintes valores de atributos: '.format(name, character[0], character[1]))
print('\n \n Força: {}'.format(atributes["strenght"]))
print('\n Inteligência: {}'.format(atributes["inteligence"]))
print('\n Agilidade: {}'.format(atributes["agility"]))
print('\n Resistência: {} \n'.format(atributes["endurance"]))

print('\nAgora que você está pronto, esta na hora de enfrentar os desafios e conquistar o tesouro')

time.sleep(10)

os.system('cls')

rooms.riddle_room()