import requests
from bs4 import BeautifulSoup

class AdoroCinema:

    def extrairSinopseFilme (self, filme):      
        url = "https://www.adorocinema.com/filmes/" + filme +'/'
        htmlFilme = requests.get(url).text
        bsS = BeautifulSoup(htmlFilme, 'html.parser')
        sinopse = bsS.find('div', class_="content-txt").get_text(strip=True)
        return sinopse
    
    def salvarSinopseFilme(self, filme, sinopse):
        arq_saida = open(filme+'_sinopse.txt', 'w')
        for line in sinopse:
            arq_saida.write(line)
        arq_saida.close()

    def extrairComentariosFilme(self, filme, n):
        comentarios = []
        for i in range(1,n+1):
            url = 'http://www.adorocinema.com/filmes/' + filme + '/criticas/espectadores/?page=' + str(i)
            htmlComentarios = requests.get(url).text
            bsC = BeautifulSoup(htmlComentarios, 'html.parser')
            comentarios_com_tags = bsC.find_all('div', class_="content-txt review-card-content")
            for comentario_com_tag in comentarios_com_tags:
                comentarios.append(comentario_com_tag.get_text().strip())
        return comentarios

    def salvarComentariosFilme(self, filme, comentarios):
        arq_saida = open(filme+'_comentarios.txt', 'w')
        for comentario in comentarios:
            arq_saida.write(comentario + '\n\n')
        arq_saida.close()


filme = input('Digite o código do filme, conforme listado na barra de endereço do site https://www.adorocinema.com/: ')
n = int(input('Digite quantas páginas de comentários você deseja consultar: '))
crawler = AdoroCinema()
sinopse = crawler.extrairSinopseFilme(filme)
crawler.salvarSinopseFilme(filme, sinopse)
comentarios = crawler.extrairComentariosFilme(filme, n)
crawler.salvarComentariosFilme(filme, comentarios)
print('Programa executado com sucesso. Consulte os arquivos gerados com a sinopse e os comentários do filme.')