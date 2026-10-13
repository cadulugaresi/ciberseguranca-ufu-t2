import numpy as np

print('Exercício 1')

A = np.array([
    [2, 1],
    [1, 1],
])

det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A) # Inverso de uma matriz é ela mesma elevada a -1
identidade = A @ inv_A # ID de uma matriz é igual a ela mesma multiplicada pelo seu inverso

print(f'''
Matriz A:
{A}

Determinante: {det_A:.4f}

Inversa:
{inv_A} 

Verificação A @ A⁻¹:
{identidade}

{np.allclose(identidade, np.eye(2))} 
''')

print('Exercício 2')

A3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

det_A3 = np.linalg.det(A3)

print(f'''
Matriz A3:
{A3}

Determinante (NumPy):      {det_A3:.4f}
Determinante (Sarrus):      0.0000
Determinante (cofatores):   0.0000

É singular? {np.isclose(det_A3, 0)}
''')

B3 = np.array([
    [2, 0, 0],
    [0, 3, 0],
    [0, 0, 4],
])
det_B3 = np.linalg.det(B3)

print(f'''
Matriz B3:
{B3}

Determinante (NumPy): {det_B3:.4f}

Exercício 4
''')

# Dado que a coluna e linha 1 = Notebook; c&l 2 = Servidor; c&l 3 = Roteador:

A_sing = np.array([
    [0, 1, 0],   # Notebook herda 100% do Servidor
    [1, 0, 0],   # Servidor herda 100% do Notebook
    [0, 0, 0],   # Roteador não herda nenhuma vulnerabilidade
])

I = np.eye(3)
I_menos_A_sing = I - A_sing

det_sing = np.linalg.det(I_menos_A_sing)

print(f'''
Matriz A_sing:
{A_sing}

Soma de cada linha de A_sing:
Linha 0: {A_sing[0].sum()}
Linha 1: {A_sing[1].sum()}
Linha 2: {A_sing[2].sum()}

Matriz (I - A_sing):
{I_menos_A_sing}

Determinante: {det_sing:.4f}

É singular? {np.isclose(det_sing, 0)}
''')