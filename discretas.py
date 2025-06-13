import re

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
          
    

def validate_credentials(email, password):

    pattern_email = r'^[a-zA-Z0-9_.+-]+@correounivalle\.edu\.co$'
    pattern_password = r'^[a-zA-Z0-9@#$%^&+=]{8,}$'

    if re.match(pattern_email, email) and re.match(pattern_password, password):
        print("Credenciales validas.")
        return True
    else:
        print("Credenciales invalidas. Denegado. Intentalo de nuevo")
        return False
        

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
        print("Codigo de verificacion incorrecto. Denegado. Intentalo de nuevo")
        return False


if __name__ == "__main__":
    menu = welcome()
    
    if menu == False:
        print("BUPEN ha cerrado correctamente.")
        exit()

    while(menu):
        print("""-----------------------------------------------------------------------------------------

Ingresa el correo y la contraseña
Asegurate de que el correo sea de la Universidad del Valle y la contraseña tenga al menos 8 caracteres.

---------------------------------------------------------------------------------------------------------""")
        email = input("Ingresa tu correo institucional: ")
        password = input("Ingresa tu contraseña: ")

        if validate_credentials(email, password):
            otp = "univallunoforever"

            if two_step_verification(otp):
                print("----------------------------------------------------------------------------------")
                print("Bienvenido a BUPEN!")
                break
            else:
                welcome()

        else:
            welcome()
