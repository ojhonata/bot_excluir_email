import imaplib
#import email
import time

def login(email, senha, conexao):
    try:
        conexao.login(email, senha)
        print('Login sucesso!')

    except imaplib.IMAP4.error as e:
        print(f"Erro de login: {e}")

    except Exception as e:
        print('erro:', e)

def caixa_de_entreda(conexao):
    conexao.select('inbox')
    status, mensagem = conexao.search(None, 'BEFORE 01-jul-2024')

    if status == "OK":
        ids = mensagem[0].split()
        id = ids[-5:]
        print(id)

imap_server = "imap.gmail.com"
conexao = imaplib.IMAP4_SSL(imap_server)
email = 'jhonatacanevare6@gmail.com'
senha = 'memmxpgemsxtjhnx'

login(email, senha, conexao)

caixa_de_entreda(conexao)