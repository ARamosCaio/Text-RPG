import random
import time
import os
import sys
import challenges

# função que printa a história letra por letra para melhor efeito visual
def tell_story(sentence):
    for letter in sentence :
        print(letter, end='')
        time.sleep(0.035)
        sys.stdout.flush()

#conta o fim da história
def tell_end(sentence):
    for letter in sentence :
        print(letter, end='')
        time.sleep(0.3)
        sys.stdout.flush()


# função que permite que o usuário corrija seu nome caso tenha escrito errado e após isso confirme
def insert_name():
    name = input('\nQual o seu nome aventureiro? : ')
    confirm = input('\nVocê é {}? \n\n1. Sim  2. Não\n'.format(name))
    if confirm == '1':
        return name
    elif confirm == '2':
        return insert_name()
    else:
        print('\nInsira apenas os valores 1 ou 2\n')
        return insert_name()    

# função rolar dado d20 comum
def roll_dice():
    return random.randrange(1,20)

#por enquanto essa ação esta serve apenas para a riddle room, adicionar posteriormente personalização para cada sala

def start_room():
    time.sleep(2)
    tell_story('\n\n 1. Examinar a porta')
    tell_story('\n 2. Abrir a porta')
    tell_story('\n 3. Abrir a porta e entrar')
    action_door = input('\n\nO que deseja fazer? : ')
    if action_door == '1':
        tell_story('\n \nUma porta de tábuas de madeira escura, levemente mofada e gasta com detalhes em metal nas pontas das tábuas. A porta não possui maçaneta. \nAcima do batente da porta esta engravada a seguinte frase: "Omnes homines natura scientiam quaerunt"\nEsta porta não aparenta ser muito resistente.\n')
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
        action_door = input('\n\nO que deseja fazer? : ')
        if action_door == '1':
            os.system('cls')
            tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra.\nÀ sua frente está a Sra. Toupeira, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.')
    
    elif action_door == '3':
        os.system('cls')
        tell_story('\nVocê entra na sala retangular de paredes de pedra com musgo e chão de terra. \nÀ sua frente está uma toupeira gigante, que aparenta já ter uma idade avançada, sentada no centro da sala tomando um chá recém preparado na fogueira que se encontra diante dela.\nÀ sua esquerda está uma parede de pedra coberta de musgo e úmida. \nÀ sua direita está uma parede semelhante com correntes fixadas firmemente, porém com os elos quebrados como se os prisioneiros tivessem escapado.') 
    
    else:
        tell_story('Insira um valor válido (1, 2 ou 3)')
        start_room()

def riddle_interaction():
    answer = input('\nToupeira: Responda aventureiro: "Quanto mais tiram, maior eu fico, o que sou?"\n \nResposta: ')
    result = challenges.riddle(answer)
    if result == '1':
        tell_story('\n\nCorreto! disse a toupeira enquanto se levantava lentamente, revelando embaixo de si um buraco.')
        tell_story('\n\nToupeira: Aí está aventureiro, como se provou inteligente o bastante, eis o caminho para a proxima sala, que leva ao tesouro')
        tell_story('\n\nToupeira: Boa sorte na sua jornada\n')
        time.sleep(3)
        os.system('cls')
        tell_story('\nSeguindo a informação da toupeira, você desce pelo buraco e segue o caminho pouco iluminado até conseguir enxergar uma fonte de luz que marca a saída do túnel')
        time.sleep(6)
        finish_game()
    elif result =='2':
        tell_story('\nToupeira: Errado! Pense mais um pouco meu jovem!')
        riddle_interaction()


def finish_game():
    tell_story('\nVocê se depara com uma porta de pedra, com a figura de um leão esculpida no batente')
    time.sleep(2)
    tell_story('\nAo se aproximar do portal uma energia de cor azulada emana do chão ao seu redor, subindo em direção à figura do leão, entrando pela boca e preenchendo os olhos vazios com uma tom azul brilhante como de uma safira')
    time.sleep(2)
    tell_story('\nEnquanto você observa maravilhado, uma voz calma, quase sussurrada. ecoa partindo da boca do leão se espalhando por toda a sala.\n "Inclitus"')
    time.sleep(2)
    tell_story('\nA porta se abre e o brilho de todo o ouro presente na câmara o cega por um momento, você conseguiu! ')
    time.sleep(2)
    tell_story('\nNa parede da sala há uma inscrição que diz: \n "A aquele que chegou ao final dos desafios, INCLITUS, deixo a você o meu tesouro e mais um presente.')
    time.sleep(0.5)
    tell_story('\nProfira a palavra "Celare" para ocultar todo o tesouro dentro de suas botas, voce não sentirá sua presença mas ele estará contigo')
    time.sleep(0.5)
    tell_story('\nFeito isso, imagine o local mais seguro em que ja esteve e profira a frase "Post Questus Relinquo" e você e o tesouro serão instantaneamente transportados para lá.')
    time.sleep(0.5)
    tell_story('\nPara que o tesouro reapareça, basta proferir a palavra "Comparuit". \n A inscrição está assinada por Firio, o ganancioso')
    time.sleep(2)
    tell_story('\nVocê segue as intruções da inscrição e leva consigo toda a riqueza da sala, use-a com sabedoria')
    time.sleep(4)
    tell_end('\n\n\n FIM!\n\n\n')