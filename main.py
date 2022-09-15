#Import librerias
import time

#Declaración de constantes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

#Variables globales de estado
questions = [{
    'question':
    '¿En que pais y año se celebro la primera Copa Mundial de Futbol?',
    'options': {
        'a': {
            'id': 'a',
            'option': 'Italia 1934',
            'message': 'Italia 1934 fue la segunda Copa Mundial de Futbol'
        },
        'b': {
            'id': 'b',
            'option': 'Brasil 1950',
            'message': 'Brasil 1950 fue la cuarta Copa Mundial de Futbol'
        },
        'c': {
            'id': 'c',
            'option': 'Uruguay 1930',
            'message': 'Muy Bien'
        },
        'd': {
            'id': 'd',
            'option': 'Francia 1938',
            'message': 'Francia 1938 fue la tercera Copa Mundial de Futbol'
        }
    },
    'answer': 'c',
    'gain': 10,
    'penalty': 5
}, {
    'question': 'Cual es el país que posee mas copas mundiales de Futbol?',
    'options': {
        'a': {
            'id':
            'a',
            'option':
            'Argentina',
            'message':
            'Argentina solo posee dos Copas Mundiales de Futbol (Argentina 78 y Mexico 86)'
        },
        'b': {
            'id':
            'b',
            'option':
            'Italia',
            'message':
            'Italia solo posee cuatro Copas Mundiales de Futbol (Italia 34, Francia 38, España 86 y Alemania 2006)'
        },
        'c': {
            'id':
            'c',
            'option':
            'Alemania',
            'message':
            'Alemania solo posee cuatro Copas Mundiales de Futbol (Suiza 54, Alemania 74, Italia 90 y Brasil 2014)'
        },
        'd': {
            'id': 'd',
            'option': 'Brasil',
            'message': 'Muy Bien'
        }
    },
    'answer': 'd',
    'gain': 20,
    'penalty': 5
}, {
    'question':
    '¿Quien es el maximo goleador en las Copas Mundiales de Futbol?',
    'options': {
        'a': {
            'id': 'a',
            'option': 'Miroslav Klose',
            'message': 'Muy Bien'
        },
        'b': {
            'id':
            'b',
            'option':
            'Gabriel Batistuta',
            'message':
            'Gabriel Batistuta solo anoto 10 goles en las Copas Mundiales de Futbol'
        },
        'c': {
            'id':
            'c',
            'option':
            'Ronaldo Nazario',
            'message':
            'Ronaldo Nazario solo anoto 15 goles en las Copas Mundiales de Futbol'
        },
        'd': {
            'id':
            'd',
            'option':
            'Gerd Muller',
            'message':
            'Gerd Muller solo anoto 14 goles en las Copas Mundiales de Futbol'
        }
    },
    'answer': 'a',
    'gain': 30,
    'penalty': 5
}, {
    'question':
    '¿Que pais fue el primer Bicampeon de las Copas Mundiales de Futbol?',
    'options': {
        'a': {
            'id': 'a',
            'option': 'Italia',
            'message': 'Muy Bien'
        },
        'b': {
            'id': 'b',
            'option': 'Brasil',
            'message': 'Brasil no fue el primer bicampeón'
        },
        'c': {
            'id': 'c',
            'option': 'Alemania',
            'message': 'Alemania no fue el primer bicampeón'
        },
        'd': {
            'id': 'd',
            'option': 'Uruguay',
            'message': 'Uruguay no fue el primer bicampeón'
        }
    },
    'answer': 'a',
    'gain': 40,
    'penalty': 5
}, {
    'question': '¿Que Pais ha jugado más finales en la Copa Mundial de Futbol',
    'options': {
        'a': {
            'id': 'a',
            'option': 'Brasil',
            'message': 'Brasil ha jugado 7 finales'
        },
        'b': {
            'id': 'b',
            'option': 'Alemania',
            'message': 'Muy Bien'
        },
        'c': {
            'id': 'c',
            'option': 'Argentina',
            'message': 'Argentina ha jugado 5 finales'
        },
        'd': {
            'id': 'd',
            'option': 'Paises Bajos',
            'message': 'Paises Bajos ha jugado 3 finales'
        }
    },
    'answer': 'b',
    'gain': 50,
    'penalty': 5
}]


def printBanner(maxPlayer, maxScore):
    print(BLUE)
    print("\n")
    print(" ███████████ ███████████   █████ █████   █████ █████   █████████  ")
    print("░█░░░███░░░█░░███░░░░░███ ░░███ ░░███   ░░███ ░░███   ███░░░░░███ ")
    print("░   ░███  ░  ░███    ░███  ░███  ░███    ░███  ░███  ░███    ░███ ")
    print("    ░███     ░██████████   ░███  ░███    ░███  ░███  ░███████████ ")
    print("    ░███     ░███░░░░░███  ░███  ░░███   ███   ░███  ░███░░░░░███ ")
    print("    ░███     ░███    ░███  ░███   ░░░█████░    ░███  ░███    ░███ ")
    print("    █████    █████   █████ █████    ░░███      █████ █████   █████")
    print("   ░░░░░    ░░░░░   ░░░░░ ░░░░░      ░░░      ░░░░░ ░░░░░   ░░░░░ ")
    print("\n")
    print('{:>45}'.format('TOTAL SCORE RANKING'))
    print('{} {:>33} {:>30}'.format('RANK', 'SCORE', 'NAME'))
    print('\n{:>4} {:>33} {:>30}\n'.format('1st', maxScore, maxPlayer))


def getName():
    print("Hola soy Jackal29")
    print("Bienvenido a mi trivia de fútbol")
    print(
        "Pondremos a prueba tus conocimientos sobre las copas mundiales de futbol\n"
    )
    time.sleep(1)
    nombre = input("Ingresa tu nombre: ")
    print("\nBienvenido", nombre, '!')
    return nombre


def executeGame(nombre):
    print(
        "\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    )
    puntaje = 0
    print('{}Tienes {} puntos{}'.format(GREEN, puntaje, BLUE))
    n = 1
    for question in questions:
        time.sleep(1)
        print('\n{:1d}) {}\n'.format(n, question['question']))
        for option in question['options'].values():
            print('{}) {}'.format(option['id'], option['option']))
        respuesta = input("\nTu respuesta: ")
        while respuesta not in ("a", "b", "c", "d"):
            respuesta = input(
                "Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")
        n += 1
        if respuesta == question['answer']:
            print("\nMuy Bien", nombre, "!")
            puntaje = puntaje + question['gain']
            print('\n{}Has ganado {} puntos. Tienes {} puntos {}'.format(
                GREEN, question['gain'], puntaje, BLUE))
        else:
            print('\nIncorrecto {}! {}'.format(
                nombre, question['options'][respuesta]['message']))
            puntaje = puntaje - question['penalty']
            print('\n{}Has perdido {} puntos.{} Tienes {} puntos {}'.format(
                RED, question['penalty'], GREEN, puntaje, BLUE))
    return puntaje


def printRanking(nombre, puntaje, maxPlayer, maxScore):
    print('\n{}Felicitaciones {}!. Has obtenido {} puntos.'.format(
        MAGENTA, nombre, puntaje))
    if puntaje > maxScore:
        maxScore = puntaje
        maxPlayer = nombre
        print('{}, has alcanzado el primer lugar del ranking{}'.format(
            nombre, BLUE))
    print(BLUE)
    return maxPlayer, maxScore


maxPlayer = 'Admin'
maxScore = 10
while True:
    printBanner(maxPlayer, maxScore)
    nombre = getName()
    puntaje = executeGame(nombre)
    maxPlayer, maxScore = printRanking(nombre, puntaje, maxPlayer, maxScore)
    continuar = input(
        "\nDeseas volver a jugar? Presiona (y/n) para continuar: ")
    while continuar not in ("y", "Y", "n", "N"):
        continuar = input("Debes presionar (y/n) para continuar: ")
    if continuar == 'N' or continuar == 'n':
        break
