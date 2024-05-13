# Rate vs Bit error ratio plot.

import numpy as np
import matplotlib.pyplot as plt
import math
p = float(input('enter the bit flip probability error '))
d = np.linspace(1,25,num=24)
# d = np.arange(1,25,1) can also be used instead of linspace
Rate = 1/d
BER = d * (np.power(p, d-1))

plt.plot(Rate,BER)
plt.xlabel('Rate')
plt.ylabel('BER')
plt.show()