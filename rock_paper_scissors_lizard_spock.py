import random

'''
Piedra, papel, tijera, spock, lagarto ¿Quien le gana a quien?

'spock': 'tijeras',
'spock': 'piedra',
'tijeras': 'papel',
'tijeras': 'lagarto',
'papel': 'piedra',
'papel': 'spock',
'piedra': 'lagarto',
'piedra': 'tijeras',
'lagarto': 'spock',
'lagarto': 'papel'


¿CÓMO FUNCIONA EL DICCIONARIO EN EL JUEGO?:

Una forma de interpretarlo es:
Si yo saco piedra, ¿qué tiene que sacar el otro jugador para que yo gane y el pierda?.
Es por esto que en el condicional, al dicccionario "gana" se le pasa lo que sacó maquina y se hace 
la comparación con el jugador.
>> Si yo como maquina juego con "piedra", según el diccionario, ¿qué tiene que sacar el jugador para que yo gane?
>> gana['piedra'] = tijera >> El jugador debe sacar "tijera" para que yo gane.

Si se hace con el jugador:
<< Si yo como jugador juego con "tijera", según el diccionario, ¿qué tiene que sacar la maquina que esta pierda? >>
>> gana['tijera'] = papel >> La maquina tiene que sacar "papel" para que yo gane. 
'''

# Esto es un comentario

OPCIONES = ['piedra', 'papel', 'tijera', 'spock', 'lagarto']
GANA = {'spock': {'tijera': 'Spock rompe la tijera',
                  'piedra': 'Spock vaporiza la piedra'},
        'tijera': {'papel': 'Tijera corta el papel',
                   'lagarto': 'Tijera decapita al lagarto'},
        'papel': {'piedra': 'Papel cubre a la piedra',
                  'spock': 'Papel desautoriza a spock'},
        'piedra': {'lagarto': 'Piedra aplasta al lagarto',
                   'tijera': 'Piedra aplasta las tijeras'},
        'lagarto': {'spock': 'Lagarto envenena a spock',
                    'papel': 'Lagarto se come el papel'}}
marcador = [0, 0]  # marcador[0] -> jugador, marcador[1] -> maquina
ronda = 0

print('¡Inicia el juego!')
maquina = random.choice(OPCIONES)  # Ej. papel
jugador = input('\n\npiedra, papel, tijera, spock o lagarto ¡Juega! (s para salir): ')  # Ej. piedra

while True:

    if jugador == 's':
        break
    if jugador in OPCIONES:
        pass
    else:
        print('¡Juega en serio, humano! ' + jugador + ' no es una opción válida.')
        jugador = input('\n\npiedra, papel, tijera, spock o lagarto ¡Juega! (s para salir): ')  # Ej. piedra
        continue

    ronda += 1
    if jugador == maquina:
        print('Empate ¬_¬')
    elif jugador in GANA[maquina].keys():
        print('¡PERDISTE! ' + GANA[maquina][jugador] + '. Buajajaja XD')
        marcador[1] += 1
    else:
        print('GANASTE ' + GANA[jugador][maquina] + '. Exijo la revancha :(')
        marcador[0] += 1

    print(f'El marcador Humano {marcador[0]} : {marcador[1]} Maquina')
    decision = input('\n¿Quieres jugar de nuevo? si (jugar de nuevo) r (reiniciar el marcador) >> ')
    maquina = random.choice(OPCIONES)  # Ej. papel
    if decision == 'si':
        jugador = input('\n\npiedra, papel, tijera, spock o lagarto ¡Juega! (s para salir): ')  # Ej. piedra
    elif decision in OPCIONES:
        jugador = decision
    elif decision == 'r':
        marcador = [0, 0]
        print(f'Nuevo marcador Humano {marcador[0]} : {marcador[1]} Maquina')
        jugador = input('\n\npiedra, papel, tijera, spock o lagarto ¡Juega! (s para salir): ')  # Ej. piedra
    else:
        break
if ronda == 0:
    print('\n\nAy yo queria jugar :´(\n')
else:
    print(
        f'\n\nMarcador final -> Humano {marcador[0]} : {marcador[1]} Maquina\nMe divertí, humano. Gracias por jugar\n')
