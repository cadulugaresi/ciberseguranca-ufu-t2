import numpy as np

def matriz_singular(A, b):

    det = np.linalg.det(A)
    print(f'Determinante = {det:.2f}')

    if np.isclose(det, 0):
        print('Matriz singular. Sistema NÃO tem solução única (SPI ou SI).')
    else:
        x = np.linalg.solve(A, b)
        print(f'Sistema SPD. Solução: {x}')

print('''Exercício 1''')

#   x + 2y = 7
#   3x - y = 7

A = np.array([[1, 2], [3, -1]])
b = np.array([7, 7])
matriz_singular(A, b)

print('''
Exercício 2 (A)''')

# x + y = 3
# 2x + 2y = 6

A2 = np.array([[1, 1], [2, 2]])
b2 = np.array([3, 6])
matriz_singular(A2, b2)

print('''
Exercício 2 (B)''')

# x + y = 3
# x + y = 5

A3 = np.array([[1, 1], [1, 1]])
b3 = np.array([3, 5])
matriz_singular(A3, b3)

print('''
Exercício 3
Interpretação geométrica

- Ex.1 (SPD): as duas retas se cruzam em um único ponto — a solução única (x=3, y=2).
- Ex.2A (SPI): as retas coincidem (uma em cima da outra). Infinitas soluções.
- Ex.2B (SI): as retas são paralelas (nunca se cruzam). Nenhuma solução.

Exercício 4''')

b = np.array([23.0, 15.8, 17.0])                  # Risco próprio (calculado na S3_09)

A = np.array([                                    # Matriz de dependências
    [0,   0.5, 0  ],                              # Notebook herda do Servidor
    [0,   0,   0.2],                              # Servidor herda do Roteador
    [0,   0,   0  ],                              # Roteador não herda
])

I = np.eye(3)

I_menos_A = I - A
print(f'''
Matriz (I - A):
{I_menos_A}''')

det = np.linalg.det(I_menos_A)
print(f'''
Determinante de (I - A):
{det:.2f}''')

if np.isclose(det, 0):
    print('Matriz (I - A) é singular. Não dá pra resolver.')
else:
    x = np.linalg.solve(I_menos_A, b)
    print(f'''
    Risco efetivo = {x}
    Risco próprio = {b}''')