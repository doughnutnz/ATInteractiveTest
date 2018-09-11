
# %%
import sys
import matplotlib.pyplot as plt
# import matplotlib as mpl
import numpy as np
print(type(sys.version[0]))
if int(sys.version[0]) < 3:
    raise Exception("Python 3 or higher is required")
x = np.linspace(0, 2 * np.pi, 1000)
# x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show
