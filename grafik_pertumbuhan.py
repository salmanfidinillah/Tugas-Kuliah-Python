import matplotlib.pyplot as plt


def hitung_grid(n):
    operasi = 0
    for i in range(n):
        for j in range(n):
            operasi += 1
    return operasi


nilai_n = [1, 2, 3, 4, 5, 10, 20]
jumlah_operasi = []

for n in nilai_n:
    jumlah_operasi.append(hitung_grid(n))

plt.plot(nilai_n, jumlah_operasi, marker="o")
plt.xlabel("Jumlah Data (n)")
plt.ylabel("Jumlah Operasi")
plt.title("Pertumbuhan Jumlah Operasi")
plt.grid()
plt.show()
