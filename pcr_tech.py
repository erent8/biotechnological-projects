import random
import matplotlib.pyplot as plt

# DNA dizisini oluşturma
dna_sequence = "ATCGATCGATCGATCGATCG"

# Primerlerin belirlenmesi
forward_primer = "ATCG"
reverse_primer = "CGAT"

# Boş listeler oluşturma
amplified_sequences = []
cycle_numbers = []
total_length = len(dna_sequence)  # Başlangıçta toplam DNA uzunluğu

# PCR simülasyonu
def pcr_simulation(dna_seq, forward, reverse, cycles, total_length):
    print("Başlangıç DNA Dizisi:", dna_seq)
    for i in range(cycles):
        # Primerlerin eşleşmesi
        forward_match = dna_seq.find(forward)
        reverse_match = dna_seq.find(reverse)

        # DNA amplifikasyonu
        amplified_sequence = dna_seq[forward_match:reverse_match + len(reverse)]
        amplified_sequences.append(total_length)
        cycle_numbers.append(i)

        print(f"Iterasyon {i + 1} - Amplifikasyon: {amplified_sequence}")

        # DNA replikasyonu
        dna_seq += amplified_sequence
        total_length = len(dna_seq)

    return dna_seq, amplified_sequences, cycle_numbers

# Simülasyonu çalıştırma
amplified_dna, amplified_sequences, cycle_numbers = pcr_simulation(dna_sequence, forward_primer, reverse_primer, 10, total_length)
print("Son DNA Dizisi: ", amplified_dna)

# Grafik oluşturma
plt.figure(figsize=(10, 6))
plt.plot(cycle_numbers, amplified_sequences, marker='o', linestyle='--', color='b')
plt.title('PCR Amplifikasyonu')
plt.xlabel('Amplifikasyon Döngüsü')
plt.ylabel('Toplam DNA Uzunluğu')
plt.show()
