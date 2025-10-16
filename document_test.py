import document 

def test_adicao_e_duplicacao():
    document.resetar_atendentes()
    assert document.adicionar_atendente("Pessoa") == "ok"
    assert document.adicionar_atendente("") == "vazio"
    assert document.adicionar_atendente("Pessoa") == " duplicado"

def test_incremento():
    document.resetar_atendentes()
    document.adicionar_atendente("Pessoa")
    document.incrementar_vendas(0)
    assert document.get_atendentes()[0]["vendas"] == 1

def test_decremento():
    document.resetar_atendentes()
    document.adicionar_atendente("Pessoa")
    document.decrementar_vendas(0)
    assert document.get_atendentes()[0]["vendas"]==-1

if __name__=="__main__":
    test_adicao_e_duplicacao()
    test_incremento()
    test_decremento()
    print("Todos os testes passaram :D")