print('Olá presado usuario. Bem vindo! Esse sistema vai coletar os numeros que voce inserir e verificar qual')
print('é o maior numero da lista e em qual posição da lista ele está')
print('ATENÇÃO. Lembre-se que a conta da posição começa do 0 e não do 1')
def indice_maior_elemento(lista, indice=0, maior_indice=0):
    if indice == len(lista):  
        return maior_indice
    
    if lista[indice] > lista[maior_indice]:
        maior_indice = indice
    return indice_maior_elemento(lista, indice + 1, maior_indice)

entrada = input("Digite os números separados por espaço: ")
lista_usuario = list(map(int, entrada.split()))  

if not lista_usuario:
    print("A lista não pode estar vazia! Coloque algum numero para funcionar direitinho ")
else:
    resultado = indice_maior_elemento(lista_usuario)
    print(f"O maior elemento é {lista_usuario[resultado]}, que está no índice {resultado}.")
