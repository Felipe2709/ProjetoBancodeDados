from app.models import crud

def cadastrar_cliente(nome, idade, email, cpf):
    if crud.verificar_existente("clientes", "cpf", cpf) or crud.verificar_existente("clientes", "email", email):
        return False  

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

def consultar_cliente_por_id(cliente_id):
    return crud.consultar_por_id("clientes", cliente_id)

def editar_cliente(cliente_id, nome, idade, email, cpf):
    dados = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "cpf": cpf
    }
    crud.atualizar_dado("clientes", cliente_id, dados)
    return True