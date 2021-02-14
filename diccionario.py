
def run():
    mi_diccionario = { 
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }

    print(mi_diccionario['key1'])

    poblacion_pais = {
        'Argentina' : 44935281,
        'Brasil' : 123110078,
        'Colombia' : 4550330,
    }

    for pais,poblacion in poblacion_pais.items(): #keys() values()
        print(pais + " tiene "+ str(poblacion) + " habitantes ")


if __name__ == '__main__':
    run()