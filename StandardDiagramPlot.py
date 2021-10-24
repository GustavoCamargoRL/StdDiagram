# Standard diagram plot using matplotlib 
# Author: Gustavo Lima

import matplotlib.pyplot as plt

use = [0,10000,20000,30000,50000,90000,999999000]      # Inicialization of the use vector by liters
tax = [50.50,50.50,5.79/1000,6.88/1000,9.48/1000,11.23/1000,21.58/1000]   # Inicialization of the tax vector value(R$)/liters
cost = []

# calculus of the total cost of tax per use
for i,litros in enumerate(use):
    if(tax[i] > 1):
        cost.append(tax[i])
    else:
        cost.append((litros-use[i-1])*tax[i])

use[:] = [litros/1000 for litros in use]  # turning liters to cubic meters


# Diagram generation and plot
plt.plot(use,cost, marker='o')
plt.xlim(0,100)
plt.ylim(0,500)
plt.ylabel('cost(R$)')
plt.xlabel('use(m3)')
plt.show()
