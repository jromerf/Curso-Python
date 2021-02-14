
def es_primo(numero):
    for i in range(2,numero + 1):
        if numero % i == 0:
            break
    return numero != 1 and i == numero

def run():
    num = int(input("Ingrese el número a evaluar: "))
    if es_primo(num) == True: 
        print("Es primo")
    else:
        print("No es primo")

if __name__ == '__main__':
    run()
