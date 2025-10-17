import tkinter as tk
from tkinter import messagebox
import controller 


def alerta(titulo,mensagem):
    messagebox.showinfo(titulo,mensagem)

def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()
#Ordenação por número de vendas(decrescente)
    # ordenar_por_vendas()
    for i,atendente in enumerate(controller.lista_atendentes()):
        texto = f"{atendente['nome']} - Vendas: {atendente['vendas']}"
        rotulo = tk.Label(quadro_atendentes,text=texto)
        rotulo.grid(row=i,column=0,sticky="w")

        botao_incrementar = tk.Button(
            quadro_atendentes,
            text="+1",
            command=lambda indice=i: controller.incrementar_vendas(indice)
        )
        botao_incrementar.grid(row=i,column=1)
        botao_decrementar = tk.Button(
            quadro_atendentes,
            text="-1",
            command=lambda indice=i: controller.decrementar_vendas(indice)
        )
        botao_decrementar.grid(row=i,column=2
        )

#Interface Principal
janela = tk.Tk()
janela.title("Controle de Vendas - Document View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5,padx=15)

botao_adicionar = tk.Button(janela, text="Adicionar Atendente", command=lambda: [controller.adicionar_atendente(entrada_nome.get().strip()),entrada_nome.delete(0,tk.END)])
botao_adicionar.pack(pady=5,padx=15)

botao_resetar = tk.Button(janela,text="Resetar",command=controller.resetar_atendentes)
botao_resetar.pack(pady=5,padx=15)

quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=10,padx=10)