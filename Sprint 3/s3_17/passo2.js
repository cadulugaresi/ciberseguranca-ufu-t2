const servidor = { nome: "Servidor Web", online: true, vulnerabilidades: 3 };
const roteador = { nome: "Roteador Wi-Fi", online: false, vulnerabilidades: 0 };

function consultarAtivo(ativo) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (ativo.online) {
                resolve(`${ativo.nome}: consulta concluída. Vulnerabilidades encontradas: ${ativo.vulnerabilidades}`);
            } else {
                reject(`${ativo.nome}: ativo fora do ar. Não foi possível consultar.`);
            }
        }, 1500);
    });
}

async function exibirConsulta(ativo) {
    try {
        const resultado = await consultarAtivo(ativo);
        console.log(resultado);
    } catch (erro) {
        console.log("ERRO →", erro);
    }
}

// async function NOME(PARAMETRO) {
//     try {
//         const resultado = await FUNCAO_QUE_DEVOLVE_PROMISE(PARAMETRO); // espera o resolve
//         // o que fazer com o resultado
//     } catch (erro) {
//         // o que fazer se der reject
//     }
// }

// consultarAtivo(servidor)
//     .then((resultado) => { console.log(`${resultado}`); })
//     .catch((erro) => { console.log("ERRO →", erro); });

// consultarAtivo(roteador)
//     .then((resultado) => { console.log(`${resultado}`); })
//     .catch((erro) => { console.log("ERRO →", erro); });

exibirConsulta(servidor);
exibirConsulta(roteador);