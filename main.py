import imaplib
from email import message_from_bytes

def login(email, senha, conexao):
    try:
        conexao.login(email, senha)
        print('Login sucesso!')

    except imaplib.IMAP4.error as e:
        print(f"Erro de login: {e}")

    except Exception as e:
        print('erro:', e)

def exibir_email(conexao):
    conexao.select('inbox')
    status, mensagem = conexao.search(None, 'ALL')

    ids = mensagem[0].split()
    id = ids[-5:]

    for num in id:
        status, dados = conexao.fetch(num, '(RFC822)')
        email_bruto = dados[0][1]
        msg = message_from_bytes(email_bruto)
        de = msg.get("From")
        assunto = msg.get("Subject")

        print(f'ID: {num}')
        print(f'De: {de}')
        print(f'Assunto: {assunto}')
        
        print()

def remover_email(conexao, id_email):
    conexao.copy(id_email, '[Gmail]/Trash')
    status, _ = conexao.store(id_email, '+FLAGS', '\\Deleted')
    if status == 'OK':
        conexao.expunge()
        print(f'E-mail {id_email} removido')
    else:
        print('Erro ao excluir o email')

def main():
    imap_server = "imap.gmail.com"
    conexao = imaplib.IMAP4_SSL(imap_server)
    usuario = 'jhonatacanevare6@gmail.com'
    senha = 'memmxpgemsxtjhnx'

    login(usuario, senha, conexao)

    exibir_email(conexao)

    remover_email(conexao, '9120')

main()