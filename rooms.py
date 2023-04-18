import actions
import os

rooms = ['riddle-room']

def riddle_room():
    actions.tell_story('\n\n 1. Falar com a Toupeira')
    actions.tell_story('\n 2. Examinar a parede à sua esquerda')
    actions.tell_story('\n 3. Examinar a parede à sua direita')
    actions.tell_story('\n 4. Examinar a parede atrás da toupeira')
    action_room = input('\n\nO que deseja fazer? : ')
    os.system('cls')

    if action_room == '1':
        actions.tell_story('\n\nVocê: Olá, estou buscando um tesouro que, segundo as lendas, se encontra nas profundezas desta masmorra.')
        actions.tell_story('\nVocê: Mas não consigo ver alguma porta ou caminho que possa me levar para as partes mais profundas desta masmorra.')
        actions.tell_story('\n\nToupeira: Olá jovem aventureiro, sim sim, existe um tesouro nesta masmorra.\nToupeira: Ele pode ser encontrado no úitimo nível e por acaso eu conheço o um caminho que leva para o próximo andar.')
        actions.tell_story('\nToupeira: Mas para isso, primeiro você deve solucionar um enigma.')
        actions.riddle_interaction()
    
    elif action_room == '2':
        actions.tell_story('\nVocê se aproxima da parede da esquerda. \nEstá coberta de musgo e bastante úmida, existem alguns buracos nos quais alguns ratos se escondem quando você se aproxima.')
        riddle_room()

    elif action_room == '3':
        actions.tell_story('\nVocê se aproxima da parede da direita. \nNela você consegue percerber marcas de unha e manchas escuras nos elos das correntes que inibiam os movimentos dos prisioneiros.')
        actions.tell_story('\nHá também pequenos insetos caminhando sobre a parede e pequenos tufos de grama, que insistem em crescer se aproveitando da luz vacilante que entra por buracos no teto.')         
        actions.tell_story('\nVocê se pergunta como os prisioneiros conseguiam sobreviver naquelas condições e além disso, como conseguiram escapar...')
        riddle_room()

    elif action_room == '4':
        actions.tell_story('\nA toupeira é tão grande que sua cabeça por pouco não toca o teto e mesmo estando no centro da sala retangular, ocupa quase todo o espaço lateral.')
        actions.tell_story('\nHá apenas um espaço de aproximadamente um metro entre ela e as paredes.\nVocê caminha por este espaço em busca verificar o que há atrás da toupeira.')
        actions.tell_story('\nPara sua amarga surpresa, tudo que você vê é uma parede de pedra semelhante as demais, aparentemente maciça e nada que indique uma porta secreta ou caminho alternativo.')
        riddle_room()
    
    
