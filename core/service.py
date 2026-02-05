# core/service.py

import random
from core.moods import sentimentos


def get_resposta(sentimento):
    if sentimento in sentimentos:
        dados = sentimentos[sentimento]

        mensagem = random.choice(dados["mensagens"])

        return {
            "mensagem": mensagem,
            "sugestao": dados["sugestao"],
            "versiculo": dados["versiculo"]
        }

    return {
        "mensagem": "Não consegui identificar esse sentimento agora.",
        "sugestao": "Tente escolher uma das opções disponíveis.",
        "versiculo": ""
    }