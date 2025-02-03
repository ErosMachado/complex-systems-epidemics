import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nomes_cidades = [
    "Mauá", "Santo André", "São Caetano", "São Paulo", "Osasco",
    "Itapevi", "Caieiras", "Franco do Rocha", "Jundiaí", "Guarulhos",
    "Ferraz de Vasconcelos", "Suzano", "Mogi das Cruzes"
]

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
#vetor começando em São Paulo com ele tendo lb = 3.0
#lb_vetor = [0,1.5,2.0,2.5,3.0,2.5,2.0,2.5,2.0,1.5,2.5,2.5,2.0,1.5]

#vetor começando em São Paulo mas com PA de razão positiva de r= 0.5
#lb_vetor = [0,4.5,4.0,3.5,3.0,3.5,4.0,3.5,4.0,4.5,3.5,3.5,4.0,4.5]

#r=1
lb_vetor = [0,6.0,5.0,4.0,3.0,4.0,5.0,4.0,5.0,6.0,4.0,4.0,5.0,6.0]


n_vetor = np.full((14),10000)
tau_vetor = np.full((14),0.05)

mu = 1.0
h = 0.01
t = 0.0

s_vetor0 = np.full((14),1.0)
i_vetor0 = np.zeros(14)
r_vetor0 = np.zeros(14)

s_vetor_velho = np.zeros(14)
i_vetor_velho = np.zeros(14)
r_vetor_velho = np.zeros(14)

s_vetor_novo = np.zeros(14)
i_vetor_novo = np.zeros(14)
r_vetor_novo = np.zeros(14)

#populando a cidade específica

s_vetor0[4] = 1.0*(n_vetor[4]-1)/n_vetor[4]
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

s_vetor_velho = s_vetor0
i_vetor_velho = i_vetor0
r_vetor_velho = r_vetor0
t = 0
for i in range(0, 1000):
  for j in range(1, 14):
    viagemS = 0
    viagemR = 0
    viagemI = 0
    for k in range(1, 14):
      viagemS = viagemS+(tau_vetor[k]*(s_vetor_velho[k]-s_vetor_velho[j])*A[j,k])
      viagemR = viagemR+(tau_vetor[k]*(r_vetor_velho[k]-r_vetor_velho[j])*A[j,k])
      viagemI = viagemI+(tau_vetor[k]*(i_vetor_velho[k]-i_vetor_velho[j])*A[j,k])

    s_vetor_novo[j]= s_vetor_velho[j] + h * (-lb_vetor[j]*i_vetor_velho[j]
                                          * s_vetor_velho[j]+(viagemS))

    i_vetor_novo[j] = i_vetor_velho[j] + h * (lb_vetor[j] * i_vetor_velho[j]
                                              * s_vetor_velho[j] - mu
                                              * i_vetor_velho[j] + viagemI)

    r_vetor_novo[j] = r_vetor_velho[j] + h * (mu * i_vetor_velho[j] + viagemR)

  s_vetor_velho = s_vetor_novo
  i_vetor_velho = i_vetor_novo
  r_vetor_velho = r_vetor_novo
  t = t+h
  lista = [t] + list(s_vetor_novo) + list(i_vetor_novo) + list(r_vetor_novo)
  dados.loc[len(dados)] = lista


dados["itotal"] = dados["i_1"]
for i in range(2,14):
  dados["itotal"] += dados[f"i_{i}"]
dados["itotal"] = dados["itotal"]/13.0
# Gráfico:
plt.figure(figsize=(16, 9))
plt.title("Epidemia pela Rede da CPTM começando em São Paulo", fontsize=18,
          fontweight="bold")
for i in range(1,14):
  plt.plot(dados["tempo"], 100*dados[f"i_{i}"], label=nomes_cidades[i-1], linewidth=1.8)
plt.plot(dados["tempo"], 100*dados["itotal"], label=f"Total",color='black',linewidth=3.5)
plt.xlabel("Tempo (semanas)", fontsize=18,fontweight="bold")
plt.ylabel("Infectados (%)", fontsize=18,fontweight="bold")
plt.legend(title="Cidades", title_fontsize=18, fontsize=16, loc="upper right",
           frameon=True, framealpha=0.9)
plt.tight_layout()
plt.tick_params(axis='both', which='major', labelsize=18)
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)
plt.show()
