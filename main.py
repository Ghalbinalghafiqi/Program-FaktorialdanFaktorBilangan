def fa(n):
    if n == 0:
        return 1
    else:
        return n * fa(n - 1)

n = int(input("Masukkan Nilai = "))

print(n, "! =", fa(n))