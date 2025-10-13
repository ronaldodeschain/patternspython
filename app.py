import tkinter as tk

atendentes = []

def adicionar_atendente():
    nome = entrada_nome.get().strip()

    if not nome:
        #pendente
        return 
    
    if nome in [a["nome"] for a in atendentes]:
        #pendente
        return

#Interface Principal
janela = tk.Tk()
janela.title("Controle de Vendas - Smart View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5,padx=15)

janela.mainloop()