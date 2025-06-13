# Integrante1: Manuela Delgado Aguirre - 2459640
# Integrante2: Paula Jimena Bohórquez Bermúdez - 2459409
# Docente: Luis Germán Toro Pareja
# Grupo: 50
# Laboratorio 5


import re
import customtkinter as ctk
import random
import tkinter.messagebox as mbox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# Función que representa el estado q0: "apagado". Tiene menú para encender o no el sistema (transición desde q0)
# y muestra un mensaje de bienvenida. Si el usuario decide encender el sistema, transita al estado q1 (login).
def show_welcome():
    clear_widgets()
    frame = ctk.CTkFrame(root, fg_color="#d7bde2", width=500, height=350)
    frame.pack(expand=True, fill="none", padx=40, pady=40)
    frame.pack_propagate(False)  # Mantiene el tamaño fijo del frame

    label = ctk.CTkLabel(
        frame,
        text="BIENVENID@\nLIBRERIA BUPEN!",
        font=ctk.CTkFont(family="Georgia", size=32, weight="bold"),
        anchor="center",
        justify="center"
    )
    label.pack(pady=40)

    botton_on = ctk.CTkButton(
        frame,
        text="Encender programa",
        fg_color="#a569bd",
        hover_color="#8e44ad",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        height=50,
        width=220,
        command=show_login,
    )
    botton_on.pack(pady=15)

    botton_exit = ctk.CTkButton(
        frame,
        text="Apagar",
        fg_color="#e74c3c",
        hover_color="#c0392b",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        height=50,
        width=220,
        command=root.destroy
    )
    botton_exit.pack(pady=10)

# Función que representa el estado q1: validación de credenciales. Usa expresiones regulares tanto para validar el correo como
# la contraseña. Si las credenciales son correctas, genera un código OTP aleatorio y transita al estado q2.

def show_login():
    clear_widgets()
    global email_entry, password_entry, login_message, login_title_label, login_button
    frame = ctk.CTkFrame(root, fg_color="#d6eaf8", width=600, height=450)
    frame.pack(expand=True, fill="both", padx=40, pady=40)

    login_title_label = ctk.CTkLabel(
        frame,
        text="INICIAR SESIÓN",
        font=ctk.CTkFont(family="Georgia", size=28, weight="bold"),
        text_color="#2874A6")

    login_title_label.pack(pady=(30, 25))

    email_label = ctk.CTkLabel(
        frame,
        text="Correo institucional:",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        text_color="#154360",
        anchor="w"
    )
    email_label.pack(pady=(0, 0), fill="x")
    email_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=16), height=35, width=400)
    email_entry.pack(pady=5, fill="x")

    password_label = ctk.CTkLabel(
        frame,
        text="Contraseña:",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        text_color="#154360",
        anchor="w"
    )
    password_label.pack(pady=(10, 0), fill="x")
    password_entry = ctk.CTkEntry(frame, show="*", font=ctk.CTkFont(size=16), height=35, width=400)
    password_entry.pack(pady=5, fill="x")

    login_message = ctk.CTkLabel(frame, text="", text_color="#C0392B", font=ctk.CTkFont(size=14, weight="bold"))
    login_message.pack(pady=5)

    login_button = ctk.CTkButton(
        frame,
        text="Iniciar sesión",
        command=validate_login,
        fg_color="#58D68D",
        hover_color="#28B463",
        text_color="white",
        font=ctk.CTkFont(size=20, weight="bold"),
        height=40,
        width=220
    )
    login_button.pack(pady=2)

# Función que valida las credenciales ingresadas. Si son correctas, genera un código OTP aleatorio y transita al estado q2.
# Si son incorrectas, muestra un mensaje de error y regresa al estado q0 (bienvenida).
def validate_login():
    email = email_entry.get()
    password = password_entry.get()
    pattern_email = r'^[a-zA-Z0-9_.+-]+@correounivalle\.edu\.co$'
    pattern_password = r'^.{8,}$'
    if re.match(pattern_email, email) and re.match(pattern_password, password):
        global otp_code
        otp_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        show_otp()
    else:
        mbox.showerror("Error", "Credenciales incorrectas. Vuelve a intentarlo.")
        show_welcome()

#Función que representa el estado q2: verificación del código OTP. Muestra el código generado y permite al usuario ingresarlo.
# Si el código es correcto, transita al estado q3 (Aceptado). Si es incorrecto, muestra un mensaje de error y regresa al estado q0 (bienvienida).
def show_otp():
    clear_widgets()
    global otp_entry, otp_message
    frame = ctk.CTkFrame(root, fg_color="#d6eaf8", width=600, height=450)
    frame.pack(expand=True, fill="none", padx=40, pady=40)
    frame.pack_propagate(False)

    otp_title = ctk.CTkLabel(
        frame,
        text="VERIFICACIÓN EN DOS PASOS",
        font=ctk.CTkFont(family="Georgia", size=32, weight="bold"),
        text_color="#2874A6",
        anchor="center",
        justify="center"
    )
    otp_title.pack(pady=(30, 10))

    otp_code_label = ctk.CTkLabel(
        frame,
        text=f"Tu código de verificación es:\n{otp_code}",
        font=ctk.CTkFont(size=22, weight="bold"),
        text_color="#154360",
        anchor="center",
        justify="center"
    )
    otp_code_label.pack(pady=10)

    otp_input_label = ctk.CTkLabel(
        frame,
        text="Ingresa el código:",
        font=ctk.CTkFont(family="Georgia", size=18, weight="bold"),
        text_color="#154360",
        anchor="center"
    )
    otp_input_label.pack(pady=(20, 0))

    otp_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=18), height=40, width=250)
    otp_entry.pack(pady=10)

    otp_message = ctk.CTkLabel(frame, text="", text_color="#C0392B", font=ctk.CTkFont(size=14, weight="bold"))
    otp_message.pack(pady=5)

    verify_button = ctk.CTkButton(
        frame,
        text="Verificar",
        command=verify_otp,
        fg_color="#2874A6",
        hover_color="#154360",
        text_color="white",
        font=ctk.CTkFont(size=20, weight="bold"),
        height=50,
        width=220
    )
    verify_button.pack(pady=20)

# Función que verifica el código OTP ingresado. Si es correcto, transita al estado q3 (éxito). Si es incorrecto, muestra un mensaje de error.
def verify_otp():
    if otp_entry.get() == otp_code:
        show_success()
    else:
        mbox.showerror("Error", "Código incorrecto. Intentalo de Nuevo.")
        show_welcome()

# Función que representa el estado q3: éxito. Muestra un mensaje de bienvenida y un botón para salir del programa.
def show_success():
    clear_widgets()
    frame = ctk.CTkFrame(root, fg_color="#d7bde2", width=600, height=450)
    frame.pack(expand=True, fill="none", padx=40, pady=40)
    frame.pack_propagate(False)

    success_label = ctk.CTkLabel(
        frame,
        text="¡Bienvenido a BUPEN!",
        font=ctk.CTkFont(family="Georgia", size=32, weight="bold"),
        text_color="#117A65",
        anchor="center",
        justify="center"
    )
    success_label.pack(pady=(80, 30))

    exit_button = ctk.CTkButton(
        frame,
        text="Salir",
        command=root.destroy,
        fg_color="#e74c3c",
        hover_color="#c0392b",
        text_color="white",
        font=ctk.CTkFont(size=20, weight="bold"),
        height=50,
        width=220
    )
    exit_button.pack(pady=20)


if __name__ == "__main__":

    root = ctk.CTk()
    root.title("BUPEN")
    root.geometry("700x500")
    root.resizable(0, 0)


    show_welcome()
    root.mainloop()