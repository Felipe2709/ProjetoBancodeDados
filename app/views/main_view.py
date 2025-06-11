import streamlit as st
from datetime import datetime
from app.models.crud import popular_banco
import pandas as pd
from app.controllers import (
    cliente_controller,
    fornecedor_controller,
    produto_controller,
    pagamento_controller,
    venda_controller
)


def menu():
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Escolha a operação", [
        "Cadastrar Cliente", "Consultar Clientes", "Editar Cliente", "Excluir Cliente",
        "Cadastrar Fornecedor", "Consultar Fornecedores", "Editar Fornecedor", "Excluir Fornecedor",
        "Cadastrar Produto", "Consultar Produtos", "Editar Produto", "Excluir Produto",
        "Cadastrar Venda", "Consultar Vendas", "Editar Venda", "Excluir Venda"
    ])
    if st.sidebar.button("Popular banco"):
        popular_banco()
        st.success("Banco populado com sucesso!")

    return opcao

def interface(opcao):
    if opcao == "Cadastrar Cliente":
        st.header("Cadastro de Cliente")
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0)
        email = st.text_input("Email")
        cpf = st.text_input("CPF")
        if st.button("Salvar"):
            if cliente_controller.cadastrar_cliente(nome, idade, email, cpf):
                st.success("Cliente cadastrado com sucesso!")
            else:
                st.warning("Cliente já existe!")
        
    elif opcao == "Consultar Clientes":
        st.header("Consulta de Clientes")
        clientes = cliente_controller.consultar_clientes()
        if clientes:
            df = pd.DataFrame(clientes, columns=["ID", "Nome", "Idade", "Email", "CPF"])
            st.dataframe(df)
        else:
            st.info("Nenhum cliente cadastrado.")
    
    elif opcao == "Editar Cliente":
        st.header("Edição de Cliente")
        clientes = cliente_controller.consultar_clientes()
        if not clientes:
            st.warning("Nenhum cliente cadastrado para editar.")
            return

        cliente_dict = {f"{c[1]} (CPF: {c[4]})": c[0] for c in clientes}
        cliente_selecionado_str = st.selectbox(
            "Selecione o cliente para editar", list(cliente_dict.keys())
        )
        
        id_para_editar = cliente_dict[cliente_selecionado_str]
        
        st.info(f"Você está editando o registro com ID: {id_para_editar}")
        
        cliente = cliente_controller.consultar_cliente_por_id(id_para_editar)
        
        if cliente:
            nome = st.text_input("Nome", value=cliente[1])
            idade = st.number_input("Idade", min_value=0, value=cliente[2])
            email = st.text_input("Email", value=cliente[3])
            cpf = st.text_input("CPF", value=cliente[4])
            if st.button("Salvar Alterações"):
                cliente_controller.editar_cliente(id_para_editar, nome, idade, email, cpf)
                st.success("Cliente atualizado com sucesso!")
                st.rerun()

    elif opcao == "Excluir Cliente":
        st.header("Exclusão de Cliente")
        id = st.number_input("ID do Cliente", min_value=1)
        if st.button("Excluir"):
            cliente_controller.excluir_cliente(id)
            st.success("Cliente excluído com sucesso!")









    elif opcao == "Cadastrar Fornecedor":
        st.header("Cadastro de Fornecedor")
        nome = st.text_input("Nome")
        contato = st.text_input("Contato")
        cnpj = st.text_input("CNPJ")
        if st.button("Salvar"):
            if fornecedor_controller.cadastrar_fornecedor(nome, contato, cnpj):
                st.success("Fornecedor cadastrado com sucesso!")
            else:
                st.warning("Fornecedor já existe!")

    elif opcao == "Consultar Fornecedores":
        st.header("Consulta de Fornecedores")
        fornecedores = fornecedor_controller.consultar_fornecedores()
        if fornecedores:
            df = pd.DataFrame(fornecedores, columns=["ID", "Nome", "Contato", "CNPJ"])
            st.dataframe(df)
        else:
            st.info("Nenhum fornecedor cadastrado.")

    elif opcao == "Editar Fornecedor":
        st.header("Edição de Fornecedor")
        fornecedores = fornecedor_controller.consultar_fornecedores()
        if not fornecedores:
            st.warning("Nenhum fornecedor cadastrado para editar.")
            return
        
        fornecedor_dict = {f[1]: f[0] for f in fornecedores}
        fornecedor_selecionado_str = st.selectbox(
            "Selecione o fornecedor para editar", list(fornecedor_dict.keys())
        )
        id_para_editar = fornecedor_dict[fornecedor_selecionado_str]
        
        st.info(f"Você está editando o registro com ID: {id_para_editar}")
        
        fornecedor = fornecedor_controller.consultar_fornecedor_por_id(id_para_editar)

        if fornecedor:
            nome = st.text_input("Nome", value=fornecedor[1])
            contato = st.text_input("Contato", value=fornecedor[2])
            cnpj = st.text_input("CNPJ", value=fornecedor[3])
            if st.button("Salvar Alterações"):
                fornecedor_controller.editar_fornecedor(id_para_editar, nome, contato, cnpj)
                st.success("Fornecedor atualizado com sucesso!")
                st.rerun()

    elif opcao == "Excluir Fornecedor":
        st.header("Exclusão de Fornecedor")
        id = st.number_input("ID do Fornecedor", min_value=1)
        if st.button("Excluir"):
            fornecedor_controller.excluir_fornecedor(id)
            st.success("Fornecedor excluído com sucesso!")














    elif opcao == "Cadastrar Produto":
        st.header("Cadastro de Produto")
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço", min_value=0.0)
        fornecedor_id = st.number_input("ID do Fornecedor", min_value=1, key="fornecedor_id_produto")
        if st.button("Salvar"):
            produto_controller.cadastrar_produto(nome, preco, fornecedor_id)
            st.success("Produto cadastrado com sucesso!")

    elif opcao == "Consultar Produtos":
        st.header("Consulta de Produtos")
        produtos = produto_controller.consultar_produtos()
        if produtos:
            df = pd.DataFrame(produtos, columns=["ID", "Nome", "Preço", "Fornecedor_ID"])
            st.dataframe(df)
        else:
            st.info("Nenhum produto cadastrado.")
    
    elif opcao == "Editar Produto":
        st.header("Edição de Produto")
        produtos = produto_controller.consultar_produtos()
        if not produtos:
            st.warning("Nenhum produto cadastrado para editar.")
            return

        produto_dict = {p[1]: p[0] for p in produtos}
        produto_selecionado_str = st.selectbox(
            "Selecione o produto para editar", list(produto_dict.keys())
        )
        id_para_editar = produto_dict[produto_selecionado_str]

        st.info(f"Você está editando o registro com ID: {id_para_editar}")

        produto = produto_controller.consultar_produto_por_id(id_para_editar)
        
        if produto:
            nome = st.text_input("Nome do Produto", value=produto[1])
            preco = st.number_input("Preço", min_value=0.0, value=float(produto[2]))
            
            fornecedores = fornecedor_controller.consultar_fornecedores()
            fornecedor_dict = {f[1]: f[0] for f in fornecedores}
            fornecedor_nomes = list(fornecedor_dict.keys())
            
            current_fornecedor_id = produto[3]
            current_fornecedor_nome = ""
            for nome_forn, id_forn in fornecedor_dict.items():
                if id_forn == current_fornecedor_id:
                    current_fornecedor_nome = nome_forn
                    break
            
            try:
                index = fornecedor_nomes.index(current_fornecedor_nome)
            except ValueError:
                index = 0

            fornecedor_selecionado = st.selectbox("Fornecedor", fornecedor_nomes, index=index)
            fornecedor_id = fornecedor_dict[fornecedor_selecionado]

            if st.button("Salvar Alterações"):
                produto_controller.editar_produto(id_para_editar, nome, preco, fornecedor_id)
                st.success("Produto atualizado com sucesso!")
                st.rerun()

    elif opcao == "Excluir Produto":
        st.header("Exclusão de Produto")
        id = st.number_input("ID do Produto", min_value=1)
        if st.button("Excluir"):
            produto_controller.excluir_produto(id)
            st.success("Produto excluído com sucesso!")
















    elif opcao == "Cadastrar Venda":
        st.header("Cadastro de Venda")
        cliente_id = st.number_input("ID do Cliente", min_value=1, key="cliente_id_venda")
        produto_id = st.number_input("ID do Produto", min_value=1, key="produto_id_venda")
        data = st.date_input("Data da Venda")
        if st.button("Salvar"):
            venda_controller.cadastrar_venda(cliente_id, produto_id, str(data))
            st.success("Venda cadastrada com sucesso!")

    elif opcao == "Consultar Vendas":
        st.header("Consulta de Vendas")
        vendas = venda_controller.consultar_vendas()
        if vendas:
            df = pd.DataFrame(vendas, columns=["ID", "Cliente_ID", "Produto_ID", "Data"])
            st.dataframe(df)
        else:
            st.info("Nenhuma venda registrada.")

    elif opcao == "Editar Venda":
        st.header("Edição de Venda")
        vendas = venda_controller.consultar_vendas()
        if not vendas:
            st.warning("Nenhuma venda registrada para editar.")
            return

        
        venda_ids = [v[0] for v in vendas]
        id_para_editar = st.selectbox("Selecione o ID da venda para editar", venda_ids)

        st.info(f"Você está editando o registro com ID: {id_para_editar}")

        venda = venda_controller.consultar_venda_por_id(id_para_editar)

        if venda:
            
            clientes = cliente_controller.consultar_clientes()
            cliente_dict = {c[1]: c[0] for c in clientes}
            cliente_nomes = list(cliente_dict.keys())
            current_cliente_id = venda[1]
            current_cliente_nome = ""
            for nome_cli, id_cli in cliente_dict.items():
                if id_cli == current_cliente_id:
                    current_cliente_nome = nome_cli
                    break
            
            try:
                index_cliente = cliente_nomes.index(current_cliente_nome)
            except ValueError:
                index_cliente = 0
            
            cliente_selecionado = st.selectbox("Cliente", cliente_nomes, index=index_cliente)
            cliente_id = cliente_dict[cliente_selecionado]

            produtos = produto_controller.consultar_produtos()
            produto_dict = {p[1]: p[0] for p in produtos}
            produto_nomes = list(produto_dict.keys())
            current_produto_id = venda[2]
            current_produto_nome = ""
            for nome_prod, id_prod in produto_dict.items():
                if id_prod == current_produto_id:
                    current_produto_nome = nome_prod
                    break
            
            try:
                index_produto = produto_nomes.index(current_produto_nome)
            except ValueError:
                index_produto = 0

            produto_selecionado = st.selectbox("Produto", produto_nomes, index=index_produto)
            produto_id = produto_dict[produto_selecionado]

            data_venda = st.date_input("Data da Venda", value=datetime.strptime(venda[3], '%Y-%m-%d').date())

            if st.button("Salvar Alterações"):
                venda_controller.editar_venda(id_para_editar, cliente_id, produto_id, str(data_venda))
                st.success("Venda atualizada com sucesso!")
                st.rerun()

    elif opcao == "Excluir Venda":
        st.header("Exclusão de Venda")
        id = st.number_input("ID da Venda", min_value=1)
        if st.button("Excluir"):
            venda_controller.excluir_venda(id)
            st.success("Venda excluída com sucesso!")



    elif opcao == "Popular Banco de Dados": 
        st.header("Popular Banco de Dados")
        if st.button("Popular"):
            popular_banco()
            st.success("Banco populado com sucesso!")

def exibir_views_personalizadas():
    st.sidebar.markdown("## Opções Personalizadas")
    opcao = st.sidebar.selectbox("Escolha uma opção:", [
        "Pagamentos", "Relatório de Vendas"
    ])

    if opcao == "Pagamentos":
        acao = st.sidebar.radio("O que deseja fazer?", [
            "Registrar Pagamento", "Consultar Pagamentos", "Editar Pagamento", "Excluir Pagamento"
        ])
        if acao == "Registrar Pagamento":
            pagamento_view()
        elif acao == "Consultar Pagamentos":
            consultar_pagamentos_view()
        elif acao == "Editar Pagamento":
            editar_pagamento_view()
        elif acao == "Excluir Pagamento":
            excluir_pagamento_view()


    elif opcao == "Relatório de Vendas":
        relatorio_vendas_view()

def pagamento_view():
    st.header("Registro de Pagamento")
    venda_id = st.number_input("ID da Venda", min_value=1, key="venda_id_pagamento")
    valor_pago = st.number_input("Valor Pago", min_value=0.0, key="valor_pago_pagamento")
    data_pagamento = st.date_input("Data do Pagamento")
    metodo_pagamento = st.selectbox("Método de Pagamento", ["Dinheiro", "Cartão", "Pix"])
    if st.button("Registrar"):
        if pagamento_controller.registrar_pagamento(venda_id, valor_pago, str(data_pagamento), metodo_pagamento):
            st.success("Pagamento registrado com sucesso!")
        else:
            st.warning("Pagamento já foi registrado para esta venda!")

def consultar_pagamentos_view():
    st.header("Consulta de Pagamentos")
    clientes = cliente_controller.consultar_clientes()
    if not clientes:
        st.info("Nenhum cliente cadastrado.")
        return

    cliente_dict = {f"{c[1]} (ID {c[0]})": c[0] for c in clientes}
    escolha = st.selectbox("Selecione um cliente:", list(cliente_dict.keys()))
    cliente_id = cliente_dict[escolha]

    pagamentos = pagamento_controller.consultar_pagamentos_por_cliente(cliente_id)
    if pagamentos:
        df = pd.DataFrame(pagamentos, columns=["Pagamento_ID", "Venda_ID", "Valor Pago", "Data", "Método"])
        st.dataframe(df)
    else:
        st.warning("Nenhum pagamento registrado para este cliente.")

def editar_pagamento_view():
    st.header("Edição de Pagamento")
    
    pagamentos = pagamento_controller.consultar_pagamentos()
    if not pagamentos:
        st.warning("Nenhum pagamento registrado para editar.")
        return

    pagamento_ids = [p[0] for p in pagamentos]
    id_para_editar = st.selectbox("Selecione o ID do pagamento para editar", pagamento_ids)

    st.info(f"Você está editando o registro com ID: {id_para_editar}")

    pagamento = pagamento_controller.consultar_pagamento_por_id(id_para_editar)

    if pagamento:
        vendas = venda_controller.consultar_vendas()
        venda_dict = {f"Venda {v[0]} (Cliente ID: {v[1]})": v[0] for v in vendas}
        venda_nomes = list(venda_dict.keys())
        current_venda_id = pagamento[1]
        current_venda_nome = ""
        for nome, id_venda in venda_dict.items():
            if id_venda == current_venda_id:
                current_venda_nome = nome
                break
        
        try:
            index_venda = venda_nomes.index(current_venda_nome)
        except ValueError:
            index_venda = 0
            
        venda_selecionada = st.selectbox("Venda", venda_nomes, index=index_venda)
        venda_id = venda_dict[venda_selecionada]

        valor_pago = st.number_input("Valor Pago", min_value=0.0, value=float(pagamento[2]))
        data_pagamento = st.date_input("Data do Pagamento", value=datetime.strptime(pagamento[3], '%Y-%m-%d').date())
        
        metodos = ["Dinheiro", "Cartão", "Pix"]
        current_metodo = pagamento[4]
        try:
            index_metodo = metodos.index(current_metodo)
        except ValueError:
            index_metodo = 0
        metodo_pagamento = st.selectbox("Método de Pagamento", metodos, index=index_metodo)

        if st.button("Salvar Alterações"):
            pagamento_controller.editar_pagamento(id_para_editar, venda_id, valor_pago, str(data_pagamento), metodo_pagamento)
            st.success("Pagamento atualizado com sucesso!")
            st.rerun()


def excluir_pagamento_view():
    st.header("Exclusão de Pagamento")
    pagamentos = pagamento_controller.consultar_pagamentos()
    if not pagamentos:
        st.warning("Nenhum pagamento registrado para excluir.")
        return
    pagamento_ids = [p[0] for p in pagamentos]
    id_para_excluir = st.selectbox("Selecione o ID do pagamento para excluir", pagamento_ids)
    if st.button("Excluir Pagamento"):
        pagamento_controller.excluir_pagamento(id_para_excluir)
        st.success(f"Pagamento com ID {id_para_excluir} foi excluído com sucesso!")
        st.rerun()
            
def relatorio_vendas_view():
    st.header("Relatório de Vendas")
    data_inicial = st.date_input("Data inicial")
    data_final = st.date_input("Data final")

    if st.button("Gerar Relatório"):
        vendas = venda_controller.relatorio_vendas_detalhado(str(data_inicial), str(data_final))
        if vendas:
            df = pd.DataFrame(vendas, columns=["ID", "Cliente", "Produto", "Preço", "Data"])
            st.dataframe(df)
        else:
            st.info("Nenhuma venda encontrada no período.")


