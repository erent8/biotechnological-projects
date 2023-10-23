import matplotlib.pyplot as plt
import random
# Gen dizisini oluşturma
gene_sequence = "ATCGATCGATCGATATCGCGATCGATCG"

# CRISPR hedef dizisi
crispr_target = "ATCG"

# CRISPR/Cas9 kullanarak gen düzeltme simülasyonu
def gene_correction(gene_seq, target):
    if target in gene_seq:
        cut_point = gene_seq.index(target)  # CRISPR'ın kesim noktası
        corrected_seq = gene_seq[:cut_point] + "AGCT" + gene_seq[cut_point + len(target):]  # Düzeltme
        return corrected_seq
    else:
        return "Hedef dizgi gen içinde bulunamadı."


print("Orijinal gen dizisi: ", gene_sequence)
corrected_sequence = gene_correction(gene_sequence, crispr_target)
print("Düzeltme sonrası gen dizisi: ", corrected_sequence)

 
plt.figure(figsize=(10, 6))
plt.plot(range(len(gene_sequence)), [1 if gene_sequence[i] == 'A' else 2 if gene_sequence[i] == 'T' else 3 if gene_sequence[i] == 'C' else 4 for i in range(len(gene_sequence))], marker='o', label='Orijinal Gen Dizisi')
plt.plot(range(len(corrected_sequence)), [1 if corrected_sequence[i] == 'A' else 2 if corrected_sequence[i] == 'T' else 3 if corrected_sequence[i] == 'C' else 4 for i in range(len(corrected_sequence))], marker='o', label='Düzeltme Sonrası Gen Dizisi')
plt.title('Gen Dizisi Analizi')
plt.xlabel('Pozisyon')
plt.ylabel('Nükleotidler')
plt.legend()
plt.show()
