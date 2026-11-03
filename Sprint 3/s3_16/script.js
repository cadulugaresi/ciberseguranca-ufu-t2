const ativos = [
    { id: 1, nome: "Servidor Web", responsavel: "Cadu", setor: "TI", vulnerabilidadesAbertas: 3},
    { id: 2, nome: "Firewall", responsavel: "Henrique", setor: "Dados", vulnerabilidadesAbertas: 2},
    { id: 3, nome: "Impressora 3D", responsavel: "Felix", setor: "Segurança", vulnerabilidadesAbertas: 1},
    { id: 4, nome: "Banco de Dados", responsavel: "Marina", setor: "Dados", vulnerabilidadesAbertas: 4},
    { id: 5, nome: "Roteador Wi-Fi", responsavel: "Lucas", setor: "Infraestrutura", vulnerabilidadesAbertas: 0},
    { id: 6, nome: "Notebook Financeiro", responsavel: "Beatriz", setor: "Financeiro", vulnerabilidadesAbertas: 2},
];

const lista = document.getElementById("lista-ativos");

for (const ativo of ativos) {
    lista.innerHTML += `<div class="card">
    <h2>${ativo.nome}</h2>
    <p>ID: ${ativo.id}</p>
    <p>Responsável: ${ativo.responsavel}</p>
    </div>`;
    // console.log(`ID ${ativo.id} (${ativo.nome}) \n Responsável: ${ativo.responsavel}`);
}