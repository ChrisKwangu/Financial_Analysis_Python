import numpy as np
import matplotlib.pyplot as plt

S = np.linspace(6000, 8000, 100)
K, r, T, sigma = 7000, 0.02, 1, 0.2
payoff_call = np.maximum(S - K, 0)
plt.plot(S, payoff_call, label='Call Payoff')
plt.title('Option Payoff at Maturity')
plt.xlabel('S&P 500')
plt.ylabel('Payoff ($)')
plt.grid(True)
plt.legend()
plt.show()