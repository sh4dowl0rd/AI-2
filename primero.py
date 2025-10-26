def validar_rut(rut):
    # Eliminar puntos y convertir a un formato único
    rut = rut.replace(".", "")
    
    # Verificar formato básico
    if not ("-" in rut and len(rut.split("-")) == 2):
        return False
    
    # Separar número y dígito verificador
    numero, dv = rut.split("-")
    
    # Verificar longitud y que sean números
    if not (len(numero) == 8 and numero.isdigit()):
        return False
    
    # Verificar dígito verificador (debe ser número o 'k')
    if len(dv) != 1:
        return False
    if not (dv.isdigit() or dv.lower() == 'k'):
        return False
        
    return True

def validar_nombre(nombre):
    # Verificar que solo contenga letras y espacios
    return nombre.replace(" ", "").isalpha()

def validar_edad(edad):
    try:
        edad = int(edad)
        return 0 < edad < 120  # Rango razonable de edad
    except ValueError:
        return False

def main():
    print("Sistema de registro de personas")
    print("==============================")
    
    while True:
        # Ingreso y validación del RUT
        rut = input("\nIngrese RUT (formato: xx.xxx.xxx-x o xxxxxxxx-x): ")
        if not validar_rut(rut):
            print("Error: RUT inválido. Intente nuevamente.")
            continue
            
        # Ingreso y validación del nombre
        nombre = input("Ingrese nombre: ")
        if not validar_nombre(nombre):
            print("Error: El nombre solo debe contener letras. Intente nuevamente.")
            continue
            
        # Ingreso y validación del apellido
        apellido = input("Ingrese apellido: ")
        if not validar_nombre(apellido):
            print("Error: El apellido solo debe contener letras. Intente nuevamente.")
            continue
            
        # Ingreso y validación de la edad
        edad = input("Ingrese edad: ")
        if not validar_edad(edad):
            print("Error: Edad inválida. Debe ser un número entre 1 y 119.")
            continue
            
        # Si llegamos aquí, todos los datos son válidos
        print("\nDatos registrados correctamente:")
        print(f"RUT: {rut}")
        print(f"Nombre completo: {nombre} {apellido}")
        print(f"Edad: {edad} años")
        break

if __name__ == "__main__":
    main()