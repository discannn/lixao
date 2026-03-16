import numpy as np
import matplotlib.pyplot as plt
#Parametros do sistema
m = 1.0
k = 10.0
b = 0.5
F = 1.0 # a força aplicada é um degrau
#matrizes
A = np.array([[0, 1],
              [-k/m, -b/m]])

B = np.array([[0],
              [1/m]])

 #Simulação
dt = 0.0 # Passo de tempo (s) - quanto menor, mais preciso
t_final = 20 # Tempo total (s)
n_steps = int(t_final/dt)
t = np.linspace(0, t_final, n_steps)

# 4. Inicialização de Vetores
# x_total guardará [posição, velocidade] para cada instante
x_total = np.zeros((n_steps, 2)) 
x = np.array([[0.0], [0.0]])     # Vetor de estado inicial (coluna)

# 5. Loop de Integração (Método de Euler)
for i in range(n_steps):
    x_total[i] = x.flatten()
    
    # Equação: dx = (Ax + BF) * dt
    dxdt = np.dot(A, x) + B * F
    x = x + dxdt * dt

# 6. Visualização
plt.figure(figsize=(10, 5))
plt.plot(t, x_total[:, 0], label='Posição $x(t)$', color='blue')
plt.axhline(y=F/k, color='red', linestyle='--', label='Equilíbrio Estático')
plt.show()