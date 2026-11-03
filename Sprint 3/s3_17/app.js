// async function carregarAtivos() {
//     const resposta = await fetch("ativos.json");
//     const ativos = await resposta.json();
//     console.log(ativos);
// }

async function carregarAtivos() {
    const lista = document.getElementById("lista-ativos");
    try {
        const resposta = await fetch("ativos.json");
        if (!resposta.ok) {                                   // servidor respondeu com erro
            throw new Error(`Erro ${resposta.status} ao buscar os ativos`);
        }
        const ativos = await resposta.json();
        for (const ativo of ativos) {
            lista.innerHTML += `<div class="card">
            <h2>${ativo.nome}</h2>
            <p>
            <span>ID: ${ativo.id} |</span>
            <span>Responsável: ${ativo.responsavel}</span>
            </p>
            <p>
            <span>Setor: ${ativo.setor} |</span>
            <span>Vulnerabilidades Abertas: ${ativo.vulnerabilidadesAbertas}</span>
            </p>
            </div>`;
        }
    } catch (erro) {
        lista.innerHTML = `<p>Não foi possível carregar os ativos. ${erro.message}</p>`; // avisa na tela
    }
}

carregarAtivos();