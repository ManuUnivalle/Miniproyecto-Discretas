import customtkinter as ctk
import re
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

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
        text="Salir",
        fg_color="#e74c3c",
        hover_color="#c0392b",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        height=50,
        width=220,
        command=root.destroy
    )
    botton_exit.pack(pady=10)

def show_login():
    clear_widgets()
    global email_entry, password_entry, login_message, login_title_label, login_button, back_button
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
    email_entry = ctk.CTkEntry(frame, font=ctk.CTkFont(size=16), height=27, width=400)
    email_entry.pack(pady=5, fill="x")

    password_label = ctk.CTkLabel(
        frame,
        text="Contraseña:",
        font=ctk.CTkFont(family="Georgia", size=16, weight="bold"),
        text_color="#154360",
        anchor="w"
    )
    password_label.pack(pady=(10, 0), fill="x")
    password_entry = ctk.CTkEntry(frame, show="*", font=ctk.CTkFont(size=16), height=27, width=400)
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

    back_button = ctk.CTkButton(
        frame,
        text="Volver",
        command=show_welcome,
        fg_color="#e74c3c",
        hover_color="#c0392b",
        text_color="white",
        font=ctk.CTkFont(size=16, weight="bold"),
        height=40,
        width=220
    )
    back_button.pack(pady=5)

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
        login_message.configure(text="Credenciales inválidas.\nCorreo debe ser @correounivalle.edu.co y contraseña de al menos 8 caracteres.")
        email_entry.delete(0, "end")      # Limpia el campo de correo
        password_entry.delete(0, "end")   # Limpia el campo de contraseña
        


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

def verify_otp():
    if otp_entry.get() == otp_code:
        show_success()
    else:
        otp_message.configure(text="Código incorrecto. Intenta nuevamente.")

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
 # Set the default color theme to blue
    root = ctk.CTk()
    root.title("BUPEN")
    root.geometry("700x500")
    root.resizable(0, 0)


    show_welcome()
    root.mainloop()