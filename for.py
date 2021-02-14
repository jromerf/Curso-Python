def mostrar_cadena(palabra):
    lista = []
    for i in range(len(palabra)):
        lista.append(palabra[i])
    return lista

def run():
    palabra = input("Escribe una palabra: ")
    lista = mostrar_cadena(palabra)
    print(list(lista))


if __name__ == '__main__':
    run()