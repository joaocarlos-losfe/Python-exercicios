<h1>Teste Prático Python</h1>
<h2>1) Retornar as Meta tags de uma página</h2>
<p>
    getMetas(URL)
    Ex: getMetas(“https://enttry.com.br/contato”)
    Retorna um json com um array (com nome do meta e content) de metas extraídos do código
    html da página com endereço web passada por parâmetro em URL. (Meta tags são
    elementos no html utilizados para armazenar informações técnicas da página)
</p>

<h2>2) Retornar a temperatura atual de um CEP específico</h2>
<p>
    getTemperature (CEP)
    Ex: getTemperature (“95020-360”)
    Retorna a temperatura atual no local do CEP especificado
    Você pode utilizar mais de uma API ou webservice de CEP e previsão do tempo.
    Fique à vontade para escolher.
</p>

<h2>3) Salva um arquivo Excel (XLS) com a lista de links presentes em uma URL</h2>
<p>
    getLinks(URL, depth, fileName)
    Ex: getLinks(“https://enttry.com.br/contato”, 2, “linksEnttry.xls”)
    Descobre todos os links/urls contidos na página apontada por URL.
    Salva um arquivo Excel (XLS) com o nome passado em fileName
    Colunas do Excel a ser retornado: “link” (url absoluta do link),”atualTime”(hora que o link foi
    encontrado).
    Um link não deve ser inserido mais de uma vez na listagem.
    O parâmetro depth indica quantos níveis devemos descer na procura
    Ex: (0) Somente os links contidos na página URL, (1) Todos de URL e os que estão nas
    páginas que estão na lista de links de URL (2) Todos os anteriores e mais os que estão nas
    páginas abertas dos links anteriores.... E assim continua descendo a profundidade de
    acordo com o número informado.
</p>