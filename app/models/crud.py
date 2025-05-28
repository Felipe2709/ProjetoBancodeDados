import sqlite3

DB_PATH = "app/database/academia.db"


def conectar():
    return sqlite3.connect(DB_PATH)

def inserir_dado(tabela, dados):
    conn = conectar()
    c = conn.cursor()
    campos = ', '.join(dados.keys())
    valores = tuple(dados.values())
    placeholders = ', '.join('?' for _ in dados)
    c.execute(f"INSERT INTO {tabela} ({campos}) VALUES ({placeholders})", valores)
    conn.commit()
    conn.close()

def consultar_todos(tabela):
    conn = conectar()
    c = conn.cursor()
    c.execute(f"SELECT * FROM {tabela}")
    dados = c.fetchall()
    conn.close()
    return dados

def excluir_dado(tabela, id):
    conn = conectar()
    c = conn.cursor()
    c.execute(f"DELETE FROM {tabela} WHERE id = ?", (id,))
    conn.commit()
    conn.close()



def criar_tabela_clientes():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_fornecedores():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            contato TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_produtos():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL,
            fornecedor_id INTEGER,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_vendas():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            produto_id INTEGER,
            data TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    ''')
    conn.commit()
    conn.close()

    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dependentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            cliente_id INTEGER,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')
    conn.commit()
    conn.close()

def criar_tabela_pagamentos():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_id INTEGER,
            valor_pago REAL,
            data_pagamento TEXT,
            metodo_pagamento TEXT,
            FOREIGN KEY (venda_id) REFERENCES vendas(id)
        )
    ''')
    conn.commit()
    conn.close()
def criar_pagamento(venda_id, valor_pago, data_pagamento, metodo_pagamento):
    dados = {
        "venda_id": venda_id,
        "valor_pago": valor_pago,
        "data_pagamento": data_pagamento,
        "metodo_pagamento": metodo_pagamento
    }
    inserir_dado("pagamentos", dados)
def consultar_pagamentos_por_cliente(cliente_id):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT p.id, p.venda_id, p.valor_pago, p.data_pagamento, p.metodo_pagamento
        FROM pagamentos p
        JOIN vendas v ON p.venda_id = v.id
        WHERE v.cliente_id = ?
    ''', (cliente_id,))
    resultados = c.fetchall()
    conn.close()
    return resultados


def consultar_vendas_por_periodo(data_inicial, data_final):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM vendas
        WHERE DATE(data) BETWEEN DATE(?) AND DATE(?)
    ''', (data_inicial, data_final))
    resultados = c.fetchall()
    conn.close()
    return resultados
def consultar_pagamentos_por_cliente(cliente_id):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT p.id, p.venda_id, p.valor_pago, p.data_pagamento, p.metodo_pagamento
        FROM pagamentos p
        JOIN vendas v ON p.venda_id = v.id
        WHERE v.cliente_id = ?
    ''', (cliente_id,))
    resultados = c.fetchall()
    conn.close()
    return resultados


def consultar_vendas_por_periodo(data_inicial, data_final):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM vendas
        WHERE DATE(data) BETWEEN DATE(?) AND DATE(?)
    ''', (data_inicial, data_final))
    resultados = c.fetchall()
    conn.close()
    return resultados
def relatorio_vendas_detalhado(data_inicial, data_final):
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        SELECT v.id, c.nome AS cliente, p.nome AS produto, p.preco, v.data
        FROM vendas v
        INNER JOIN clientes c ON v.cliente_id = c.id
        INNER JOIN produtos p ON v.produto_id = p.id
        WHERE DATE(v.data) BETWEEN DATE(?) AND DATE(?)
    ''', (data_inicial, data_final))
    resultados = c.fetchall()
    conn.close()
    return resultados

def popular_banco():
    conn = conectar()
    c = conn.cursor()

    c.executemany('INSERT INTO clientes (nome, idade, email) VALUES (?, ?, ?)', [
        ("Beatriz", 25, "beatriz@email.com"),
        ("Lucas", 32, "lucas@email.com"),
        ("Ana", 28, "ana@email.com"),
    ])

    c.executemany('INSERT INTO fornecedores (nome, contato) VALUES (?, ?)', [
        ("Força Suplementos", "contato@forca.com"),
        ("GymPower", "suporte@gympower.com")
    ])

    c.executemany('INSERT INTO produtos (nome, preco, fornecedor_id) VALUES (?, ?, ?)', [
        ("Halteres 5kg", 89.90, 1),
        ("Corda de Pular", 29.90, 2),
        ("Barra Olímpica", 299.00, 1)
    ])

    c.executemany('INSERT INTO vendas (cliente_id, produto_id, data) VALUES (?, ?, ?)', [
        (1, 1, "2025-05-23"),
        (2, 2, "2025-05-24"),
        (3, 3, "2025-05-25")
    ])


    c.executemany('INSERT INTO pagamentos (venda_id, valor_pago, data_pagamento, metodo_pagamento) VALUES (?, ?, ?, ?)', [
    (1, 89.90, "2025-05-23", "Pix"),
    (2, 29.90, "2025-05-24", "Cartão"),
    (3, 299.00, "2025-05-25", "Dinheiro")
])



    conn.commit()
    conn.close()
    print("Tabelas populadas com sucesso.")

