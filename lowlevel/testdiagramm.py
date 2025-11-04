import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
import numpy as np

diagramm = np.array([3,235,1,25,2,3])

plt.plot(diagramm)
plt.yticks(np.arange(0,600,100))
plt.show()