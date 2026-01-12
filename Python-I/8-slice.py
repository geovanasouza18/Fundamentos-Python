gameName = "Palia"

gameDescription = """
Palia é um jogo de simulação de vida
desenvolvido pela Singularity 6,
com foco em atividades como pesca, culinária e agricultura.
Permite jogar sozinho ou com amigos online.
"""

# string[início:fim] - índice começa com 0 | índice final -1

# Busque toda string a partir da primeira posição
print(gameName[0:])

# Busque toda string até a última posição
print(gameName[:5])

# Busque toda string da terceira até a última posição
print(gameName[2:])

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""
#Busque toda a string de 2 em 2 caracteres.
print(gameName[::2])

# Inverta uma string de trás pra frente
print(gameName[::-1])

# Imprime os caracteres nos índices ímpares
print(gameName[1::2])
