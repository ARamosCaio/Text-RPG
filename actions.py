import random
import time
import os
import sys

# função que printa a história letra por letra para melhor efeito visual
def tell_story(sentence):
    for letter in sentence :
        print(letter, end='')
        time.sleep(0.035)
        sys.stdout.flush()


# função que permite que o usuário corrija seu nome caso tenha escrito errado e após isso confirme
def insert_name():
    name = input('\nQual o seu nome aventureiro? : ')
    confirm = input('\nVocê é {}? \n\n1. Sim  2. Não\n'.format(name))
    if confirm == '1':
        return name
    elif confirm == '2':
        return insert_name()
    

# função rolar dado d20 comum
def roll_dice():
    return random.randrange(1,20)

#por enquanto essa ação esta serve apenas para a riddle room, adicionar posteriormente personalização para cada sala

def start_room(action_door):
    if action_door == '1':
        tell_story('\n \nUma porta de tábuas de madeira escura, levemente mofada e gasta com detalhes em metal nas pontas das tábuas. A porta não possui maçaneta. \nAcima do batente da porta esta engravada a seguinte frase: "Omnes homines natura scientiam quaerunt"\nEsta porta não aparenta ser muito resistente.')
        time.sleep(2)
        tell_story('\n 1. Abrir a porta')
        tell_story('\n 2. Abrir a porta e entrar')
        action_door = input('\nO que deseja fazer? : ')
        if action_door == '1':
            os.system('cls')
            tell_story('\nVocê abre a porta com cautela sem entrar e observa o interior da sala. \nAlém das paredes velhas, marcadas pela passagem do tempo e pelo desespero dos prisioneiros da masmorra você observa a presença inusitada de um ser sentado no centro da sala: Uma Toupeira Velha Gigante')
            tell_story('\nEnquanto você observa a sala por alguns segundos, a Sra. toupeira lhe diz "Entre aventureiro, não tenha medo, se aproxime para conversarmos"')
            time.sleep(2)
            tell_story('\n1. Entrar')
            action_door = input('\nO que deseja fazer? : ')
            if action_door == '1':
                os.system('cls')
                tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra. \nÀ sua frente está a Sra. Toupeira, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.')
                
        elif action_door == '2':
            os.system('cls')
            tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra. \nÀ sua frente está a Sra. Toupeira, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.')
    
    elif action_door == '2':
        os.system('cls')
        tell_story('\nVocê abre a porta com cautela sem entrar e observa o interior da sala. \n Além das paredes velhas, marcadas pela passagem do tempo e pelo desespero dos prisioneiros da masmorra você observa a presença inusitada de um ser sentado no centro da sala: Uma Toupeira Velha Gigante')
        tell_story('\nEnquanto você observa a sala por alguns segundos, a Sra. toupeira lhe diz "Entre aventureiro, não tenha medo, se aproxime para conversarmos"')
        time.sleep(2)
        tell_story('\n 1. Entrar')
        action_door = input('O que deseja fazer? : ')
        if action_door == '1':
            os.system('cls')
            tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra.\nÀ sua frente está a Sra. Toupeira, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.')
    
    elif action_door == '3':
        os.system('cls')
        tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra. \nÀ sua frente está a Sra. Toupeira, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.') 