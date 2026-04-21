import secrets
import string
import customtkinter as ctk

#-----------------------------JANELA------------------------------------

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.iconbitmap("icon.ico")
app.title("Gerador de Senhas")
app.geometry("350x300")
app.resizable(False, False)

#-----------------------------LAYOUT------------------------------------

# grid principal
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

main_container = ctk.CTkFrame(app)
main_container.grid(row=0, column=0, padx=15, pady=20, sticky="nsew")

# grid interno
main_container.grid_columnconfigure(0, weight=1)
main_container.grid_columnconfigure(1, weight=1)

#-----------------------------TÍTULO------------------------------------

label = ctk.CTkLabel(
    main_container,
    text="Tamanho: 8",
    font=("Gotham Narrow Bold", 18)
)
label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

#-----------------------------SLIDER------------------------------------

def atualizar_valor(valor):
    valor = int(float(valor))
    label.configure(text=f"Tamanho: {valor}")

slider = ctk.CTkSlider(
    main_container,
    from_=8,
    to=32,
    command=atualizar_valor
)
slider.grid(row=1, column=0, columnspan=2, padx=30, pady=10, sticky="ew")
slider.set(8)

#--------------------------CAMPO SENHA----------------------------------

label_password = ctk.CTkEntry(
    main_container,
    justify="center",
    width=250,
    font=("Arial", 14)
)
label_password.grid(row=2, column=0, columnspan=2, padx=30, pady=20, sticky="ew")

#-----------------------------FUNÇÕES------------------------------------

def gerar_senha():
    tamanho = int(slider.get())
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))

    label_password.delete(0, "end")
    label_password.insert(0, senha)

    status.configure(text="")

def copiar_senha():
    senha = label_password.get()
    if senha:
        app.clipboard_clear()
        app.clipboard_append(senha)
        status.configure(text="Senha Copiada", text_color="green")

#-----------------------------BOTÕES------------------------------------

btn_gerar = ctk.CTkButton(
    main_container,
    text="Gerar senha",
    command=gerar_senha
)
btn_gerar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

btn_copiar = ctk.CTkButton(
    main_container,
    text="Copiar",
    command=copiar_senha
)
btn_copiar.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

#---------------------------STATUS COPIAR-------------------------------

status = ctk.CTkLabel(main_container, text="")
status.grid(row=4, column=0, columnspan=2, pady=(5, 10))

#-----------------------------MAINLOOP----------------------------------

app.mainloop()