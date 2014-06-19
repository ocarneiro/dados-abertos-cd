#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from suds.client import Client  #importa o cliente

#suds - consulta ao webservice
url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl'
client = Client(url, headers={'Content-Type': 'text/xml; charset=UTF-8'})
ano = 2013

def consulta() :
#print (client)
    resultado = client.service.ListarProposicoes(\
        sigla='MPV', numero=None, ano=ano, \
        datApresentacaoIni=None, datApresentacaoFim=None, \
        idTipoAutor=None, parteNomeAutor=None, \
        siglaPartidoAutor=None, siglaUFAutor=None, \
        generoAutor=None, \
        codEstado=None, codOrgaoEstado=None, \
        emTramitacao=1) 
    return resultado

#permite preservar as quebras de linha
def nl2br(value): 
     return value.replace('\n','<br>\n')
#jinja_env.filters['nl2br'] = nl2br

#dados utilizados pela página
app_data = {}

#aplicação
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    app_data['isso'] = 'aquilo'
    app_data['cliente'] = client
    resultado = consulta()
    app_data['tamanho'] = len(resultado['proposicoes']['proposicao'])
    return render_template('welcome.html', data=app_data)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
