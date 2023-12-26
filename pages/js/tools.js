function gerarArquivos() {
    const prefixo = document.getElementById('prefixInput').value;
    const token = document.getElementById('tokenInput').value;
    
    const arquivoPy = `# BIBLIOTECAS
import discord
from discord.ext import commands
import os
from colorama import Fore, Style

# CONFIGURAÇÃO DO BOT
prefixo = "${prefixo}" # PREFIX DO USUARIO
token = "${token}" # TOKEN DO USUARIO

# Restante do código...
`;

    const arquivoTxt = `Para adicionar esse arquivo .py, crie uma nova pasta e nomeie-a como preferir. Em seguida, dentro dessa pasta, crie outra chamada 'comandos'. Agora, simplesmente mova o arquivo .py para a pasta principal que você acabou de criar.

    📁 MinhaNovaPasta
       |
       └── 📁 comandos
       |      |
       |      └── comandos.py / ou subpastas
       |
       └── 📄 main.py`;

    download(arquivoPy, 'meu_bot.py', 'text/plain');
    download(arquivoTxt, 'instrucoes.txt', 'text/plain');
}

function download(texto, nomeArquivo, tipo) {
    var arquivo = new Blob([texto], { type: tipo });

    var a = document.createElement("a");
    var url = URL.createObjectURL(arquivo);
    a.href = url;
    a.download = nomeArquivo;
    document.body.appendChild(a);
    a.click();
    setTimeout(function() {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }, 0);
}
