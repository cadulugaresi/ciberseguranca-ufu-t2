# S4_15 — Docker: Conceitos Fundamentais e Containers

Roteiro executado com os comandos Docker essenciais, com as evidências de execução e a explicação da diferença entre imagem, container e volume.

**Aluno:** Cadu Lugaresi — Cibersegurança UFU, Turma 2
**Ambiente:** MacBook Air (Apple Silicon) com Docker Desktop v4.98.0

---

## ✨ 1. Verificar a instalação

```bash
docker --version
```

```
Docker version 29.9.2, build a82e528
```

## 🫧 2. Executar a imagem `hello-world`

```bash
docker run hello-world
```

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
58dee6a49ef1: Pull complete
c3bdf82c34d1: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```

Como a imagem não existia localmente, o Docker a baixou do Docker Hub, camada por camada (`Pull complete`), já na versão para o processador ARM do Mac (`arm64v8`). Em seguida, criou um container a partir dela, que imprimiu a mensagem e encerrou.

## ✨ 3. Container Python interativo

```bash
docker run -it --name meu-python python:3.12-slim bash
```

```
Unable to find image 'python:3.12-slim' locally
3.12-slim: Pulling from library/python
70b4f81c82dc: Pull complete
0373269344dc: Pull complete
acd43e9bebc3: Pull complete
0ba3a3e89cd9: Pull complete
cf4b30a54e0f: Download complete
bdec8a8ca49a: Download complete
Digest: sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b
Status: Downloaded newer image for python:3.12-slim
```

Comandos executados dentro do container:

```
root@09b26c71840d:/# ls /
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

root@09b26c71840d:/# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.7
ID=debian

root@09b26c71840d:/# python3 --version
Python 3.12.16

root@09b26c71840d:/# whoami
root

root@09b26c71840d:/# exit
```

- `-it` abre o container em modo interativo, com um terminal.
- O container roda **Debian Linux** mesmo estando num Mac: containers usam o kernel Linux, que o Docker Desktop fornece por meio de uma máquina virtual leve.
- O nome do host (`09b26c71840d`) é o ID do container.
- O processo roda como **root** por padrão, o que é um risco de segurança caso a aplicação seja comprometida.

## 🫧 4. Executar um container em segundo plano

```bash
docker run -d --name meu-servidor python:3.12-slim python3 -u -m http.server
```

```
4fcf1812b28d35cfbf28233bb414ae9182da91ac3d7a15742256304f47d959d5
```

`-d` executa o container em segundo plano e devolve o ID completo dele.

## ✨ 5. Listar containers em execução (`docker ps`)

```bash
docker ps
```

```
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS     NAMES
4fcf1812b28d   python:3.12-slim   "python3 -u -m http.…"   7 seconds ago   Up 6 seconds             meu-servidor
```

## 🫧 6. Consultar os logs (`docker logs`)

```bash
docker logs meu-servidor
```

```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

## ✨ 7. Executar um comando dentro do container (`docker exec`)

```bash
docker exec meu-servidor whoami
```

```
root
```

## 🫧 8. Parar o container (`docker stop`) e listar todos (`docker ps -a`)

```bash
docker stop meu-servidor
docker ps -a
```

```
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                       PORTS     NAMES
4fcf1812b28d   python:3.12-slim   "python3 -u -m http.…"   43 seconds ago   Exited (137) 2 seconds ago             meu-servidor
09b26c71840d   python:3.12-slim   "bash"                   5 minutes ago    Exited (0) 5 minutes ago               meu-python
b2ecfe0cd442   hello-world        "/hello"                 6 minutes ago    Exited (0) 6 minutes ago               sad_hypatia
```

- `docker ps -a` mostra também os containers parados.
- `Exited (0)` indica que o processo terminou normalmente.
- `Exited (137)` indica que o processo foi encerrado à força: o servidor não respondeu ao pedido de encerramento, e o Docker o finalizou após o tempo limite.
- `sad_hypatia` é um nome gerado automaticamente, porque o container do `hello-world` foi criado sem `--name`.

## ✨ 9. Iniciar novamente (`docker start`)

```bash
docker start meu-servidor
```

```
meu-servidor
```

## 🫧 10. Remover containers (`docker rm`)

Tentativa de remover um container em execução:

```bash
docker rm meu-servidor meu-python
```

```
meu-python
Error response from daemon: cannot remove container "meu-servidor": container is running: stop the container before removing or force remove
```

O Docker removeu o `meu-python`, que estava parado, mas se recusou a remover o `meu-servidor`, que estava em execução. Essa proteção evita que um container ativo seja apagado por engano.

Remoção correta, parando o container antes:

```bash
docker stop meu-servidor
docker rm meu-servidor sad_hypatia
docker ps -a
```

```
meu-servidor
sad_hypatia

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## ✨ 11. Imagens continuam após remover os containers (`docker images`)

```bash
docker images
```

```
IMAGE                ID             DISK USAGE   CONTENT SIZE
hello-world:latest   c567b231f656       22.6kB         10.3kB
python:3.12-slim     5e2bdb1b0d54        205MB         45.7MB
```

Todos os containers foram removidos, mas as imagens continuam armazenadas localmente e podem gerar novos containers sem um novo download.

---

## 🫧 Imagem, container e volume

**Imagem:** é um pacote somente leitura que contém o programa e tudo o que ele precisa para rodar: sistema base, interpretador e bibliotecas. Ela funciona como um modelo. A imagem `python:3.12-slim`, por exemplo, trouxe um Debian com o Python 3.12 já instalado, e continuou armazenada mesmo depois de todos os containers serem removidos (passo 11).

**Container:** é uma instância da imagem em execução, isolada do restante do sistema. Uma mesma imagem pode gerar vários containers independentes. Neste roteiro, a imagem `python:3.12-slim` deu origem a dois containers, `meu-python` e `meu-servidor`, cada um com o próprio ID e o próprio ciclo de vida (criado, executando, parado, removido).

**Volume:** é um espaço de armazenamento gerenciado pelo Docker que fica fora do container. Os arquivos criados dentro de um container são apagados quando ele é removido com `docker rm`. Já os dados gravados em um volume persistem e podem ser reutilizados por um novo container, o que é essencial para aplicações que guardam dados, como um banco SQLite.