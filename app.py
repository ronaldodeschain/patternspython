import tkinter as tk
from tkinter import messagebox
import document

def adicionar_atendente():
    nome = entrada_nome.get().strip()
    resultado = document.adicionar_atendente(nome)
    if resultado == "vazio":
        messagebox.showwarning("Nome vazio","Digite um nome svp.")
    
    elif resultado == "duplicado":
        messagebox.showinfo("Duplicado","Atendente já existe.")
    elif resultado == "ok":
        entrada_nome.delete(0,tk.END)
        atualizar_interface() 
    
def resetar_atendentes():
    if messagebox.askyesno("Resetar","Deseja resetar os dados de atendentes?"):
        document.resetar_atendentes()
        atualizar_interface()
    
def incrementar_vendas(indice):
    document.incrementar_vendas(indice)
    atualizar_interface()

def decrementar_vendas(indice):
    document.decrementar_vendas(indice)
    atualizar_interface()

def ordenar_por_vendas():
    document.get_atendentes().sort(key=lambda x: x["vendas"],reverse=True)

def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    #Ordenação por número de vendas(decrescente)
    ordenar_por_vendas()

    for i,atendente in enumerate(document.get_atendentes()):
        texto = f"{atendente['nome']} - Vendas: {atendente['vendas']}"
        rotulo = tk.Label(quadro_atendentes,text=texto)
        rotulo.grid(row=i,column=0,sticky="w")

        botao_incrementar = tk.Button(
            quadro_atendentes,
            text="+1",
            command=lambda indice=i: incrementar_vendas(indice)
        )
        botao_incrementar.grid(row=i,column=1)
        botao_decrementar = tk.Button(
            quadro_atendentes,
            text="-1",
            command=lambda indice=i: decrementar_vendas(indice)
        )
        botao_decrementar.grid(row=i,column=2
        )


#Interface Principal
janela = tk.Tk()
janela.title("Controle de Vendas - Document View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5,padx=15)

botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=adicionar_atendente)
botao_adicionar.pack(pady=5,padx=15)

botao_resetar = tk.Button(janela,text="Resetar",command=resetar_atendentes)
botao_resetar.pack(pady=5,padx=15)

quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=10,padx=10)

janela.mainloop()