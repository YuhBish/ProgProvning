ord=input("Skriv ett ord i stora bokstäver: ")
A = ord[0]
B = ord[-1]

if A==B:
    print(A,B)
    print("Den första och sista bokstaven är samma")
else:
    print("Fint ord!")