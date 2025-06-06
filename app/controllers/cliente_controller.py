from app.models import crud

def cadastrar_cliente(nome, idade, email, cpf):
    # ✅ Validação direta via CRUD
    if crud.verificar_existente("clientes", "cpf", cpf) or crud.verificar_existente("clientes", "email", email):
        return False  # Já existe CPF

    dados = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cpf": cpf
    }

    crud.inserir_dado("clientes", dados)
    return True

def consultar_clientes():
    return crud.consultar_todos("clientes")

def excluir_cliente(cliente_id):
    crud.excluir_dado("clientes", cliente_id)