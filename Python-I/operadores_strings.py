gameName = "Palia"

gameDescription = """
Palia é um jogo de simulação de vida
desenvolvido pela Singularity 6,
com foco em atividades como pesca, culinária e agricultura.
Permite jogar sozinho ou com amigos online.
"""
#Operação de multiplicação de Strings
line = "-"
print(line * 30)

# Operação de concatenação de string
gameVersion = " 0.192"
gameFullName = gameName + gameVersion

print(gameFullName)

print(line * 30)

#Procura palavra dentro de um texto - o retorno que ele dá será true ou false. É tipo uma pergunta se existe uma determinada palavra em um texto
print ("fazenda" in gameDescription)