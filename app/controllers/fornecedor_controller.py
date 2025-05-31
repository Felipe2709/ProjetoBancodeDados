from app.models import crud

def cadastrar_fornecedor(nome, contato, cnpj):
    # ✅ Validação direta via CRUD para o CNPJ
    if crud.verificar_existente("fornecedores", "cnpj", cnpj):
        return False  # Já existe CNPJ

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