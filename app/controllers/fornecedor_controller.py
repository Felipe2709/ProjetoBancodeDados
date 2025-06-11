from app.models import crud

def cadastrar_fornecedor(nome, contato, cnpj):
    if crud.verificar_existente("fornecedores", "cnpj", cnpj):
        return False 

    dados = {
        "nome": nome,
        "contato": contato,
        "cnpj": cnpj
    }

    crud.inserir_dado("fornecedores", dados)
    return True

def consultar_fornecedores():
    return crud.consultar_todos("fornecedores")

def excluir_fornecedor(fornecedor_id):
    crud.excluir_dado("fornecedores", fornecedor_id)

def consultar_fornecedor_por_id(fornecedor_id):
    return crud.consultar_por_id("fornecedores", fornecedor_id)

def editar_fornecedor(fornecedor_id, nome, contato, cnpj):
    dados = {
        "nome": nome,
        "contato": contato,
        "cnpj": cnpj
    }
    crud.atualizar_dado("fornecedores", fornecedor_id, dados)
    return True