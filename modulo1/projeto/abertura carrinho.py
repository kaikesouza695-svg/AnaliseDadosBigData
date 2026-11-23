#def possibiita a função para importar em outro arquivo py
#variavél ter o dicionaria
#fiz um dicionario  com as informações
#dei um retuno na primeira variável
#a primeira variável tem  len(serve pra contar a quantidade de elementos)
#e uma chave
#
#

def abrir_carrinho_difital(banco_dados, email_usuario,
nickname, assinatura_anual):
    id_pedido = len(banco_dados["assinaturas_transacoes"])
    + 2026001

    banco_dados["assinatura_transacoes"][id_pedido] = {
        "email_usuario": email_usuario,
        "nickname": nickname,
        "assinante_anual": assinatura_anual,
        "carrinho":[],
        "valor_bruto": 0.0,
        "valor_liquido": 0.0,
        "metodo_pagamento":  "pendente",
        "status": "ABERTO"
    }

    return id_pedido