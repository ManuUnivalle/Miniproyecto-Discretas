# Integrante1: Manuela Delgado Aguirre - 2459640
# Integrante2: Paula Jimena Bohórquez Bermúdez - 2459409
# Docente: Luis Germán Toro Pareja
# Grupo: 50
# Laboratorio 5

import re

# Función que representa el estado q0: "apagado". Tiene menú para encender o no el sistema (transición desde q0)
# Retorna True para hacer transición a q1, False para permanecer en q0 y terminar, o que vuelva a pedir entrada válida
def welcome():
    print("""     BIENVENID@ A LA LIBRERIA BUPEN!"
    -------------------------------------------""")
    
    print("""Deseas encender el programa?
1. Si
2. No""")

    choice = input("Elige una opcion: ")
    if choice == "1":

        print("BUPEN ha iniciado correctamente.")
        return True
    
    elif choice == "2":

        return False
    
    else:
        print("Opcion no valida. Por favor, elige 1 o 2.")
        return welcome()
          
    
# Función que representa el estado q1: validación de credenciales. Usa expresiones regulares tanto para validar el correo como
# la contraseña. Retorna True si las credenciales son válidas para hacer transición a q2 o False para hacer transición a q4
def validate_credentials(email, password):

    pattern_email = r'^[a-zA-Z0-9_.+-]+@correounivalle\.edu\.co$'
    pattern_password = r'^[a-zA-Z0-9@#$%^&+=]{8,}$'

    if re.match(pattern_email, email) and re.match(pattern_password, password):
        print("Credenciales validas.")
        return True
    else:
        print("Credenciales invalidas. Denegado. Intentalo de nuevo\n")
        return False
        
        
# Función que representa el estado q2: verificación del código OTP. Muestra el código de verificación esperado
# Retorna True para hacer transición a q3 si el código es correcto o False si es incorrecto y hacer transición a q4
def two_step_verification(code):
    print(f"""------------------------------------------------------------------------------------------
Este es el código de verificación que hemos hecho para ti: {code}
Necesitamos validar que seas tú
Por favor, ingresa el codigo de verificacion.

----------------------------------------------------------------------------------------------------------""")
    verification_code = input("Codigo de verificacion: ")
    
    if verification_code == code:

        print("Codigo de verificacion correcto.")
        return True
    else:
        print("Codigo de verificacion incorrecto. Denegado. Intentalo de nuevo\n")
        return False


if __name__ == "__main__":
    menu = welcome()

    # Si elige "no encender", el programa termina
    if menu == False:
        print("BUPEN ha cerrado correctamente.")
        exit() 

    # Bucle principal del programa (simula regreso desde q4 a q0)
    while(menu):
        print("""-----------------------------------------------------------------------------------------

Ingresa el correo y la contraseña
Asegurate de que el correo sea de la Universidad del Valle y la contraseña tenga al menos 8 caracteres.

---------------------------------------------------------------------------------------------------------""")
        # Ingreso de credenciales (estado q1)
        email = input("Ingresa tu correo institucional: ")
        password = input("Ingresa tu contraseña: ")

        # Si son válidas pasa a verificación OTP (q2)
        if validate_credentials(email, password):
            otp = "America" # Código OTP fijo

            # Validación OTP
            if two_step_verification(otp):
                # Si pasa ambas validaciones, hace transición al estado final q3 y termina el programa
                print("----------------------------------------------------------------------------------")
                print("Bienvenido a BUPEN!")
                break
            
        # Si falla alguna validacion, hace transición a q4 y luego a su estado inicial q0
            else:
                welcome()

        else:
            welcome()
