import random

menu = """


 █████╗ ██████╗ ██╗██╗   ██╗██╗███╗   ██╗ █████╗           
██╔══██╗██╔══██╗██║██║   ██║██║████╗  ██║██╔══██╗          
███████║██║  ██║██║██║   ██║██║██╔██╗ ██║███████║          
██╔══██║██║  ██║██║╚██╗ ██╔╝██║██║╚██╗██║██╔══██║          
██║  ██║██████╔╝██║ ╚████╔╝ ██║██║ ╚████║██║  ██║          
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝          
                                                           
                    ███████╗██╗                            
                    ██╔════╝██║                            
                    █████╗  ██║                            
                    ██╔══╝  ██║                            
                    ███████╗███████╗                       
                    ╚══════╝╚══════╝                       
                                                           
███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗  ██████╗     
████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔═══██╗    
██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║   ██║    
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║    
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝    
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝     
                                                           

               -----Ingres un numero------
                   "Recuerda que tienes 
                     3 oportunidades"




"""

def run():
    valor_true = random.randrange(20) # lanzar valores aleatorios entre 0 y 20
    
    vida = 4 # por alguna razon de que permita 5 intentos, si pongo 3 se permiten 4

    while vida > 0 :  # bucle que solo se corre si y solo si la variables no es <= a 0
        opcion = int(input("Ingresa un número: ")) # lectura que se repetira hasta de las vidas sean >= 0
        if opcion == valor_true: # condicional para comparar si el ususario es ganador
            print("Felicidades, te ganaste una sonrisa \U0001F600")
            break 
        else: # condicional por si no gana 
            vida = vida - 1 # reductor de vidas
            print("Intenta de nuevo!")
            continue

if __name__ == "__main__":
    run()