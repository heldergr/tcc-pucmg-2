from repository.nerds_viajantes import read_published
from cleanning.limpeza_posts import remover_posts_especificos, remover_papeis_parede

if __name__ == "__main__":
    published = read_published()
    print("Shape inicial: ", published.shape)
    published = remover_posts_especificos(published)
    print("Shape apos de limpeza de posts: ", published.shape)
    published = remover_papeis_parede(published)
    print("Shape apos de remocao de papeis de parede: ", published.shape)
