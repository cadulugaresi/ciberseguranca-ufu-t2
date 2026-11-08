-- ESTUDOS SQLite | SQL Injection | Python

-- def listar_vulnerabilidades(conexao):
--     vulnerabilidades = conexao.execute("SELECT nome, cvss FROM vulnerabilidades")
--     return vulnerabilidades.fetchall()


-- def mostrar_vulnerabilidades(vulnerabilidades):
--     for nome, cvss in vulnerabilidades:
--         print(f"{nome} - CVSS: {cvss}")

-- vulnerabilidades = listar_vulnerabilidades(conexao)
-- mostrar_vulnerabilidades(vulnerabilidades)

--------------------------------------------------

-- def listar_ativos(conexao):
--     ativos = conexao.execute("SELECT id_ativo, nome, tipo FROM ativos")
--     return ativos.fetchall()


-- def mostrar_ativos(ativos):
--     for id_ativo, nome, tipo in ativos:
--         print(f"[{id_ativo}] {nome} ({tipo})")

-- ativos = listar_ativos(conexao)
-- mostrar_ativos(ativos)

--------------------------------------------------
--            Aplicação de SQL Injection
--------------------------------------------------

-- def buscar_ativo_por_id(conexao, id):
--     id = input("Digite o id do ativo: ")
--     query = f"SELECT id_ativo, nome, tipo FROM ativos WHERE id = '{id}'"
--     resultado = conexao.execute(query)
--     return resultado.fetchall() 


-- def buscar_ativo_por_id_seguro(conexao, id):
--     query = "SELECT id_ativo, nome, tipo FROM ativos WHERE id = ?"
--     resultado = conexao.execute(query, (id,))
--     return resultado.fetchall()

--------------------------------------------------

PRAGMA foreign_keys = ON;

CREATE TABLE ativos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Notebook', 'Impressora', 'Roteador', 'Servidor')),
    setor INTEGER NOT NULL CHECK (setor IN (1, 2, 3, 4, 5)),
    responsavel TEXT NOT NULL,
    status INTEGER NOT NULL CHECK (status IN (1, 2, 3))
);

CREATE TABLE notebooks (
    id_ativo INTEGER PRIMARY KEY,
    tela REAL NOT NULL,
    sistema_operacional TEXT NOT NULL,
    FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE
);

CREATE TABLE impressoras (
    id_ativo INTEGER PRIMARY KEY,
    tecnologia INTEGER NOT NULL CHECK (tecnologia IN (1, 2)),
    cor INTEGER NOT NULL CHECK (cor IN (1, 2)),
    FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE
);

CREATE TABLE roteadores (
    id_ativo INTEGER PRIMARY KEY,
    portas INTEGER NOT NULL CHECK (portas > 0),
    velocidade INTEGER NOT NULL CHECK (velocidade > 0),
    FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE
);

CREATE TABLE servidores (
    id_ativo INTEGER PRIMARY KEY,
    ram INTEGER NOT NULL CHECK (ram > 0),
    armazenamento REAL NOT NULL CHECK (armazenamento > 0),
    FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE
);

CREATE TABLE vulnerabilidades (
    id_vulnerabilidade INTEGER PRIMARY KEY,
    nome_vulnerabilidade TEXT NOT NULL,
    cvss REAL NOT NULL CHECK (cvss >= 0 AND cvss <= 10)
);

CREATE TABLE vinculos (
    id_ativo INTEGER NOT NULL,
    id_vulnerabilidade INTEGER NOT NULL,
    status_tratamento  INTEGER NOT NULL CHECK (status_tratamento IN (1, 2, 3, 4)),
    PRIMARY KEY (id_ativo, id_vulnerabilidade),
    FOREIGN KEY (id_ativo) REFERENCES ativos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_vulnerabilidade) REFERENCES vulnerabilidades(id_vulnerabilidade) ON DELETE CASCADE
);