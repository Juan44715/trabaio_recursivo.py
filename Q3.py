print('Bem vindo ao Contador de letras e numeros! Nesse codigo você vai escolher uma palavra, que pode também ter numeros,')
print('e depois escolher uma letra ou numero para que o sistema calcule quantas vezes a escolha aparece')
def contar_caracteres(s, c):
   
    if not s:  
        return 0
    return (1 if s[0] == c else 0) + contar_caracteres(s[1:], c)


s = input("Digite uma string bacana: ")
c = input("Digite o caractere que deseja contar (ex: a, h, 2, ): ")

while len(c) != 1:
    print("Por favor, digite apenas um único caractere.")
    c = input("Digite o caractere que deseja contar (ex: a, h, 2, ): ")

resultado = contar_caracteres(s, c)
print(f"O caractere '{c}' aparece {resultado} vezes na string '{s}'.")
print('Bem legal, não acha??')
