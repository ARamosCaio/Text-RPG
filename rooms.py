import actions
import time
import challenges

rooms = ['riddle-room']

def riddle_room():
    actions.tell_story('\n Você adentra nas masmorras abaixo da superfície e após descer pelas escadas você se depara com uma porta de madeira.')
    time.sleep(2)
    actions.tell_story('\n 1. Examinar a porta')
    actions.tell_story('\n 2. Abrir a porta')
    actions.tell_story('\n 3. Abrir a porta e entrar')
    action_door = input('\nO que deseja fazer? : ')
    actions.start_room(action_door)
    actions.tell_story('\n 1. Falar com a Toupeira')
    actions.tell_story('\n 2. Examinar a parede à sua esquerda')
    actions.tell_story('\n 3. Examinar a parede à sua direita')
    actions.tell_story('\n 4. Examinar a parede atrás da toupeira')
    action_room = input('\nO que deseja fazer? : ')

    if action_room == '1':
        actions.tell_story('\nVocê: Olá, estou buscando um tesouro que, diz a lenda, se encontra nas profundezas desta masmorra.')
        actions.tell_story('\nVocê: Mas não consigo ver alguma porta ou caminho que possa mais levar para as partes mais profundas desta masmorra.')
        actions.tell_story('\nToupeira: Jovem aventureiro, sinto um grande potencional em você.\n Por acaso eu conheço o único caminho que leva para o nível mais baixo da masmorra')
        actions.tell_story('\nToupeira: Mas para isso, primeiro você deve responder a uma pergunta.')
        answer = input('\nQuanto mais tiram, maior eu fico, o que sou?\n Resposta: ')
        result = challenges.riddle(answer)
        if result == '1':
            actions.tell_story('\nCorreto! disse a toupeira enquanto se levantava lentamente, revelando embaixo de si um buraco.')
            actions.tell_story('\nToupeira: Aí está aventureiro, como se provou inteligente o bastante, eis o caminho que leva ao tesouro')
            actions.tell_story('\nToupeira: Boa sorte na sua jornada')


