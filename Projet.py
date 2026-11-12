import  matplotlib.pyplot as plt
import numpy as np

months = [1, 3, 6, 9, 12]
prices = [96, 97, 98, 99, 100]     #Contango because prices increase
plt.plot(months, prices, marker='+', label='Futures Curve')
plt.xlabel('Months')
plt.ylabel('Price ($/barrel)')
plt.legend()
plt.title('Oil Futures Curve (Contango)')
plt.grid(True)
plt.show()