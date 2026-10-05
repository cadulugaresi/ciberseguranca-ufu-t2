fila_lista = []


def enqueue(item):                           # ENQUEUE adiciona um item no fim da fila
    fila_lista.append(item)


def dequeue():                               # DEQUEUE remove o item do início da fila e o retorna
    if len(fila_lista) == 0:
        return None                          # SE a qtde de itens da fila for 0, retorna None
    return fila_lista.pop(0)                 # SE a fila tiver itens, remove o primeiro item.

                                             # Depois da execução do dequeue, todos os itens da fila
                                             # são deslocados uma posição para a esquerda, ou seja, o
                                             # segundo item passa a ser o primeiro e consecutivamente.
                                             # Isso faz com que essa função seja lenta em listas grandes,
                                             # porque é preciso percorrer toda a lista para deslocar tudo.
# ======== EXEMPLO DE USO ========

print(fila_lista)                            # Imprime a fila vazia
enqueue('Ana')                               # Adiciona 'Ana' no fim da fila
enqueue('Bia')                               # Adiciona 'Bia' no fim da fila
enqueue('Cris')                              # Adiciona 'Cris' no fim da fila
enqueue('Dani')                              # Adiciona 'Dani' no fim da fila
print(fila_lista)

print("Item removido:", dequeue())           # Remove o primeiro item da fila e o retorna
print(fila_lista)                            # Agora 'Bia' é o primeiro item da fila, porque 'Ana' foi removida

def front(fila_lista):                       # Retorna o primeiro item da fila sem removê-lo.
    if len(fila_lista) == 0:                 # Usando a mesma logica: se a fila estiver vazia, retorna None.
        return None                               
    return fila_lista[0]

def esta_vazia(fila_lista):                  # Se a fila tiver 0 itens, retorna True.
    return len(fila_lista) == 0

print(f'Primeiro da fila: {front(fila_lista)}')
print(f'Fila tá vazia? {esta_vazia(fila_lista)}')

# ======== DEQUE =========

from collections import deque                # Visualmente, deque é igual a uma lista.

fila_deque = deque(['Gato','Cão','Coelho','Pássaro','Peixe','Rato'])                          
print(fila_deque)
                                             # fila.appendleft(item) === Adiciona item no início.
# ======== TIME =========                    # fila.append(item) === Adiciona item no fim da fila.          
                                             # fila.pop() === Remove item do fim da fila.
import time                                  #fila.popleft() === Remove item do início da fila.

fila_lista = []                              # O diferencial do deque é que ele é otimizado para adicionar
                                             # e remover itens tanto no início quanto no fim da fila, sem
inicio = time.time()                         # precisar deslocar os itens como acontece com listas. Ou seja,
                                             # ele é mais rápido para essas operações em filas grandes.
for itens in range(100000):                  
    fila_lista.append(itens)                 # Teste com lista comum:
for itens in range(100000):                  # itens = todos os números dentro do range(100000)
    fila_lista.pop(0)                        # Tira o primeiro item da fila 100000 vezes usando o pop(0) (lento).

fim = time.time()
duracao_lista = fim - inicio
print(f'Lista: {duracao_lista:.4f} segundos')

fila_deque_test = deque()                    # Mesmo teste, mas usando deque e popleft() (rápido)

inicio = time.time()

for itens in range(100000):                  
    fila_deque_test.append(itens)
for itens in range(100000):
    fila_deque_test.popleft()
    
fim = time.time()
duracao_deque = fim - inicio
print(f'Deque: {duracao_deque:.4f} segundos')     

# ======= LISTA ENCADEADA ==========
                                             # Nesse primeiro exemplo, crio uma lista encadeada "manual",
class No:                                    # em que cada vez que crio um novo nó, tenho que definir
    def __init__(self, valor):               # manualmente qual é seu próximo e seu antecessor
        self.valor = valor 
        self.proximo = None

no1 = No(10)                                 # Cria três nós soltos
no2 = No(20)
no3 = No(30)
                                             # Estado atual: cada um tá sozinho, sem ligação
print(no1.valor, no1.proximo)                # Retorna 10, None
print(no2.valor, no2.proximo)                # Retorna 20, None
print(no3.valor, no3.proximo)                # Retorna 30, None

no2.proximo = no1                            # Defino a ordem/ligação dos nós manualmente
no3.proximo = no2

atual = no3                                  # Começamos na cabeça (head) da lista como o valor atual
while atual is not None:                     # Enquanto o valor atual não for None
    print(atual.valor)                       # Printamos o valor atual
    atual = atual.proximo                    # Colocamos que o atual agora é o próximo
                                             # E assim vai, até a lista acabar e o atual for None
class ListaEncadeada:

    def __init__(self):                      # Cria um vagão com um valor 'começo'
        self.inicio = 'começo'               

    def inserir_inicio(self, valor):         # Função insere novo vagão no início
                                             
        novo_vagao = No(valor)               # Novo vagão recebe tal valor
        novo_vagao.proximo = self.inicio     # Próximo vagão a ser adicionado vai virar o novo início
        self.inicio = novo_vagao             # Novo vagão (criado agora) vira início atual
                                             
    def percorrer(self):                     # Função que percorre e printa toda a lista
        vagao_atual = self.inicio            # Vagão atual é o começo da lista encadeada
        while vagao_atual != 'começo':       # Enquanto o vagão atual não o vagão de valor 'começo'
            print(vagao_atual.valor,end='->')# ela printa o valor de cada vagão, seguido de uma seta ' -> '
            vagao_atual = vagao_atual.proximo# Vagão atual agora é o próximo vagão, então vai
        print('começo')                      # printando até percorrer toda a lista e não haver próximo vagão.

    def inserir_fim(self, valor):            # Insere um valor no fim da lista encadeada e não no começo
        novo_vagao = No(valor)               # Insere o vagão novo, beleza
        novo_vagao.proximo = 'começo'
        if self.inicio == 'começo':          # Se não tiver nenhum outro vagão, esse é o primeiro
            self.inicio = novo_vagao         
            return
        
        else:                                # Agora se já houverem outros vagões
            vagao_atual = self.inicio        # Essa função percorre até o último
            while vagao_atual.proximo != 'começo':# e liga o novo valor no último vagão
                vagao_atual = vagao_atual.proximo  
            vagao_atual.proximo = novo_vagao      

lista = ListaEncadeada()

print('Adicionando itens ao início da lista:')
lista.inserir_inicio('um')                   #   inicio ──► ['três'] ──► ['dois'] ──► ['um'] ──► ['quatro'] ──► ['começo']
lista.inserir_inicio('dois')
lista.inserir_inicio('três')                 #   inserir_inicio: adiciona na ESQUERDA (início)
lista.percorrer()                            #   inserir_fim:    adiciona na DIREITA (fim)
                                             #   percorrer:      segue .proximo até achar 'começo'
print('Adicionando itens ao fim da lista:')
lista.inserir_fim('quatro')
lista.percorrer()