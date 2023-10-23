import random
import matplotlib.pyplot as plt

# Örnek organizma listesi
organisms = ['OrganizmaA', 'OrganizmaB', 'OrganizmaC', 'OrganizmaD', 'OrganizmaE']

# Benzerlik matrisi
similarity_matrix = [[1.0, 0.4, 0.2, 0.1, 0.3],
                     [0.4, 1.0, 0.5, 0.2, 0.4],
                     [0.2, 0.5, 1.0, 0.4, 0.6],
                     [0.1, 0.2, 0.4, 1.0, 0.5],
                     [0.3, 0.4, 0.6, 0.5, 1.0]]

# Rastgele benzerlik matrisi oluşturma
for i in range(len(organisms)):
    for j in range(i, len(organisms)):
        if i != j:
            similarity_matrix[i][j] = similarity_matrix[j][i] = round(random.uniform(0.1, 1.0), 2)

# Filogenetik ağaç oluşturma
plt.figure(figsize=(8, 6))
for i in range(len(organisms)):
    for j in range(i, len(organisms)):
        if i != j:
            plt.plot([i, j], [similarity_matrix[i][j], similarity_matrix[i][j]], marker='o', linestyle='-', linewidth=1, markersize=8, color='b')

plt.xticks(range(len(organisms)), organisms, rotation=45)
plt.title('Basit Filogenetik Ağaç')
plt.xlabel('Organizmalar')
plt.ylabel('Benzerlik Skoru')
plt.show()
