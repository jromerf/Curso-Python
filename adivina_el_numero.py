import random

def run():
    ran = random.randint(1,100)
    adivina = False
    vidas = 10
    print("Tienes "+ str(vidas) + " vidas!")
    

    while(vidas > 1 and adivina == False):

        try:
            num = int(input("[vida "+ str(vidas) +"] Elige un número: "))
        except ValueError:
            print("Ingresa un número correcto")
            continue

        if num == ran:
            adivina = True
            print("Felicidades!")
        elif ran > num: 
            print("Elige un número mayor")
        else: 
            print("Elige un número menor")
        vidas -= 1
    
    if adivina == False : 
        print("Game Over")

if __name__ == '__main__':
    run()