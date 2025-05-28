from app.models import crud

def registrar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento):
    # Verifica se já existe pagamento para a mesma venda
    pagamentos = crud.consultar_pagamentos_por_cliente(venda_id)
    for pagamento in pagamentos:
        if pagamento[1] == venda_id:  # índice 1 = venda_id
            return False  # Pagamento já registrado

    crud.criar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento)
    return True

def consultar_pagamentos_por_cliente(cliente_id):
    return crud.consultar_pagamentos_por_cliente(cliente_id)
