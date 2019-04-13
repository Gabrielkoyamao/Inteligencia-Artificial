import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.xlabel('Lógico')
plt.ylabel('Emocional')
plt.title('Sistema Vocacional')
plt.plot([10], [15], 'ro')
#          y   x   y   x
# plt.plot([20, 20, 50, 20])

plt.axis([0,50,0,100])
plt.show()

# rng = np.random.RandomState(0)

# x = rng.randn(100)
# y = rng.randn(100)
# colors = rng.rand(100)
# sizes = 1000 * rng.rand(100)

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
#             cmap='viridis')
# plt.colorbar();  # show color scale
# plt.show()