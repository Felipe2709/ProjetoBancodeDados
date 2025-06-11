from app.models import crud

def registrar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento):
    
    pagamentos = crud.consultar_pagamentos_por_cliente(venda_id)
    for pagamento in pagamentos:
        if pagamento[1] == venda_id:  
            return False  

    crud.criar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento)
    return True

def consultar_pagamentos_por_cliente(cliente_id):
    return crud.consultar_pagamentos_por_cliente(cliente_id)

def consultar_pagamentos():
    return crud.consultar_todos("pagamentos")

def consultar_pagamento_por_id(pagamento_id):
    return crud.consultar_por_id("pagamentos", pagamento_id)

def editar_pagamento(pagamento_id, venda_id, valor_pago, data_pagamento, metodo_pagamento):
    dados = {
        "venda_id": venda_id,
        "valor_pago": valor_pago,
        "data_pagamento": data_pagamento,
        "metodo_pagamento": metodo_pagamento
    }
    crud.atualizar_dado("pagamentos", pagamento_id, dados)
    return True

def excluir_pagamento(pagamento_id):
    crud.excluir_dado("pagamentos", pagamento_id)