import time
import re
import random

def welcome():
    print("""     BIENVENID@ A LA LIBRERIA BUPEN!"
-------------------------------------------""")
    time.sleep(1)
    print("""Deseas encender el programa?
1. Si
2. No""")

    choice = input("Elige una opcion: ")
    if choice == "1":
        print("Iniciando BUPEN...")
        time.sleep(1)
        print("BUPEN ha iniciado correctamente.")
        return True
    elif choice == "2":
        return False
    else:
        print("Opcion no valida. Por favor, elige 1 o 2.")
        return welcome()   
    

def validate_credentials(email, password):

    pattern_email = r'^[a-zA-Z0-9_.+-]+@correounivalle\.edu\.co$'
    pattern_password = r'^[a-zA-Z0-9@#$%^&+=]{8,}$'

    if re.match(pattern_email, email) and re.match(pattern_password, password):
        print("Validando credenciales...")
        time.sleep(1)
        print("Credenciales validas.")
        return True
    else:
        print("Credenciales invalidas. Asegurate de que el correo sea de la Universidad del Valle y la contraseña tenga al menos 8 caracteres.")
        return False
        

def two_step_verification(code):
    print("""------------------------------------------------------------------------------------------

Necesitamos validar que seas tú
Por favor, ingresa el codigo de verificacion.

----------------------------------------------------------------------------------------------------------""")
    verification_code = input("Codigo de verificacion: ")
    
    # Simulando la validacion del codigo
    if verification_code == code:
        time.sleep(1)
        print("Validando codigo de verificacion...")
        time.sleep(1)
        print("Codigo de verificacion correcto.")
        return True
    else:
        print("Codigo de verificacion incorrecto. Intenta nuevamente.")
        return two_step_verification(code) 

def ramdom_coding():
    print("""Generando codigo aleatorio...
----------------------------------------------------------------------------------""")
    time.sleep(1)
    random_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    print(f"Tu codigo de verificación es: {random_code}")
    print("----------------------------------------------------------------------------------")
    time.sleep(1)
    return random_code


if __name__ == "__main__":
    menu = welcome()
    if menu == False:
        print("Cerrando BUPEN...")
        time.sleep(1)
        print("BUPEN ha cerrado correctamente.")
        exit()
    else:
        print("""-----------------------------------------------------------------------------------------

Ingresa el correo y la contraseña
Asegurate de que el correo sea de la Universidad del Valle y la contraseña tenga al menos 8 caracteres.

---------------------------------------------------------------------------------------------------------""")
        email = input("Ingresa tu correo institucional: ")
        password = input("Ingresa tu contraseña: ")
        if validate_credentials(email, password):
            otp = ramdom_coding()
            two_step_verification(otp)
            print("----------------------------------------------------------------------------------")
            print("Bienvenido a BUPEN!")
        else:
            print("Credenciales invalidas. Por favor, intenta nuevamente.")
            exit()







