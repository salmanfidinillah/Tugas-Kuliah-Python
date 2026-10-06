def hitung_linear(n):
    operasi = 0
    for i in range(n):
        operasi += 1
    return operasi


print("PERCOBAAN 1 - SATU PERULANGAN")
for n in [5, 10, 20]:
    print(f"n = {n:2} -> {hitung_linear(n)} operasi")
