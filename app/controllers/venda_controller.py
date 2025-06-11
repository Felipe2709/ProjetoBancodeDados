from app.models import crud

def cadastrar_venda(cliente_id, produto_id, data):
    dados = {
        "cliente_id": cliente_id,
        "produto_id": produto_id,
        "data": data
    }
    crud.inserir_dado("vendas", dados)

def consultar_vendas():
    return crud.consultar_todos("vendas")

def excluir_venda(venda_id):
    crud.excluir_dado("vendas", venda_id)

def consultar_vendas_por_periodo(data_inicial, data_final):
    return crud.consultar_vendas_por_periodo(data_inicial, data_final)

def relatorio_vendas_detalhado(data_inicial, data_final):
    return crud.relatorio_vendas_detalhado(data_inicial, data_final)

def consultar_venda_por_id(venda_id):
    return crud.consultar_por_id("vendas", venda_id)

def editar_venda(venda_id, cliente_id, produto_id, data):
    dados = {
        "cliente_id": cliente_id,
        "produto_id": produto_id,
        "data": data
    }
    crud.atualizar_dado("vendas", venda_id, dados)