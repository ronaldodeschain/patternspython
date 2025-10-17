import document as model

view = None

def atribuir_view(_view):
    global view
    view = _view

def adicionar_atendente(nome):
    resultado = model.adicionar_atendente(nome)

    if resultado == "vazio":
        view.alerta("Nome vazio","O nome não pode ser vazio")
    elif resultado == "duplicado":
        view.alerta("Nome duplicado","Nome já na lista")
    elif resultado == "ok":
        view.atualizar_interface() 
    
def resetar_atendentes():
        model.resetar_atendentes()
        view.atualizar_interface()
    
def incrementar_vendas(indice):
    model.incrementar_vendas(indice)
    view.atualizar_interface()

def decrementar_vendas(indice):
    model.decrementar_vendas(indice)
    view.atualizar_interface()

def lista_atendentes():
    return model.get_atendentes()