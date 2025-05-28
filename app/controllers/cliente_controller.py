from app.models import crud

def cadastrar_cliente(nome, idade, email):
    # Verifica se já existe cliente com o mesmo email
    clientes = crud.consultar_todos("clientes")
    for cliente in clientes:
        if cliente[3] == email:  # índice 3 = email
            return False  # Já existe

    dados = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    crud.inserir_dado("clientes", dados)
    return True

def consultar_clientes():
    return crud.consultar_todos("clientes")

def excluir_cliente(cliente_id):
    crud.excluir_dado("clientes", cliente_id)