import requests

# def sCotacao_dolar():
#     sCotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#     sCotacoes = sCotacoes.json()
#     sCotacao_dolar = sCotacoes['USDBRL']["bid"]
#     return print("Cotação atual DOLAR: R$ {}".format(sCotacao_dolar))


# def sCEP(cep):
#     iValor = requests.get("https://cep.awesomeapi.com.br/json/{}" .format(cep))
#     iValor = iValor.json()
#     iRua = iValor["address"]
#     iBairro = iValor["district"]
#     iCidade = iValor["city"]
#     iEstado = iValor["state"]
#     return print("Rua {}, {}, {} - {}".format(iRua[4:], iBairro, iCidade, iEstado))

# sCotacao_dolar()
# sCEP("79823461")

# Documentação API: https://farmboxapi.docs.apiary.io/#introduction/authentication

# Token Homologação: mpQJEWcCIQLimILEdfxfoA
# URL Utilizada: http://test.farmbox.cc/api/v1/

# Token Produção: -ymOiFfKmf3lAYvG6-OjQg
# URL Utilizada: https://farmbox.cc/api/v1/ 


headers = {
  'Authorization': 'mpQJEWcCIQLimILEdfxfoA'
}

request = requests.get('http://test.farmbox.cc/api/v1/users')
request.headers[headers]
print(request)

