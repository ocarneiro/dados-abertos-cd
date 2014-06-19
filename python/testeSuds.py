from suds.client import Client  #importa o cliente
#import pandas as pd

url = 'http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl'
client = Client(url, headers={'Content-Type': 'text/xml; charset=UTF-8'})

ano = 2013
#print (client)

resultado = client.service.ListarProposicoes(\
	sigla='MPV', numero=None, ano=ano, \
	datApresentacaoIni=None, datApresentacaoFim=None, \
	idTipoAutor=None, parteNomeAutor=None, \
	siglaPartidoAutor=None, siglaUFAutor=None, \
	generoAutor=None, \
	codEstado=None, codOrgaoEstado=None, \
	emTramitacao=1) 
print(str(ano) + ': ' + str(len(resultado['proposicoes']['proposicao'])))

props = resultado['proposicoes']['proposicao']

#---- Pandas ---
#urso = pd.Series(props)
#print(urso.head())
#---------------

for prop1 in props :
	situacao = prop1['situacao']
	descricao = situacao['descricao'] #.decode('utf8')
	print(str(situacao['id']) + ' = ' + descricao)

#print(props)
#print(type(urso))
