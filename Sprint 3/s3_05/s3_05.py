import time
import random


def busca_linear(lista, alvo):
    for posicao in range(len(lista)):  # percorre a lista do início ao fim
        if lista[posicao] == alvo:  # se o item atual for o alvo
            return posicao  # retorna a posição do alvo
    return -1  # -1 é convenção de não encontrado


def busca_binaria(lista, alvo):  # busca cortando a lista pela metade
    esq = 0  # esquerda começa na posição 0
    dir = len(lista) - 1  # direita começa na última posição

    while esq <= dir:  # enquanto o pedaço não está vazio
        metade = (esq + dir) // 2  # calcula o meio do pedaço
        if lista[metade] == alvo:  # alvo está na metade
            return metade  # retorna a posição da metade
        elif lista[metade] < alvo:  # alvo é maior que a metade
            esq = metade + 1  # descarta a metade esquerda
        else:  # alvo é menor que a metade
            dir = metade - 1  # descarta a metade direita

    return -1  # não encontrado


# Testes de busca:

if __name__ == "__main__":

    lista_busca = [10, 20, 30, 40, 50, 60, 70, 80]

    print("=== BUSCAS ===")
    print(f"Linear(40): {busca_linear(lista_busca, 40)}")  # 3
    print(f"Linear(100): {busca_linear(lista_busca, 100)}")  # -1
    print(f"Binária(40): {busca_binaria(lista_busca, 40)}")  # 3
    print(f"Binária(100): {busca_binaria(lista_busca, 100)}")  # -1


def bubble_sort(lista):
    tamanho = len(lista)  # quantidade de itens da lista

    for passada in range(tamanho):  # cada passada
        for posicao in range(tamanho - 1 - passada):  # posições a comparar
            if lista[posicao] > lista[posicao + 1]:  # fora de ordem?
                # troca os dois itens de lugar
                lista[posicao], lista[posicao + 1] = lista[posicao + 1], lista[posicao]

    return lista


def bubble_sort_explicado(lista):  # versão com prints pra visualizar
    print("BubbleSort em ação: ")

    tamanho = len(lista)

    for passada in range(tamanho):
        print(f"--- Passada {passada}: range(0, {tamanho - 1 - passada}) ---")
        for posicao in range(tamanho - 1 - passada):
            if lista[posicao] > lista[posicao + 1]:
                lista[posicao], lista[posicao + 1] = lista[posicao + 1], lista[posicao]
            print(f"  posicao={posicao}: {lista}")

    return lista


bubble_sort_explicado([7, 3, 2, 0, 4, 6])  # exemplo de BubbleSort


def selection_sort(lista):
    tamanho = len(lista)  # quantidade de itens na lista

    for posicao_atual in range(tamanho):  # posição que queremos preencher
        posicao_menor = posicao_atual  # assume que o menor está aqui
        for posicao_busca in range(posicao_atual + 1, tamanho):  # busca o menor
            if lista[posicao_busca] < lista[posicao_menor]:  # achou um menor?
                posicao_menor = posicao_busca  # atualiza a posição do menor

        # troca a posição atual com a posição do menor
        lista[posicao_atual], lista[posicao_menor] = (
            lista[posicao_menor],
            lista[posicao_atual],
        )

    return lista


def selection_sort_explicado(lista):  # versão com prints pra visualizar
    print("SelectionSort em ação: ")

    tamanho = len(lista)

    for posicao_atual in range(tamanho):
        posicao_menor = posicao_atual

        for posicao_busca in range(posicao_atual + 1, tamanho):
            if lista[posicao_busca] < lista[posicao_menor]:
                posicao_menor = posicao_busca

        lista[posicao_atual], lista[posicao_menor] = (
            lista[posicao_menor],
            lista[posicao_atual],
        )
        print(f"Passada {posicao_atual}: {lista}")

    return lista


selection_sort_explicado([7, 3, 2, 0, 4, 6])  # exemplo de SelectionSort


def insertion_sort(lista):
    tamanho = len(lista)

    for posicao_atual in range(1, tamanho):  # começa em 1 (0 já ordenado)
        chave = lista[posicao_atual]  # item a ser inserido
        posicao_compara = posicao_atual - 1  # começa à esquerda

        # enquanto não chegou ao início e o item à esquerda é maior
        while posicao_compara >= 0 and lista[posicao_compara] > chave:
            lista[posicao_compara + 1] = lista[posicao_compara]  # move pra direita
            posicao_compara -= 1  # volta uma posição

        lista[posicao_compara + 1] = chave  # encaixa a chave na posição

    return lista


def insertion_sort_explicado(lista):  # versão com prints pra visualizar
    print("InsertionSort em ação: ")
    tamanho = len(lista)
    for posicao_atual in range(1, tamanho):
        chave = lista[posicao_atual]
        posicao_comparacao = posicao_atual - 1
        while posicao_comparacao >= 0 and lista[posicao_comparacao] > chave:
            lista[posicao_comparacao + 1] = lista[posicao_comparacao]
            posicao_comparacao -= 1
        lista[posicao_comparacao + 1] = chave
        print(f"Após inserir {chave}: {lista}")
    return lista


insertion_sort_explicado([5, 2, 4, 1, 3])

# Testes de desempenho dos Sorts:

if __name__ == "__main__":
    print("Testes de desempenho das Sorts: ")
    tamanhos = [100, 500, 1000]

    for n in tamanhos:
        lista_teste = list(range(n))
        random.shuffle(lista_teste)  # desorganiza a lista aleatoriamente

        print(f"Tamanho: {n}")

        copia = lista_teste.copy()
        inicio = time.time()
        bubble_sort(copia)
        final = time.time()
        teste_bubble = final - inicio
        print(f"Bubble: {teste_bubble} segundos. ")

        copia = lista_teste.copy()
        inicio = time.time()
        selection_sort(copia)
        final = time.time()
        teste_selection = final - inicio
        print(f"Selection: {teste_selection} segundos. ")

        copia = lista_teste.copy()
        inicio = time.time()
        insertion_sort(copia)
        final = time.time()
        teste_insertion = final - inicio
        print(f"Insertion: {teste_insertion} segundos. ")
