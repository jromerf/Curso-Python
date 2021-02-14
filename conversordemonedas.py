def conversor(option, moneda):
    if option == 1: 
        valor_dolar = 0.85
    elif option == 2 :
        valor_dolar = 3.30
    else : 
        valor_dolar = 1000.00

    return moneda / valor_dolar

menu = """ 
Bienvenido al conversor de monedas 💛❤💛💰
1 - Euros
2 - Soles
3 - Pesos argentinos
Elige una opcion: 
"""

option = int(input(menu))
moneda = float(input("Ingrese cantidad: "))

dolares = conversor(option,moneda)

print("Esto son $" + str(round(dolares,2)) + " dolares") 