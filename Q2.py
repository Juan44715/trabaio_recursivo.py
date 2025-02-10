print('Olá pessoa! Você gostaria de testar essa calculadora de listas e sublistas?')
print('Não? ah... MESMO ASSIM! Funciona o seguinte, você vai seguir as instruções abaixo para criar listas e sublistas e, depois,')
print('a calculadora vai fazer o que ela faz de melhor. Calcular')
def soma_lista_aninhada(lista):

    soma = 0
    for elemento in lista:
        if isinstance(elemento, list): 
            soma += soma_lista_aninhada(elemento)
        else: 
            soma += elemento
    return soma

def criar_lista():

    lista = []
    while True:
        entrada = input("Digite um número para entrar na lista, 'sub' para criar uma sublista ou 'finalizar' para... bem, finalizar né: ")
        if entrada.lower() == "finalizar":
            break
        elif entrada.lower() == "sub":
            print("Criando uma sublista...")
            lista.append(criar_lista())  
        else:
            try:
                lista.append(int(entrada))  
            except ValueError:
                print("Entrada inválida! Digite um número ou 'sub' para sublista fazendo o favor.")
    return lista

print("Vamos criar uma lista aninhada:")
lista_usuario = criar_lista()
print("Lista criada:", lista_usuario)


resultado = soma_lista_aninhada(lista_usuario)
print("A soma dos elementos é:", resultado)

