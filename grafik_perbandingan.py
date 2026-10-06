import matplotlib.pyplot as plt


def hitung_linear(n):
    operasi = 0
    for i in range(n):
        operasi += 1
    return operasi


def hitung_grid(n):
    operasi = 0
    for i in range(n):
        for j in range(n):
            operasi += 1
    return operasi


nilai_n = [1, 2, 3, 4, 5, 10, 20]
linear = []
kuadrat = []

for n in nilai_n:
    linear.append(hitung_linear(n))
    kuadrat.append(hitung_grid(n))

print("PERBANDINGAN")
print(f"{'n':>4} {'Satu perulangan':>18} {'Dua perulangan':>18}")
for n in [5, 10, 20]:
    print(f"{n:>4} {hitung_linear(n):>18} {hitung_grid(n):>18}")

plt.plot(nilai_n, linear, marker="o", label="Satu Perulangan")
plt.plot(nilai_n, kuadrat, marker="o", label="Dua Perulangan")
plt.xlabel("Jumlah Data (n)")
plt.ylabel("Jumlah Operasi")
plt.title("Perbandingan Pertumbuhan Operasi")
plt.legend()
plt.grid()
plt.show()
