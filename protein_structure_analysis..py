import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Rastgele protein yapısı oluşturma
num_atoms = 100
x = np.random.random(num_atoms)
y = np.random.random(num_atoms)
z = np.random.random(num_atoms)

# 3D grafiği oluşturma
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='o')
ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')
ax.set_zlabel('Z Ekseni')
ax.set_title('Rastgele Protein Yapısı')
plt.show()
