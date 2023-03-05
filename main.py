import time
import actions
import rooms
import os


# Declarando a lista chracter, espécies, classes e definindo seus atributos
character = []

atributes = { 
    "strenght" : 0,   
    "inteligence": 0,
    "agility": 0,
    "endurance": 0
}

breeds = ['Humano', 'Elfo', 'Ciborgue', 'Anfíbio', 'Golem']

classes = ['Guerreiro', 'Caçador', 'Ladrão', 'Druida', 'Mago', 'Bardo']

#Apagando o terminal antes de começar
os.system('cls')

#Inicio da história, primeira interação com o usuário

actions.tell_story('\n \nOlá aventureiro, seja bem-vindo ao Rooms. \n\n')

#time.sleep(3)

actions.tell_story('Seu objetivo aqui é entrar nas masmorras, enfrentar os desafios e encontrar o tesouro!\n')

name = actions.insert_name()

actions.tell_story('\nPara iniciarmos, escolha sua espécie, sua classe e role o dado de 1 a 20 para sortear seus pontos de FORÇA, INTELIGÊNCIA, AGILIDADE e RESISTÊNCIA \n')

print('Lembrando que cada espécie e cada classe tem seus pontos fortes e fracos, escolha com cuidado!\n')


#time.sleep(4)


character.append(breeds[int(input('1. Humano \n \n2. Elfo \n \n3. Ciborgue \n \n4. Anfíbio \n \n5. Golem \n \nDigite o número da sua raça/espécie: '))-1])

character.append(classes[int(input('\n1. Guerreiro \n \n2. Caçador \n \n3. Ladrão \n \n4. Druida \n \n5. Mago\n \n6. Bardo \n \nDigite o número da sua classe: '))-1])


actions.tell_story('\nVocê é um {} {} \n'.format(character[0], character[1]))


time.sleep(3)

os.system('cls')

actions.tell_story('\nAgora vamos rolar os dados para sortear seus atributos de FORÇA, INTELIGÊNCIA, AGILIDADE e RESISTÊNCIA\n')


#time.sleep(3)
actions.tell_story('\nSorteando.')
#time.sleep(1)
actions.tell_story('\nSorteando..')
#time.sleep(1)
actions.tell_story('\nSorteando...')
#time.sleep(1)

for atribute in atributes:
    atributes[atribute] = actions.roll_dice()

actions.tell_story('\n\nParabéns {}! você possui os seguintes valores de atributos: '.format(name))
actions.tell_story('\n \n Força: {}'.format(atributes["strenght"]))
actions.tell_story('\n Inteligência: {}'.format(atributes["inteligence"]))
actions.tell_story('\n Agilidade: {}'.format(atributes["agility"]))
actions.tell_story('\n Resistência: {} \n'.format(atributes["endurance"]))

actions.tell_story('\nAgora que você está pronto, esta na hora de enfrentar os desafios e conquistar o tesouro')

time.sleep(7)

os.system('cls')

actions.tell_story('\nVocê adentra nas masmorras abaixo da superfície e após descer pelas escadas você se depara com uma porta de madeira.')

actions.start_room()

rooms.riddle_room()

