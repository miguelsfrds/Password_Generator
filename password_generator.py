import secrets
import string
import customtkinter as ctk
import lista_palavras_chave
import webbrowser
import os

#---------------------------JANELA-------------------------------------

app = ctk.CTk()
app.title("Gerador de Senhas")
app.geometry("450x300")

#FRAME
frame = ctk.CTkFrame(app, width=400, height=260)
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
    
    label_aviso.configure(text="")

def copiar_senha():
    senha = campo_senha.get()
    app.clipboard_clear()
    app.clipboard_append(senha)
    label_aviso.configure(text="Senha Copiada!", text_color="green")

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

#-----------------------FEEDBACK MENSAGEM COPIADA----------------------

label_aviso = ctk.CTkLabel(frame, text="")
label_aviso.grid(column=0, columnspan=3)

# ----------------------LINK DO GITHUB---------------------------------

def abrir_github(event=None):
    webbrowser.open("https://github.com/miguelsfrds")

link_github = ctk.CTkLabel(
    frame,
    text="miguelsfrds",
    font=("Consolas", 15),
    text_color="white",
    compound="left"
)
link_github.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
link_github.bind("<Button-1>", abrir_github)

app.mainloop()