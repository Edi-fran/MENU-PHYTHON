# Funciones para calcular el área y el perímetro de las siguientes  figuras geométricas
#"**************1. Pentágono********************************"
#"**************2. Hexágono*********************************")
#"**************3. Trapecio*********************************")
#"**************4. Paralelogramo****************************")

def calcular_area_perimetro_P(apotema, lado):
    # funcion para area y perimetro del pentagono
    perimetro = 5 * lado
    area = (perimetro * apotema) / 2
    return area, perimetro
#para calcular el perimetro del Hexagono se multiplica el lado por 5  y para el area  se multiplica perimetro por apotema dividido para 2

def calcular_area_perimetro_H(apotema, lado):
    # Funcion para calcular el Area y Perimetro de un Hexagono
    perimetro = 6 * lado
    area = (perimetro * apotema) / 2
    return area, perimetro
#para calcular el perimetro del Hexagono se multiplica el lado por 6  y para el area  se multiplica perimetro por apotema dividido para 2

def calcular_area_T(base_mayor, base_menor, altura):
    # Funcion para calcular el el area de un Trapecio
    area = ((base_mayor + base_menor) * altura) / 2
    return area
#para calcular el Area se suma la base mayor mas la base menor por la altura y la dividimos para 2

def calcular_area_P(base, altura):
    #Funcion para calcular el area de un apralelogramo
    area = base * altura
    return area
# Para calcular el area se  multiplica la base con la altura 

# Función principal que muestra el menú y procesa la entrada del usuario
def menu():
    while True:
        print("\n************Selección de figuras geométricas************")
        print("**************1. Pentágono********************************")
        print("**************2. Hexágono*********************************")
        print("**************3. Trapecio*********************************")
        print("**************4. Paralelogramo****************************")
        print("**************5. Salir************************************")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            apotema = float(input("Ingresar la apotema del pentágono en centímetros: "))
            lado = float(input("Ingresar el lado del pentágono en centímetros: "))
            area, perimetro = calcular_area_perimetro_P(apotema, lado)
            print("calcularemos area del Pentagono")
            print(f"El Pentágono de apotema {apotema} cm tiene un perímetro de {perimetro} cm y un área de {area} cm²")
        
        elif opcion == '2':
            apotema = float(input("Ingresar la apotema del hexágono en centímetros: "))
            lado = float(input("Ingresar el lado del hexágono en centímetros: "))
            area, perimetro = calcular_area_perimetro_H(apotema, lado)
            print("calcularemos area, perimetro del hexágono")
            print(f"El Hexágono de apotema {apotema} cm tiene un perímetro de {perimetro} cm y un área de {area} cm²")

        elif opcion == '3':
            base_mayor = float(input("Ingresar la base mayor del trapecio en centímetros: "))
            base_menor = float(input("Ingresar la base menor del trapecio en centímetros: "))
            altura = float(input("Ingresar la altura del trapecio en centímetros: "))
            area = calcular_area_T(base_mayor, base_menor, altura)
            print("calcularemos area,del Trapecio")
            print(f"El Trapecio de base mayor {base_mayor} cm, base menor {base_menor} cm y altura {altura} cm tiene un área de {area} cm²")

        elif opcion == '4':
            base = float(input("Ingresar la base del paralelogramo en centímetros: "))
            altura = float(input("Ingresar la altura del paralelogramo en centímetros: "))
            area = calcular_area_P(base, altura)
            print("calcularemos area,del Paralelogramo")
            print(f"El Paralelogramo de base {base} cm y altura {altura} cm tiene un área de {area} cm²")

        elif opcion == '5':
            print("Saliendo del programa.")
            print("grcias por utilizar nuestro programa ")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecuta el menú principal
menu()
#trabajo desarrollado por Edilson Guillin primer ciclo en la carrera TECNOLOGIAS D ELA INFORMACION
#UEA ECUADOR 


