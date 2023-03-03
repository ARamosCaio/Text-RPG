import actions
import time

rooms = ['riddle-room']

def riddle_room():
    print('\n Você adentra nas masmorras abaixo da superfície e após descer pelas escadas você se depara com uma porta de madeira.')
    time.sleep(2)
    print('\n 1. Examinar a porta')
    print('\n 2. Abrir a porta')
    print('\n 3. Abrir a porta e entrar')
    action_door = input('\nO que deseja fazer? : ')
    actions.start_room(action_door)
    print('\n 1. Falar com a Toupeira')
    print('\n 2. Examinar a parede à sua esquerda')
    print('\n 3. Examinar a parede à sua direita')
    print('\n 4. Examinar a parede atrás da toupeira')
    action_room = input('O que deseja fazer? : ')