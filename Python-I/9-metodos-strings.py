name = "Sherlock Code"
description = """
Aula para desvendar os mistérios da programação, com lógica afiada e raciocínio preciso.
"""

print(name.upper()) #Retornar strings tudo Maiúsculo
print(name.lower()) # Minúsculo
print(name.capitalize()) #Apenas primeira letra maiúscula
print(name.title()) #Apenas primeira letra maiúscula
print(name.center(19, '-')) #Retorna a string centralizada, esse valor 19 já conta com o valor da string, então tem que colocar um valor que ambos os lados fique igual ou não precisa que os lagos fique igual
print(name.find("e")) #Retorna a posição de um determinado caractere
print(description.count('a')) #Conta quantos caracteres, iguais a ele, se o ã for assim, ele não conta
print(description.replace("Aula", "Assunto")) #Altera valor de uma string
print(description.split(','))