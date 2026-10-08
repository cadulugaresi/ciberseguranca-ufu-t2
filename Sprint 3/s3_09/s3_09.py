import numpy as np

M = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
])

v = np.array([3, 4, 5, 2])

resultado = M @ v

print(f'''
ex1.
Matriz M:
{M}

Vetor V: {v}

Resultado Mv: {resultado}
''')

# Matriz de incidência
# Simulando 3 equipamentos e 4 vulnerabilidades

# Linhas: Notebook, Servidor, Roteador
# Colunas CVE: 2024-30064, 2024-36904, 2024-9644, 2024-12856
# 1 = Possui a vulnerabilidade | 0 = Não possui

M_t2 = np.array([
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
])

# Vetor de severidade (notas CVSS)
v_t2 = np.array([8.8, 7, 9.8, 7.2])

risco_proprio = M_t2 @ v_t2

print(f'''
RP ex.1
Risco próprio: {risco_proprio}
''')

# Núcleo e imagem:

M_ni = np.array([                                 # Simulação de núcleo e imagem: zeramos a coluna da CVE3 (índice 2).
    [1, 1, 0, 1],                                 # Como a coluna inteira é 0, a severidade dessa vulnerabilidade não afeta
    [1, 1, 0, 0],                                 # o resultado — o Roteador perde o peso dela, caindo de 17.0 para 7.2.
    [0, 0, 0, 1],                                 # Conceitualmente: a matriz "ignora" a CVE3, e qualquer vetor com apenas
])                                                # essa entrada não-nula pertence ao núcleo de M.

v_ni = np.array([8.8, 7, 9.8, 7.2])

risco_proprio_ni = M_ni @ v_ni

print(f'''
NI ex1.
Risco próprio: {risco_proprio_ni}
''')

# Transformações geométricas

# Escala
escala = np.array([
    [2, 0],
    [0, 3],
])
v_tg = np.array([1, 1])
print(f'''
TG ex1.
Escala de {v_tg} por
{escala}:

{escala @ v_tg}
''')

# Reflexão em relação ao Y
reflexao = np.array([
    [-1, 0],
    [0, 1],
])
vr = np.array([3, 2])
print(f'''
TG ex2.
Reflexão de {vr} por
{reflexao}:

{reflexao @ vr}
''')

# Rotação (trigonometria)
rotacao = np.array([
    [0, -1],
    [1, 0],
])
v_rt = np.array([1, 0])
print(f'''
TG ex3.
Rotação de {v_rt} por 90°:

{rotacao @ v_rt}
''')

# Verificação de lineraridade
u = np.array([1, 0])
w = np.array([0, 1])

resultado1 = rotacao @ (u + w)                    # T(u + v)
resultado2 = (rotacao @ u) + (rotacao @ w)        # T(u) + T(v)

print(f'''
TL ex1.
T(u.v) = {resultado1}
T(u)+T(v) = {resultado2}
São lineares e iguais? {np.array_equal(resultado1, resultado2)}
''')

# Matriz diagonal
F = np.array([
    [0.8, 0,   0  ],
    [0,   1.5, 0  ],
    [0,   0,   1.2],
])

resultado3 = F @ (M_t2 @ v_t2)
resultado4 = (F @ M_t2) @ v_t2

print(f'''
TD ex1.
Matriz F:
{F}

Utilizando valores do RP ex1.:

F(M.v) = {resultado3}
(F.M)v = {resultado4}
São iguais (associatividade)? {np.array_equal(resultado3, resultado4)}
''')