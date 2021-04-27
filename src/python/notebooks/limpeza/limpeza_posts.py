names_remover = [
    'recomendamos', 'contato', 'pesquisa-perfil-dos-leitores-do-blog',
    'india-folha-dicas-de-sobrevivencia',
    'google-oferece-wi-fi-gratis-nos-bares-do-brasil',
    'na-midia-nerd-na-puc-tv',
    'parceria-mondial-assistance', # comercial
    'estude-idiomas-e-fuja-do-silencio', # post patrocinado
    'quem-somos',
    'tripadvisor-top-25-hoteis', # Publicado em 2012 (temporal) e ainda irrelevante para levantamento de topicos, nao eh conteudo nosso
    'infraero-internet-gratuita-nos-aeroportos', # temporal, 2012
    'convite-exposicao-fotografica-parques-nacionais-americanos', # temporal, 2012
    'exposicao-fotografica-parques-nacionais-americanos', # temporal, 2012
    'trip-advisor-vistas-espetaculares-da-cama-do-hotel', # comercial e temporal
    'blogs-viajens', # referencia para outros blogs de viagens
    'tres-anos-de-nerds-viajantes', # temporal
    'relato-assalto-a-mao-armada-em-genipabu', # apoio a conhecidos
    'rbbv-rede-brasileira-de-blogueiros-de-viagem', # comercial
    'evento-workshop-argentina', # comercial e temporal
    'blog-action-day-the-power-of-we', # comercial
    'peru-um-pais-a-ser-explorado', # comercial, post patrocinado
    'belo-horizonte-feliz-115-anos', # post temporal
    'encontro-rede-brasileira-de-blogueiros-de-viagem', # temporal
    'acompanhe-todas-as-nossas-atualizacoes-pelo-facebook', # comercial
    'blogosfera-viajante-secreto', # temporal
    'um-ano-de-nerds-viajantes', # temporal
    'sorteio-album-de-fotos-o-segredo-do-vitorio', # comercial
    'sorteio-guia-essencial-gramado-e-canela', # comercial
    'sorteio-guia-miami-romero-britto', # comercial
    'sorteio-de-cape-town-a-muscat-uma-aventura-pela-africa', # comercial
    'sorteio-porta-retrato-lata-turista-chic', # comercial
    'visitando-aeroporto-viracopos', # temporal e comercial
    'concurso-assista-a-final-da-uefa-champions-league-em-wembley', # comercial
    'intrip-reserve-exeriencias-viagem', # outros blogs
    'nerd-na-globo-bom-dia-minas', # comercial
    'voando-com-a-azul-linhas-aereas', # comercial
    'estamos-de-volta', # post pessoal e sem conteudo a definir topico
    'adventure-bloggers-jalapao-eu-vou', # comercial e temporal
    'retrospectiva-2013', # temporal
    'dois-anos-de-nerds-viajantes', # temporal
    'concurso-cultural-viajar-e', # temporal e comercial
    'serra-cipo-fotos-pos-casamento', # pessoal
    'livro-guia-essencial-de-curitiba', # comercial
    'emirates-airlines-conectando-os-amantes-do-futebol', # comercial
    'na-midia-nerds-na-tv-horizonte', # comercial e temporal
    'dicas-capa-mala-trippy', # comercial
    'na-midia-programa-caleidoscopio-argentina', # temporal e comercial
    'desconto-no-seguro-de-viagem-outubro2015', # temporal e comercial
    'mondial-assistance-seguro-viagem-desconto', # comercial
    'quatro-anos-de-nerds-viajantes', # temporal
    'cinco-anos-de-nerds-viajantes', # temporal
    'fidelidade-livelo-acumular-pontos' # comercial
 ]

def remover_posts_especificos(posts):
    return posts[~posts['name'].isin(names_remover)]

def remover_papeis_parede(posts):
    # Verifica quem eh papel de parede
    papel_parede = posts['name'].str.startswith('papel-de-parede')

    # Verificar quantos papeis de parede ainda existem
    # (unique, counts) = np.unique(papel_parede, return_counts=True)
    # frequencies = np.asarray((unique, counts)).T

    # Verificamos que ainda haviam 60 papeis de parede mesmo apos remover os textos menores que 42
    # frequencies

    posts = posts[~papel_parede].reset_index(drop=True) 

    # Ha o caso em que o "name" comeca com "papel-parede"
    papel_parede = posts['name'].str.startswith('papel-parede')
    posts = posts[~papel_parede].reset_index(drop=True)

    return posts

# No notebook de exploracao eu explico porque o numero default 42.
def remover_posts_pequenos(posts, limite=42):
    posts['n_characters'] = posts['content'].str.len()
    posts.query("n_characters>=" + str(limite), inplace=True)

    return posts

def limpar_posts(posts,
    limpar_especificos = True,
    limpar_papel_parede = True,
    limpar_pequenos = True
):
    
    if limpar_especificos:
        posts = remover_posts_especificos(posts)

    if limpar_papel_parede:
        posts = remover_papeis_parede(posts)

    if limpar_pequenos:
        posts = remover_posts_pequenos(posts)

    return posts

if __name__ == "__main__":
    import pandas as pd
    posts = pd.DataFrame(data = {'name': ['Cerro Torre', 'Cerro Catedral'] })
    print(limpar_posts(posts))
