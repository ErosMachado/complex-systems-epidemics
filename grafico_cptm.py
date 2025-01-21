import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definição de vetores, variáveis e constantes:
A = np.zeros((14, 14))
A[1,2] = 1
A[2,3] = 1
A[4,7] = 1
A[7,8] = 1
A[8,9] = 1
A[4,10] = 1
A[4,11] = 1
A[11,12] = 1
A[12,13] = 1
A[3,4] = 1
A[4,5]= 1
A[5,6]= 1

for i in range(0,14):
  for j in range(0,14):
    if(A[i,j] == 1):
      A[j,i] = 1

lb_vetor = np.full((14),3.0)
n_vetor = np.full((14),10000)
tau_vetor = np.full((14),0.01)

mu = 1.0
h = 0.01
t = 0.0

s_vetor0 = np.full((14),1)
i_vetor0 = np.zeros(14)
r_vetor0 = np.zeros(14)

s_vetor_velho = np.zeros(14)
i_vetor_velho = np.zeros(14)
r_vetor_velho = np.zeros(14)

s_vetor_novo = np.zeros(14)
i_vetor_novo = np.zeros(14)
r_vetor_novo = np.zeros(14)

#populando a cidade específica

s_vetor0[4]= (n_vetor[4]-1)/(n_vetor[4])
i_vetor0[4]=1.0/n_vetor[4]

# Utiliza aqui f-strings para evitar popular as colunas na mão. 
colunas = ["tempo"]
for i in range(14):
    colunas.append(f"s_{i}")
for i in range(14):
    colunas.append(f"i_{i}")
for i in range(14):
    colunas.append(f"r_{i}")
dados = pd.DataFrame(columns=colunas)

for i in range(0, 1000):
  for j in range(1, 14):
    viagem = 0
    for k in range(1, 14):
      viagem = viagem+(tau_vetor[k]*(s_vetor_velho[k]-s_vetor_velho[j])*A[j,k])

    s_vetor_novo[j]= s_vetor_velho[j] + h * (-lb_vetor[j]*i_vetor_velho[j]
                                          * s_vetor_velho[j]+(viagem))
     
    i_vetor_novo[j] = i_vetor_velho[j] + h * (lb_vetor[j] * i_vetor_velho[j]
                                              * s_vetor_velho[j] - mu
                                              * i_vetor_velho[j] + viagem)
        
    r_vetor_novo[j] = r_vetor_velho[j] + h * (mu * i_vetor_velho[j] + viagem)

  s_vetor_velho = s_vetor_novo
  i_vetor_velho = i_vetor_novo
  r_vetor_velho = r_vetor_novo

  lista = [t] + list(s_vetor_novo) + list(i_vetor_novo) + list(r_vetor_novo)
  dados.loc[len(dados)] = lista

# Gráfico: 
plt.figure(figsize=(12, 6))
plt.title("Epidemia pela Rede da CPTM - Modelo resumido")
# O que colocar no plot()?
plt.plot()
plt.xlabel("Tempo")
plt.ylabel("Infectados")
plt.grid()
plt.legend()
plt.show()
