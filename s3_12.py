import numpy as np
import math

verdadeiro = 1 / 3                                # Erro absoluto e relativo
aproximado = 0.33                                 # abs é o valor absoluto!!!
erro_abs = abs(verdadeiro - aproximado)
erro_rel = erro_abs / abs(verdadeiro)

print(0.1 + 0.2 == 0.3)                           # Ponto flutuante
print(math.isclose(0.1 + 0.2, 0.3))

pi = math.pi                                      # Truncamento e arredondamento
truncado = math.trunc(pi * 1000) / 1000           # Truncamento corta os dígitos posteriores aos escolhidos
arredondado = round(pi, 3)                        # Arredondamento aumenta o último dígito escolhido se o primeiro após ele for >= 5
erro_trunc = abs(pi - truncado)
erro_arre = abs(pi - arredondado)
print(f'''
Pi: {pi} | Truncado: {truncado} | Arredondado: {arredondado}
Erro do truncado: {erro_trunc} | Erro do arredondado: {erro_arre}''')
errado = input('Qual errou menos? (t/a)').strip().lower()
if errado == 't':
    print(f'Resposta incorreta! O arredondado errou menos por {erro_trunc - erro_arre}.')
elif errado == 'a':
    print(f'Resposta correta! O arredondado errou menos por {erro_trunc - erro_arre}.')
else:
    print(f'Resposta inválida! O arredondado errou menos por {erro_trunc - erro_arre}.')

b = np.array([23.0, 15.8, 17.0])                  # risco próprio (S3_09)
A = np.array([[0, 0.5, 0], [0, 0, 0.2], [0, 0, 0]])  # dependências entre equipamentos
M = np.eye(3) - A                                 # I - A, matriz do sistema
kappa = np.linalg.cond(M)   
                                                  # número de condição: amplificação de erros
print(f'Sistema de risco: \n kappa = {kappa}')
if kappa > 1 / np.finfo(float).eps:               # acima de ~4,5e15
    print("Erro: matriz praticamente singular. Revise as dependências.")  # recusa
elif kappa > 1e8:                                 # perde ~8 dígitos
    print("Aviso: resultado pouco confiável.")    # resolve e avisa
else:                                             # até 1e8
    print("Matriz saudável: pode resolver normalmente.")  # resolve normal

n = 12                                            # tamanho da matriz
H = np.zeros((n, n))                              # matriz n x n só de zeros (essa parte o claude fez pra mim)
for i in range(n):                                # percorre as linhas
    for j in range(n):                            # percorre as colunas
        H[i][j] = 1 / (i + j + 1)                 # fórmula de Hilbert
x_certo = np.ones(n)                              # resposta que queremos (tudo 1)
b_h = H @ x_certo                                 # b que produz essa resposta
res_s = np.linalg.norm(H @ np.linalg.solve(H, b_h) - b_h)  # resíduo do solve
res_i = np.linalg.norm(H @ (np.linalg.inv(H) @ b_h) - b_h)  # resíduo do inv
print(np.linalg.cond(H), res_s, res_i)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9.0000000001]])  
x_certo = np.array([1, 1, 1])                    
b = A @ x_certo                                   
x_solve = np.linalg.solve(A,b)                    
x_inv = np.linalg.inv(A) @ b              
res_s = np.linalg.norm(A @ x_solve - b)           
res_i = np.linalg.norm(A @ x_inv - b)  
print(np.linalg.cond(A), res_s, res_i)

print(f'Hilbert: kappa = {np.linalg.cond(H):.1e} | resíduo solve = {res_s:.1e} | resíduo inv = {res_i:.1e}')