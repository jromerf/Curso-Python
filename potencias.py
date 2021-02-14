
def potencia(num,pot):
    
    if pot == 1: 
        res = 1; 
    else: 
        res = num * potencia(num,pot - 1)
    return res

def run():
    num = int(input("Ingrese el número: "))
    pot = int(input("Ingrese la potencia: "))
    res = potencia(num,pot)

    print("Resultado: " + str(res))


if __name__ == '__main__':
    run()

    