import tkinter as tk

def animar_linha_expandir(canvas, linha1, linha2, comprimento_final, tempo):
    largura_atual = 0
    incremento = comprimento_final / tempo

    def expandir():
        nonlocal largura_atual
        if largura_atual < comprimento_final:
            largura_atual += incremento
            canvas.coords(linha1, 0, 1, largura_atual, 1)
            canvas.coords(linha2, 0, 1, largura_atual, 1)
            canvas.after(10, expandir)
    
    expandir()

def animar_linha_recolher(canvas, linha1, linha2, tempo):
    comprimento_inicial = canvas.coords(linha1)[2]
    decremento = comprimento_inicial / tempo

    def recolher():
        nonlocal comprimento_inicial
        if comprimento_inicial > 0:
            comprimento_inicial -= decremento
            if comprimento_inicial < 0:
                comprimento_inicial = 0
            canvas.coords(linha1, 0, 1, comprimento_inicial, 1)
            canvas.coords(linha2, 0, 1, comprimento_inicial, 1)
            canvas.after(10, recolher)
    
    recolher()

def on_focus_in(event):
    input_field = event.widget
    if input_field.get() == input_field.placeholder:
        input_field.delete(0, tk.END)
        input_field.config(fg='white')

    canvas = input_field.canvas
    linha1 = input_field.linha1
    linha2 = input_field.linha2
    animar_linha_expandir(canvas, linha1, linha2, 300, 30)

def on_focus_out(event):
    input_field = event.widget
    if input_field.get() == '':
        input_field.insert(0, input_field.placeholder)
        input_field.config(fg='gray')

    canvas = input_field.canvas
    linha1 = input_field.linha1
    linha2 = input_field.linha2
    animar_linha_recolher(canvas, linha1, linha2, 30)

root = tk.Tk()
root.title('Login')
root.configure(bg='black')
root.geometry('400x500')

def criar_input(master, placeholder, show=None):
    container = tk.Frame(master, bg='black')
    container.pack(pady=20, anchor="center")
    
    input_field = tk.Entry(container, font=('Arial', 14), bd=0, bg='black', fg='gray', insertbackground='white', relief='flat')
    input_field.insert(0, placeholder)
    input_field.placeholder = placeholder
    if show:
        input_field.config(show=show)

    input_field.pack(fill='x')

    canvas = tk.Canvas(container, width=300, height=6, bd=0, highlightthickness=0, bg='black')
    # Linha principal (fina)
    linha1 = canvas.create_line(0, 3, 0, 3, width=2, fill="Blue")
    # Linha de brilho (um pouco mais grossa e semi-transparente)
    linha2 = canvas.create_line(0, 3, 0, 3, width=6, fill="Blue", stipple='gray50')
    canvas.pack(fill='x')

    input_field.canvas = canvas
    input_field.linha1 = linha1
    input_field.linha2 = linha2

    input_field.bind("<FocusIn>", on_focus_in)
    input_field.bind("<FocusOut>", on_focus_out)

    return input_field

frame = tk.Frame(root, bg='black')
frame.place(relx=0.5, rely=0.5, anchor='center')

titulo = tk.Label(frame, text="Bem-vindo de volta", bg='black', fg='white', font=('Arial', 22, 'bold'))
titulo.pack(pady=(0, 30))

# E-mail
entry_email = criar_input(frame, 'Digite seu e-mail')

# Senha
entry_senha = criar_input(frame, 'Digite sua senha', show="*")

# Botão de login (só pra ficar bonito)
btn_login = tk.Button(frame, text="Login", font=('Arial', 14), bg='blue', fg='white', bd=0, relief='flat', activebackground='#9A32CD', activeforeground='white', cursor='hand2')
btn_login.pack(pady=40)

root.mainloop()
