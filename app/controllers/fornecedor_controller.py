from app.models import crud

def cadastrar_fornecedor(nome, contato):
    # Verifica se já existe fornecedor com o mesmo nome e contato
    fornecedores = crud.consultar_todos("fornecedores")
    for fornecedor in fornecedores:
        if fornecedor[1] == nome and fornecedor[2] == contato:  # índice 1 = nome, 2 = contato
            return False  # Já existe

    dados = {"nome": nome, "contato": contato}
    crud.inserir_dado("fornecedores", dados)
    return True

def consultar_fornecedores():
    return crud.consultar_todos("fornecedores")

def excluir_fornecedor(fornecedor_id):
    crud.excluir_dado("fornecedores", fornecedor_id)
