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


def tampilkan_tabel():
    nilai_n = [1, 2, 3, 4, 5, 10, 20]

    print("PERCOBAAN 1 - SATU PERULANGAN")
    for n in [5, 10, 20]:
        print(f"n = {n:2} -> {hitung_linear(n)} operasi")

    print("\nPERCOBAAN 2 - DUA PERULANGAN")
    for n in [3, 5, 10]:
        print(f"n = {n:2} -> {hitung_grid(n)} operasi")

    print("\nPERBANDINGAN")
    print(f"{'n':>4} {'Satu perulangan':>18} {'Dua perulangan':>18}")
    for n in [5, 10, 20]:
        print(f"{n:>4} {hitung_linear(n):>18} {hitung_grid(n):>18}")

    return nilai_n


def tampilkan_grafik(nilai_n):
    jumlah_operasi = [hitung_grid(n) for n in nilai_n]

    plt.figure(figsize=(8, 5))
    plt.plot(nilai_n, jumlah_operasi, marker="o")
    plt.xlabel("Jumlah Data (n)")
    plt.ylabel("Jumlah Operasi")
    plt.title("Pertumbuhan Jumlah Operasi")
    plt.grid(True)
    plt.tight_layout()

    linear = [hitung_linear(n) for n in nilai_n]
    kuadrat = [hitung_grid(n) for n in nilai_n]

    plt.figure(figsize=(8, 5))
    plt.plot(nilai_n, linear, marker="o", label="Satu Perulangan")
    plt.plot(nilai_n, kuadrat, marker="o", label="Dua Perulangan")
    plt.xlabel("Jumlah Data (n)")
    plt.ylabel("Jumlah Operasi")
    plt.title("Perbandingan Pertumbuhan Operasi")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    nilai_n = tampilkan_tabel()
    tampilkan_grafik(nilai_n)
