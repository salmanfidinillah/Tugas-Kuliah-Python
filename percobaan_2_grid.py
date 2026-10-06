def hitung_grid(n):
    operasi = 0
    for i in range(n):
        for j in range(n):
            operasi += 1
    return operasi


print("PERCOBAAN 2 - DUA PERULANGAN")
for n in [3, 5, 10]:
    print(f"n = {n:2} -> {hitung_grid(n)} operasi")
