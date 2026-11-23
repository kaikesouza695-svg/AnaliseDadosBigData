def contar_caracteres(texto, caractere_procurado):
    contador = 0

    for letra in texto:
        if letra == caractere_procurado:
            contador += 1
    return contador

texto  = input("digte um texto:")
caractere = input("digite o caractere que deseja procurar:")

resultado = contar_caracteres(texto, caractere)

print(f"o caractere aparece {resultado} vezes.")