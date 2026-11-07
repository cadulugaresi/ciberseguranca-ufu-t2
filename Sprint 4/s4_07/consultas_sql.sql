-- Este documento se refere às atividades entregáveis de SQL do primeiro semestre do curso de Cibersegurança da UFU.

--------------------------------------------------
--                    S4_06
--------------------------------------------------

-- NOTEBOOKS E SUAS TELAS
-- Selecione os ativos que são notebooks e mostre o nome, o responsável, a tela e o sistema operacional de cada um.
SELECT ativos.id, ativos.nome, ativos.responsavel, notebooks.tela, notebooks.sistema_operacional
FROM ativos
INNER JOIN notebooks ON notebooks.id_ativo = ativos.id;

-- VULNERABILIDADES E OS ATIVOS AFETADOS
-- Selecione cada vulnerabilidade com os ativos que ela afeta e o status do tratamento, ordenando pelo nome da vulnerabilidade.
SELECT vulnerabilidades.nome_vulnerabilidade, ativos.nome, vinculos.status_tratamento
FROM vulnerabilidades
INNER JOIN vinculos ON vinculos.id_vulnerabilidade = vulnerabilidades.id_vulnerabilidade
INNER JOIN ativos ON ativos.id = vinculos.id_ativo
ORDER BY vulnerabilidades.nome_vulnerabilidade;

-- VULNERABILIDADES SEM VÍNCULO
-- Selecione as vulnerabilidades do catálogo que não estão vinculadas a nenhum ativo.
SELECT vulnerabilidades.id_vulnerabilidade, vulnerabilidades.nome_vulnerabilidade, vulnerabilidades.cvss
FROM vulnerabilidades
LEFT JOIN vinculos ON vinculos.id_vulnerabilidade = vulnerabilidades.id_vulnerabilidade
WHERE vinculos.id_vulnerabilidade IS NULL;

--------------------------------------------------
--                    S4_07
--------------------------------------------------

-- QUANTIDADE DE VULNERABILIDADES POR ATIVO
-- Selecione cada ativo com a quantidade de vulnerabilidades vinculadas a ele, incluindo os que não têm nenhuma, ordenando da maior para a menor quantidade.
SELECT ativos.nome, COUNT(vinculos.id_vulnerabilidade) AS quantidade
FROM ativos
LEFT JOIN vinculos ON vinculos.id_ativo = ativos.id
GROUP BY ativos.id
ORDER BY quantidade DESC;

-- VULNERABILIDADES POR FAIXA DE CVSS
-- Selecione a quantidade de vulnerabilidades por faixa de CVSS, considerando as faixas: Crítica (CVSS >= 9.0), Alta (7.0 <= CVSS < 9.0), Média (4.0 <= CVSS < 7.0) e Baixa (CVSS < 4.0).
SELECT CASE
        WHEN cvss >= 9.0 THEN 'Crítica'
        WHEN cvss >= 7.0 THEN 'Alta'
        WHEN cvss >= 4.0 THEN 'Média'
        ELSE 'Baixa'
    END AS faixa, COUNT(*) AS quantidade
FROM vulnerabilidades
GROUP BY faixa
ORDER BY
    quantidade DESC,
    CASE faixa
        WHEN 'Crítica' THEN 1
        WHEN 'Alta' THEN 2
        WHEN 'Média' THEN 3
        ELSE 4
    END;

-- SOMA DOS CVSS POR ATIVO
-- Selecione cada ativo com a soma dos CVSS das vulnerabilidades vinculadas a ele, incluindo os que não têm nenhuma, ordenando da maior para a menor soma.
SELECT ativos.nome, COALESCE(SUM(vulnerabilidades.cvss), 0) AS soma_cvss
FROM ativos
LEFT JOIN vinculos ON vinculos.id_ativo = ativos.id
LEFT JOIN vulnerabilidades ON vulnerabilidades.id_vulnerabilidade = vinculos.id_vulnerabilidade
GROUP BY ativos.id
ORDER BY soma_cvss DESC;

-- ATIVOS CUJA SOMA DOS CVSS É MAIOR QUE 10
-- Selecione os ativos cuja soma dos CVSS das vulnerabilidades vinculadas a eles seja maior que 10, incluindo o nome do ativo e a soma dos CVSS, ordenando da maior para a menor soma.
SELECT ativos.nome, COALESCE(SUM(vulnerabilidades.cvss), 0) AS soma_cvss
FROM ativos
LEFT JOIN vinculos ON vinculos.id_ativo = ativos.id
LEFT JOIN vulnerabilidades ON vulnerabilidades.id_vulnerabilidade = vinculos.id_vulnerabilidade
GROUP BY ativos.id
HAVING soma_cvss > 10
ORDER BY soma_cvss DESC;
