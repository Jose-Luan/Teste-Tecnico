""" 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse; """

string = str(input("Digite uma string: "))
string_invertida = ""

index = len(string) - 1
while index >= 0:
    string_invertida += string[index]
    index -= 1

print("String original:", string)
print("String invertida:", string_invertida)
