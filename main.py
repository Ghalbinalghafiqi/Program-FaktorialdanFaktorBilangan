def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def faktor(n):
    return [i for i in range(1, n + 1) if n % i == 0]

while True:
    n = int(input("Masukkan Nilai = "))
    
    print("Pilih Menu:")
    print("A. Faktorial")
    print("B. Faktor")
    
    pilihan = input("Masukkan pilihan (A/B): ").upper()
    
    if pilihan == 'A':
        print(f"{n}! = {factorial(n)}")
    elif pilihan == 'B':
        print(f"Faktor dari {n} adalah: {faktor(n)}")
    else:
        print("Pilihan tidak valid! Silakan pilih A atau B.")
    
    print()