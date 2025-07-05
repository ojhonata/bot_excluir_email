import imaplib
import email
import time

def login(email, senha, imap_server):
    try:
        conexao = imaplib.IMAP4_SSL(imap_server)
        conexao.login(email, senha)

        print('Login sucesso!')

    except imaplib.IMAP4.error as e:
        print(f"Erro de login: {e}")

    except Exception as e:
        print('erro:', e)

imap_server = "imap.gmail.com"
email = 'jhonatacanevare6@gmail.com'
senha = 'memm xpge msxt jhnx'

login(email, senha)