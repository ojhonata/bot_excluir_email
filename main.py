import imaplib
from email import message_from_bytes
from email.header import decode_header

def login(usuario, senha, conexao):
    try:
        conexao.login(usuario, senha)
        print('Login sucesso!')

    except imaplib.IMAP4.error as e:
        print(f"Erro de login: {e}")

    except Exception as e:
        print('erro:', e)

def exibir_email(conexao, inicio):
    conexao.select('inbox')
    status, mensagem = conexao.search(None, 'ALL')

    ids = mensagem[0].split()
    ultimos_id = ids[0:inicio]

    for num in ultimos_id:
        status, dados = conexao.fetch(num, '(RFC822)')
        email_bruto = dados[0][1]
        msg = message_from_bytes(email_bruto)
        de = msg.get("From", "")
        assunto_bruto = msg.get("Subject", "")

        assunto, cod = decode_header(assunto_bruto)[0]
        if isinstance(assunto, bytes):
            assunto = assunto.decode(cod or 'utf-8', errors='ignore')

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
    usuario = input('Digite seu email: ')
    senha = input('Digite sua senha de aplicativo: ')

    login(usuario, senha, conexao)
    
    while True:
        opcao = input('1 - Listar emails\n2 - Excluir email\nDigite uma opção: ')
        if opcao == '1':
            inicio = int(input('Digite a quantidade de email para exibir: '))
            exibir_email(conexao, inicio)
        elif opcao == '2':
            remover_id = input('Digite apenas o número do id que deseja remover: ')
            remover_email(conexao, remover_id)
        else:
            print('Digite uma opção válida!')

        sair = input('Deseja sair [s]im ou [n]ão: ').lower().startswith('s')
        if sair:
            break

main()