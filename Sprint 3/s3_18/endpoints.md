# API de Ativos — S3_18

API REST de ativos de TI e vulnerabilidades, usada para estudar os princípios REST e os testes de integração com o Postman.

A API é simulada com o **json-server**, que lê o arquivo `db.json` e cria automaticamente os endpoints REST para cada recurso.

---

## ✨ Como rodar

1. Ter o **Node.js** instalado (`node -v` para conferir)
2. No Terminal, entrar na pasta `s3_18`
3. Rodar:

```
npx json-server@0.17.4 --watch db.json
```

4. A API fica disponível em: **`http://localhost:3000`**

> ⚠️ Os métodos POST, PUT, PATCH e DELETE alteram o `db.json` de verdade. O arquivo `db-original.json` é um backup do estado inicial do banco.

---

## 🫧 Recurso: ativos (implementado)

Cada ativo tem o formato:

```json
{
    "id": 1,
    "nome": "Servidor Web",
    "responsavel": "Cadu",
    "setor": "TI",
    "vulnerabilidadesAbertas": 3
}
```

### Listar ativos
- `GET /ativos` → lista todos os ativos
- Resposta: **200 OK** com uma lista de ativos

### Buscar um ativo
- `GET /ativos/{id}` → mostra um ativo pelo ID
- Resposta: **200 OK** com o ativo
- Se o ID não existir: **404 Not Found**

### Cadastrar ativo
- `POST /ativos` → cadastra um ativo (o `id` é gerado pelo servidor)
- Body:
```json
{
    "nome": "Câmera de Segurança",
    "responsavel": "Rafael Torres",
    "setor": "Segurança",
    "vulnerabilidadesAbertas": 1
}
```
- Resposta: **201 Created** com o ativo criado, já com o `id`

### Substituir ativo
- `PUT /ativos/{id}` → substitui o ativo **inteiro** pelo que foi enviado
- Body: o ativo completo (os campos que ficarem de fora são apagados)
- Resposta: **200 OK** com o ativo atualizado

### Editar ativo
- `PATCH /ativos/{id}` → altera **só os campos enviados**
- Body (exemplo): `{ "vulnerabilidadesAbertas": 0 }`
- Resposta: **200 OK** com o ativo atualizado

### Remover ativo
- `DELETE /ativos/{id}` → remove um ativo
- Resposta: **200 OK** com `{}` (muitas APIs usam **204 No Content** nesse caso)

### Listar vulnerabilidades de um ativo
- `GET /ativos/{id}/vulnerabilidades` → lista as vulnerabilidades ligadas a um ativo (pelo campo `ativoId`)
- Resposta: **200 OK** com uma lista (vazia `[]` se o ativo não tiver vulnerabilidades)

---

## ✨ Recurso: vulnerabilidades (projetado para o Trabalho 2)

Cada vulnerabilidade tem o formato:

```json
{
    "id": 1,
    "titulo": "TLS desatualizado",
    "cvss": 7.5,
    "ativoId": 1
}
```

O campo `ativoId` liga a vulnerabilidade a um ativo. Uma vulnerabilidade pode ser cadastrada sem ativo e vinculada depois.

- `GET /vulnerabilidades` → lista todas as vulnerabilidades
- `GET /vulnerabilidades/{id}` → mostra uma vulnerabilidade
- `POST /vulnerabilidades` → cadastra uma vulnerabilidade
- `PUT /vulnerabilidades/{id}` → atualiza uma vulnerabilidade inteira
- `PATCH /vulnerabilidades/{id}` → altera só alguns campos (ex.: vincular a um ativo com `{ "ativoId": 3 }`)
- `DELETE /vulnerabilidades/{id}` → remove uma vulnerabilidade
- `GET /ativos/{id}/vulnerabilidades` → lista as vulnerabilidades de um ativo

---

## 🫧 Códigos de status usados

- **200 OK** → deu certo (GET, PUT, PATCH, DELETE)
- **201 Created** → recurso criado (POST)
- **404 Not Found** → o recurso não existe

---

## ✨ Testes de integração (Postman)

Arquivo da coleção: `S3_18-API-Ativos.postman_collection.json`

### Como rodar
1. Ligar a API (ver **Como rodar** acima)
2. No Postman: **Import** → escolher o arquivo da coleção
3. Na coleção: **`...` → Run** → **Run S3_18 - API Ativos**

### O que cada request testa (na ordem)

1. **Listar ativos** → status 200 e resposta é uma lista não vazia
2. **Buscar ativo inexistente** → status 404 para `/ativos/999`
3. **Cadastrar ativo** → status 201, nome correto e presença do `id` (o `id` é guardado na variável `{{ativoId}}`)
4. **Buscar ativo cadastrado** → status 200 e o `id` é o do ativo recém-criado
5. **Substituir ativo** → status 200 e o responsável foi trocado
6. **Editar ativo** → status 200, `vulnerabilidadesAbertas` virou 0 e o nome continua o mesmo
7. **Deletar ativo** → status 200
8. **Confirmar remoção de ativo** → status 404 ao buscar o ativo apagado
9. **Listar vulnerabilidades de um ativo** → status 200 e todas pertencem ao ativo 4

Como o fluxo cria um ativo, edita e depois apaga, a coleção pode ser rodada várias vezes seguidas sem bagunçar o banco.

**Resultado:** 15 testes, 15 aprovados.