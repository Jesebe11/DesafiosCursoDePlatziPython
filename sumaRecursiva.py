def suma_recursiva(numero):
    #suma_total = numero
    if numero == 1:
        return int(1)
    else:
        suma_total = numero
        suma_total += suma_recursiva(numero - 1)
        return suma_total

def run():
    print('Bienvenido. \t Sumas recursivas')
    print('Para salir, ingrese: 0')
    while True:
        try:
            numero = int(input('Ingresa un número positivo y entero: '))
            if numero == 0:
                break
            if numero < 0:
                print('El numero tiene que ser mayor a 0.')
                pass
            resultado = suma_recursiva(numero)
            print('El resultado de la suma recursiva del número {} es: {}'.format(numero,resultado))
        except:
            print('Error: 1')

if __name__ == '__main__':
    run()