from functools import lru_cache
import time
from funcoes_t2 import *

# ==========================================================


def fatorial_recursivo(n):  # Aprendendo recursividade com função fatorial:
    if n == 1:  # Caso base: se n for igual a 1, função retorna 1, pois 1!=1.
        return 1  # Se n não for 1, a função chama a si mesma. Assim, a função
    else:  # continua se chamando até que n seja 1 e, portanto, o fatorial
        return n * fatorial_recursivo(n - 1)  # seja resolvido até o fim.


def fatorial_iterativo(n):  # Aqui em iteratividade a função não chama a si mesma,
    resultado = 1  # mas ainda assim se repete até que o range todo seja percorrido,
    for numero in range(1, n + 1):  # o que, nesse caso, é do número 1 até o (n).
        resultado = resultado * numero
    return resultado


print("Fatorial recursivo:", fatorial_recursivo(10))
# Testes pra provar que as duas funções retornam o mesmo resultado.
print("Fatorial iterativo:", fatorial_iterativo(10))

# ==========================================================


def fibonacci_memoizado(n, cache={}):  # Implementação de cache, para que o programa
    if n in cache:  # memorize os resultados já calculados, evitando
        return cache[n]  # calculos repetidos e tornando o programa mais
        # rápido e eficiente.
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci_memoizado(n - 1, cache) + fibonacci_memoizado(
            n - 2, cache
        )

    cache[n] = resultado
    return resultado


print("Fibonacci memoizado:", fibonacci_memoizado(38))


def fibonacci_recursivo(n):  # Essa é a primeira função do Fibonacci que aprendi,
    if n <= 1:  # só deixei ela depois da memoização pra ver na prática
        return n  # que ela é muito mais lenta que a memoizada e que o cachê
    else:  # realmente faz diferença no desempenho do programa.
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


print("Fibonacci recursivo:", fibonacci_recursivo(38))


@lru_cache(maxsize=None)  # Agora fazendo a memoização com o lru_cache,
def fibonacci_memoizado_2(n):  # a ferramenta embutida do python, pra não precisar
    if n <= 1:  # fazer a implementação manual do cache como na função anterior.
        return n
    else:
        return fibonacci_memoizado_2(n - 1) + fibonacci_memoizado_2(n - 2)


print("Fibonacci memoizado 2:", fibonacci_memoizado_2(38))

# ==========================================================

print(time.time())  # O time() retorna o tempo em segundos desde 1970.

inicio = time.time()  # Aqui uso o time() pela primeira vez. Ele compara
resultado_recursivo = fibonacci_recursivo(35)
# o tempo de execução de cada função, pra ver a diferença
fim = time.time()  # de desempenho entre a memoizada e a recursiva.
duracao_recursivo = fim - inicio
# O time funciona medindo quantos segundos se passaram
# entre 1970 e o início da execução do programa, e depois
inicio = time.time()  # entre 1970 e o fim da execução do programa.
resultado_memoizado = fibonacci_memoizado_2(35)
# A diferença entre os dois tempos é a duração da execução.
fim = time.time()  # O 6f significa que o número será exibido com 6 casas decimais.
duracao_memoizado = fim - inicio
# Obs: como fibonacci_memoizado_2(38) já rodou antes, fib(35)
# já estava no cache do lru_cache - por isso o tempo memoizado
# aqui é tão baixo: é uma busca no cache, não um cálculo novo.

print(f"""
        Recursivo: {resultado_recursivo}
        Tempo: {duracao_recursivo:.6f} segundos

        Memoizado: {resultado_memoizado}
        Tempo: {duracao_memoizado:.6f} segundos
        """)

# ==========================================================

ativos = [
    Notebook(1, "Dell", Setor.TI, "Cadu", StatusDoAtivo.ATIVO, "Linux", 15.6),
    # Chamando função com lambda, que é um jeito de resumir
    Notebook(2, "MacBook", Setor.MARKETING, "Ana", StatusDoAtivo.ATIVO, "macOS", 13.3),
    # funções pequenas em uma linha só. Aqui lambda recebe
    Servidor(3, "Dell PowerEdge", Setor.TI, "Cadu", StatusDoAtivo.ATIVO, 32, 4),
    # ativo e retorna seu nome. A função map(), que também é
    Roteador(4, "TP-Link", Setor.TI, "Cadu", StatusDoAtivo.INATIVO, 4, 1000),
    # uma função de alta ordem, aplica a função lambda a cada
    Impressora(
        5, "HP", Setor.RH, "Bia", StatusDoAtivo.ATIVO, Cor.COLORIDA, Tecnologia.LASER
    ),
    # item da lista [ativos]. A função list() transforma o
]  # resultado da map() em outra lista: [nome dos ativos].

# ==========================================================

nomes = list(map(lambda ativo: ativo.nome, ativos))
print(f"Nomes: {nomes}")

# Em seguida, o exemplo mostra que dá pra fazer a mesma coisa com uma função def normal.


def pegar_nome(a):
    return a.nome  # Função def normal!!!
    # Faz a mesma coisa que a lambda!


nomes = list(map(pegar_nome, ativos))

print(f"""
Versão sem lambda, usando função def normal:-
Lista dos nomes dos ativos: {nomes}
""")

# ==========================================================

# Nesse exemplo seguinte, pegamos com isinstance apenas os ativos da
notebooks = list(filter(lambda a: isinstance(a, Notebook), ativos))
# subclasse Notebooks e depois imprimimos a qtde de Notebooks
print(f"{len(notebooks)} notebook(s) encontrado(s)")
# encontrados com len(), que retorna a qtde de itens da lista.

# Versão sem lambda, usando função def normal:


def pegar_notebook(a):
    return isinstance(a, Notebook)  # Função def normal!!!
    # Faz a mesma coisa que a lambda!


notebooks = list(filter(pegar_notebook, ativos))
# Usando a função def normal no lugar da lambda!

print(f"""
Versão sem lambda, usando função def normal:-
{len(notebooks)} notebook(s) encontrado(s)
""")

# ==========================================================

ativos_ordenados = sorted(ativos, key=lambda ativo: ativo.nome)
# A função sorted() ordena os ativos, usando a função lambda como chave de
nomes_ordenados = list(map(lambda ativo: ativo.nome, ativos_ordenados))
# ordenação, que nesse caso é o nome do ativo. A função sorted() retorna
print(f"Ativos ordenados: {nomes_ordenados}")
# uma nova lista ordenada, sem alterar a lista original. Aqui o resultado
# é capturado numa variável, e o map() extrai só os nomes pra imprimir
# de forma legível (sem isso, o print mostraria endereços de memória,
# porque as classes não têm um __str__ definido).

# Versão sem lambda, usando função def normal:
# A função sorted() também pode ser utilizada com uma função def
# normal, como no exemplo abaixo, reaproveitando pegar_nome().
ativos_ordem_nome = sorted(ativos, key=pegar_nome)
nomes_ordem_alfabetica = list(map(pegar_nome, ativos_ordem_nome))
# Mesma ideia do bloco acima: map() + pegar_nome() pra extrair
# só os nomes da lista já ordenada, em vez de imprimir os objetos crus.
print(f"""
Versão sem lambda, usando função def normal:-
Ativos ordenados: {nomes_ordem_alfabetica}
""")
