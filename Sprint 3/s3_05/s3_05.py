def busca_linear(lista, alvo):
    for posicao in range(len(lista)):                                      # Percorre a lista do início ao fim, índice por índice
        if lista[posicao] == alvo:                                         # Se alvo estiver entre os itens,
            return posicao                                                 # retorne a posição onde o item é o alvo
    return -1                                                              # -1 aqui é convenção

def busca_binaria(lista, alvo):                                            # Vai cortando a lista pela metade pra otimizar as bucas

    esq = 0                                                                # Esquerda é a posição 0
    dir = len(lista) - 1                                                   # Direita é a posição final da lista -1

    while esq <= dir:                                                      # Metade é a esquerda (0) + direita
        metade = (esq + dir) // 2                                          #  (todas as posições) // 2

        if lista[metade] == alvo:                                          # Se o alvo da busca estiver na posição da metade
            return metade                                                  # da lista, retorna a metade
        elif lista[metade] < alvo:                                         # Se o alvo for maior q os valores da primeira metade
            esq = metade + 1                                               # retorna a segunda metade
        else:                                                              # Se o alvo for menor que a posição da metade,
            dir = metade - 1                                               # retorna a primeira metade

    return -1

## Testes de busca:

if __name__ == '__main__':

    lista_busca = [10, 20, 30, 40, 50, 60, 70, 80]
    
    print('=== BUSCAS ===')
    print(f'Linear(40): {busca_linear(lista_busca, 40)}')                  # 3
    print(f'Linear(100): {busca_linear(lista_busca, 100)}')                # -1
    print(f'Binária(40): {busca_binaria(lista_busca, 40)}')                # 3
    print(f'Binária(100): {busca_binaria(lista_busca, 100)}')              # -1

def bubble_sort(lista):

    tamanho = len(lista)                                                   # Define o tamanho da lista (a qtde de posições q os itens da lista ocupam)

    for passada in range(tamanho):                                         # Pra cada passada (vai passar o número de vezes equivalente ao tamanho da lista)
        for posicao in range(tamanho - 1 - passada):                       # Passando na posição tal dentro do range que queremos
            if lista[posicao] > lista[posicao + 1]:                        # Se o item da posição a esquerda for maior que o da direita
                lista[posicao], lista[posicao + 1] = lista[posicao + 1], lista[posicao] # Ocorre a troca

    return lista

def bubble_sort_explicado(lista):                                          # Aqui pedi pra IA gerar uma versão da função que explicasse cada etapa
    print('BubbleSort em ação: ')                                          # porque eu estava com dificuldade de entender a construção da função
    
    tamanho = len(lista)

    for passada in range(tamanho):
        print(f'--- Passada {passada}: range(0, {tamanho - 1 - passada}) ---')
        for posicao in range(tamanho - 1 - passada):
            if lista[posicao] > lista[posicao + 1]:
                lista[posicao], lista[posicao + 1] = lista[posicao + 1], lista[posicao]
            print(f'  posicao={posicao}: {lista}')

    return lista

bubble_sort_explicado([7, 3, 2, 0, 4, 6])                                  # Exemplo de BubbleSort

def selection_sort(lista):

    tamanho = len(lista)                                                   # Quantos itens tem na lista
    
    for posicao_atual in range(tamanho):                                   # Percorre cada posição que queremos preencher
        posicao_menor = posicao_atual                                      # Assume que o menor tá na posição atual
                                                                  # Procura o menor no resto
        for posicao_busca in range(posicao_atual + 1, tamanho):            # Se existir um menor do que o presumido
            if lista[posicao_busca] < lista[posicao_menor]:                # anteriormente, atualiza a posição do menor,
                posicao_menor = posicao_busca                              #  ou seja, esse novo menor vai pra posição 0.
        
        lista[posicao_atual], lista[posicao_menor] = lista[posicao_menor], lista[posicao_atual]

    return lista

def selection_sort_explicado(lista):                                       # Aqui é o selection sort com os prints
    print('SelectionSort em ação: ')                                       # mostrando cada etapa/passada da função

    tamanho = len(lista)

    for posicao_atual in range(tamanho):
        posicao_menor = posicao_atual

        for posicao_busca in range(posicao_atual + 1, tamanho):
            if lista[posicao_busca] < lista[posicao_menor]:
                posicao_menor = posicao_busca

        lista[posicao_atual], lista[posicao_menor] = lista[posicao_menor], lista[posicao_atual]
        print(f'Passada {posicao_atual}: {lista}')

    return lista

selection_sort_explicado([7, 3, 2, 0, 4, 6])                               # Exemplo de SelectionSort

def insertion_sort(lista):

    tamanho = len(lista)
    
    for posicao_atual in range(1, tamanho):                                # começa em 1 (o 0 já tá "ordenado")
        chave = lista[posicao_atual]                                       # o item que vamos inserir na parte ordenada
        posicao_compara = posicao_atual - 1                                # começa comparando com o item à esquerda
                                                                           # enquanto não chegou ao início e o item à esquerda é maior que a chave
        while posicao_compara >= 0 and lista[posicao_compara] > chave:
            lista[posicao_compara + 1] = lista[posicao_compara]            # move o item pra direita
            posicao_compara -= 1                                           # volta mais uma posição
                                                                           # encaixa a chave na posição correta
        lista[posicao_compara + 1] = chave
    
    return lista

def insertion_sort_explicado(lista):
    print('InsertionSort em ação: ')
    tamanho = len(lista)
    for posicao_atual in range(1, tamanho):
        chave = lista[posicao_atual]
        posicao_comparacao = posicao_atual - 1
        while posicao_comparacao >= 0 and lista[posicao_comparacao] > chave:
            lista[posicao_comparacao + 1] = lista[posicao_comparacao]
            posicao_comparacao -= 1
        lista[posicao_comparacao + 1] = chave
        print(f'Após inserir {chave}: {lista}')
    return lista

insertion_sort_explicado([5, 2, 4, 1, 3])

## Testes de desempenho dos Sorts/Ordenações:

import time
import random                                                              # Importei o time pra medir o tempo de execução das funções
                                                                           # e também o random só pra desordenar aleatoriamente as listas.
if __name__ == '__main__':                                                 # Testes de desempenho:

    print('Testes de desempenho das Sorts: ')
    tamanhos = [100, 500, 1000]

    for n in tamanhos:
        lista_teste = list(range(n))
        random.shuffle(lista_teste)                                        # Usando o random pra desorganizar a lista
        
        print(f'Tamanho: {n}')                                             # Mostra qual o tamanho da lista sendo ordenada (100, 500 ou 1000)
        
        copia = lista_teste.copy()
        inicio = time.time()
        bubble_sort(copia)
        final = time.time()
        teste_bubble = final - inicio
        print(f'Bubble: {teste_bubble} segundos. ')
        
        copia = lista_teste.copy()
        inicio = time.time()
        selection_sort(copia)
        final = time.time()
        teste_selection = final - inicio
        print(f'Selection: {teste_selection} segundos. ')
        
        copia = lista_teste.copy()
        inicio = time.time()
        insertion_sort(copia)
        final = time.time()
        teste_insertion = final - inicio
        print(f'Insertion: {teste_insertion} segundos. ')
