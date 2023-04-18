import time
import actions
import rooms
import os


atributes = { 
    "strenght" : 0,   
    "inteligence": 0,
    "agility": 0,
    "endurance": 0,
    "luck" : 0
}

breeds = ['Humano', 'Elfo', 'Ciborgue', 'Anfíbio', 'Golem']

classes = ['Guerreiro', 'Caçador', 'Ladrão', 'Druida', 'Mago', 'Bardo']

#Apagando o terminal antes de começar
os.system('clear')

#Inicio da história, primeira interação com o usuário

actions.tell_story('\n \nOlá aventureiro, seja bem-vindo ao Rooms. \n\n')

actions.tell_story('Seu objetivo aqui é entrar nas masmorras, enfrentar os desafios e encontrar o tesouro!\n')

name = actions.insert_name()

actions.tell_story('\nPara iniciarmos, escolha sua espécie, sua classe e role o dado de 1 a 20 para sortear seus pontos de FORÇA, INTELIGÊNCIA, AGILIDADE, RESISTÊNCIA e SORTE\n')

actions.tell_story('\nLembrando que cada espécie e cada classe tem seus pontos fortes e fracos, escolha com cuidado!\n')


time.sleep(3)


character = [
    breeds[int(input('\n1. Humano \n \n2. Elfo \n \n3. Ciborgue \n \n4. Anfíbio \n \n5. Golem \n \nDigite o número da sua raça/espécie: '))- 1],

    classes[int(input('\n1. Guerreiro \n \n2. Caçador \n \n3. Ladrão \n \n4. Druida \n \n5. Mago\n \n6. Bardo \n \nDigite o número da sua classe: '))- 1],
] 

actions.tell_story(f'\nVocê é um {character[0]} {character[1]} \n')


time.sleep(3)

os.system('clear')

actions.tell_story('\nAgora vamos rolar os dados para sortear seus atributos de FORÇA, INTELIGÊNCIA, AGILIDADE, RESISTÊNCIA e SORTE\n')


time.sleep(3)
actions.tell_story('\nSorteando.')
time.sleep(0.5)
actions.tell_story('\nSorteando..')
time.sleep(0.5)
actions.tell_story('\nSorteando...')



for atribute in atributes:
    atributes[atribute] = actions.roll_dice()

actions.tell_story(
    f'\n\nParabéns {name}! você possui os seguintes valores de atributos: '
)
actions.tell_story(f'\n \n Força: {atributes["strenght"]}')
actions.tell_story(f'\n Inteligência: {atributes["inteligence"]}')
actions.tell_story(f'\n Agilidade: {atributes["agility"]}')
actions.tell_story(f'\n Resistência: {atributes["endurance"]}')
actions.tell_story(f'\n Sorte: {atributes["luck"]}\n')

actions.tell_story('\nAgora que você está pronto, esta na hora de enfrentar os desafios e conquistar o tesouro')

time.sleep(7)

os.system('clear')

actions.tell_story('\nVocê adentra nas masmorras abaixo da superfície e após descer pelas escadas você se depara com uma porta de madeira.')

actions.start_room()

rooms.riddle_room()

