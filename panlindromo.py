def es_palindromo(palabra):
    return palabra == palabra[::-1]


def run():

    palabra = input("Escribe una palabra: ")
    sol = es_palindromo(palabra.lower().replace(' ',''))

    if sol == True: 
        print("Es palíndromo")
    else: 
        print("No es palíndromo")


if __name__ == '__main__':
    run()

