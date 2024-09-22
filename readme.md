# Gupy Scrapper
Um scrapper feito com selenium que serve para entrar na página da gupy de algumas
empresas e verificar se há vagas do meu interesse.

## Para quê isso serve?
Eu costumo de tempos em tempos olhar a página gupy de uma certa empresa para ver se tem vagas 
novas que sejam do meu interesse porém a gupy tá longe de ser um bom portal para os candidatos, 
há poucas opções de filtragem e não é possível ordenar as vagas da mais recente para a mais antiga,
de modo que para saber se há vagas novas é preciso olhar todas e tentar lembrar quais vagas já estavam alí 
e quais não. Por causa disso criei esse scrapper para me mostrar de forma rápida se há ou não vagas do meu interesse.

## Como isso funciona?
Utilizando a biblioteca selenium, uma navegação automatizada é feita na página da empresa no portal gupy.
Primeiro, em uma aba do firefox, o scrapper clica no botão 'next' 15 vezes e então observa o número da última página.
É assim que o programa sabe quantas páginas há ao todo (infelizmente a gupy não nos dá um jeito fácil de saber quantas 
páginas existem ao todo, estamos contando com a sorte de que não existam mais do que 15).

Então a página é recarregada e o programa passa a copiar os nomes das vagas da página e a passar para a próxima até 
as páginas acabarem. Um arquivo json com as informações e a data do dia é salvo para consultas futuras e possíveis novas
features que penso em adicionar no futuro. Por fim é feita uma verificação baseada em palavras chave para verificar quais vagas
podem ser do meu interesse e estas são apresentadas no terminal.