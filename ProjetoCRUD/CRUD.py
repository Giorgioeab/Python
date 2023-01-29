import mysql.connector
import pandas as pd


# Conexão com servidor (atualmente local)
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='ProjetoCRUD'
)

cursor = conexao.cursor()


def inserir():
    novo_aluno = input('Digite o nome do aluno: ')
    cpf_aluno = int(input('Digite o CPF do aluno (APENAS NUMEROS)'))
    novo_curso = input('Digite o curso do aluno: ')
    comandoSQL = f'INSERT INTO aluno (nome_aluno, cpf_aluno, curso_aluno) values ("{novo_aluno}",{cpf_aluno},"{novo_curso}")'
    cursor.execute(comandoSQL)
    conexao.commit()


def consultarTodos():
    comandoSQL = f'SELECT * FROM aluno'
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    df = pd.DataFrame(resultadoDaConsulta)
    print(f'{df} \n')


def consultaAlunoPorID():
    idAluno = int(input('Digite o id do aluno para a consulta: '))
    comandoSQL = f'SELECT nome_aluno, curso_aluno FROM aluno WHERE id_aluno={idAluno}'
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    df = pd.DataFrame(resultadoDaConsulta)
    print(f'{df} \n')


def atualizar():
    idAluno = int(input('Digite o ID do Aluno a ser atualizado: '))
    atualiza_aluno = input('Atualize para o nome: ')
    atualiza_cpf = int(input('Digite o cpf: '))
    atualiza_curso = input('Digite o curso do aluno: \n')
    comandoSQL = f'UPDATE aluno set nome_aluno="{atualiza_aluno}", cpf_aluno={atualiza_cpf}, nome_curso="{atualiza_curso}" where id_aluno={idAluno}'
    cursor.execute(comandoSQL)
    conexao.commit()


def delete():
    idAluno = int(input('Digite o ID do Aluno a ser excluido: '))
    comandoSQL = f'DELETE FROM aluno where id_aluno = {idAluno}\n'
    cursor.execute(comandoSQL)
    conexao.commit()


while True:
    menu = int(input('Digite o que deseja fazer pelos numeros do menu abaixo: \n'
                     '1 - Cadastrar aluno\n'
                     '2 - Pesquisar todos os alunos\n'
                     '3 - Pesquisar por ID do aluno\n'
                     '4 - Atualizar cadastro\n'
                     '5 - Deletar aluno\n'
                     '6 - Sair do sistema\n'))
    match menu:
        case 1:
            inserir()
            print('-' *50)
        case 2:
            consultarTodos()
            print('-' *50)
        case 3:
            consultaAlunoPorID()
            print('-' *50)
        case 4:
            atualizar()
            print('-' *50)
        case 5:
            delete()
            print('-' *50)
        case 6:
            print('Você saiu com Sucesso!')
            print('-' * 50)
            break
        case _:
            print('Opção Inválida!')
