frase = "Essa é uma sintese normal de frase feitas para teste"
lista = []

def contador(algo):
    palavra =algo.split()
    for x in palavra:
        lista.append(x)
    tamanho = len(lista)
    return(print(f"O tamanho da frase foi de {tamanho} palavras"))


contador(frase)
for x in range(len(lista)):
    print(x)
