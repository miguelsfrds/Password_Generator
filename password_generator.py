import secrets
import string
import customtkinter as ctk
import lista_palavras_chave
import os

#---------------------------JANELA-------------------------------------

app = ctk.CTk()
app.title("Gerador de Senhas")
app.geometry("450x300")

try:
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
    app.iconbitmap(icon_path)
except Exception:
    pass

#FRAME
frame = ctk.CTkFrame(app, width=390, height=240)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.grid_propagate(False)

frame.columnconfigure((0, 1, 2), weight=1)

#----------------------------FUNÇÕES----------------------------------

def atualiza_tamanho(valor):
    tamanho = int(valor)
    label_tamanho.configure(text=f"Tamanho: {tamanho}")

def gerar_senha():

    tamanho = int(slider.get())

    palavra_aleatoria = secrets.choice(lista_palavras_chave.palavras_chave)

    alfabeto = ""

    if swt_numeros.get():
        alfabeto += string.digits

    if swt_pontuacoes.get():
        alfabeto += string.punctuation

    if swt_letras.get():
        alfabeto += string.ascii_letters

    if not alfabeto:
        alfabeto = string.ascii_letters

    senha_aleatoria = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))

    senha = f"{palavra_aleatoria}-{senha_aleatoria}"

    campo_senha.delete(0, "end")
    campo_senha.insert(0, senha)

def copiar_senha():
    senha = campo_senha.get()
    app.clipboard_clear()
    app.clipboard_append(senha)

#------------------------LABEL-TAMANHO--------------------------------

label_tamanho = ctk.CTkLabel(frame, text="Tamanho: 8")
label_tamanho.grid(row=0, column=0, columnspan=3, pady=5)

#------------------------SLIDER---------------------------------------

slider = ctk.CTkSlider(
    frame,
    from_=8,
    to=32,
    command=atualiza_tamanho
)

slider.grid(row=1, column=0, columnspan=3, pady=5)
slider.set(8)

#------------------------CAMPO SENHA----------------------------------

campo_senha = ctk.CTkEntry(frame, width=350)
campo_senha.grid(row=2, column=0, columnspan=3, pady=10)

#------------------------SWITCHES-------------------------------------

frame_switches = ctk.CTkFrame(frame, fg_color="transparent")
frame_switches.grid(row=3, column=0, columnspan=3, pady=10)

swt_letras = ctk.CTkSwitch(
    frame_switches,
    text="Letras"
)

swt_numeros = ctk.CTkSwitch(
    frame_switches,
    text="Números"
)

swt_pontuacoes = ctk.CTkSwitch(
    frame_switches,
    text="Símbolos"
)

swt_letras.pack(side="left", padx=10)
swt_numeros.pack(side="left", padx=10)
swt_pontuacoes.pack(side="left", padx=10)

#--------------------------BOTÕES-------------------------------------

frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
frame_botoes.grid(row=4, column=0, columnspan=3, pady=10)

btn_gerar_senha = ctk.CTkButton(
    frame_botoes,
    text="Gerar Senha",
    command=gerar_senha
)

btn_copiar_senha = ctk.CTkButton(
    frame_botoes,
    text="Copiar Senha",
    command=copiar_senha
)

btn_gerar_senha.pack(side="left", padx=10)
btn_copiar_senha.pack(side="left", padx=10)

#----------------------------------------------------------------------

app.mainloop()