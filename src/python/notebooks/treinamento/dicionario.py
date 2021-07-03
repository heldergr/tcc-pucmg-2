from gensim.corpora import Dictionary
# Documentacao Dictionary: https://radimrehurek.com/gensim/corpora/dictionary.html

default_dir = '/home/helder/estudos/tcc-pucmg-2/data'
default_filename = f'{default_dir}/dicionario.txt'

def criar(documentos):
    """
    Mapeamento de id para palavras
    id2word.token2id
    We can see word: word id pairs in this output.
    """
    return Dictionary(documentos)

def salvar_como_texto(dicionario, filename=default_filename):
    dicionario.save_as_text(filename)

def carregar_de_texto(filename=default_filename):
    return Dictionary.load_from_text(filename)