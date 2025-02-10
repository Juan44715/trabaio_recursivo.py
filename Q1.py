print('Bem vindo ao ReverteString 2.0! (patente pendente)')
print('Aqui você vai digitar alguma string e ela vai sair invertida, mas sem laços de repetição! Legal, não?')
def reverter_caracteres(s):
    if len(s) <= 1:
        return s

    return s[-1] + reverter_caracteres(s[:-1])


teste = input('Digite a palavra que vai sair ao contrario: ')
print('O que você digitou ficou assim invertido: ')
print(reverter_caracteres(teste))  
print('Prontinho! Olha que legal :D')