import random

def generate_passw(tam):
    mays = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    mins = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caract = mays + mins + nums + chars

    passw = []

    for i in range(tam):
        value = random.choice(caract)
        passw.append(value)
    passw = ''.join(passw)
    return passw

def run():
    tam = int(input("Ingrese el tamaño de la contrasenia: "))
    passw = generate_passw(tam)
    
    print("Tu nueva contrasenia es: " + passw)


if __name__ == '__main__':
    run()