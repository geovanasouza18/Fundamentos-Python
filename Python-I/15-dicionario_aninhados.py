import pprint

gameDict = {
    'Palia':{
        'ano': 2023,
        'clasificacao': 9.0,
        'genero': ['Massively Multiplayer Online', 'Aventura e Exploração']
    },
    'Mario odyssey':{
        'ano': 2017,
        'clasificacao': 10.0,
        'genero': ['3D', 'Aventura']
    },
    'The Sims 4':{
        'ano': 2014,
        'clasificacao': 8.5,
        'genero': 'Simulador de vida'
    }
}
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(gameDict)