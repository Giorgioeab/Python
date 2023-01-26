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
    novo_curso = input('Digite o curso do aluno: ')
    comandoSQL = f'INSERT INTO aluno (nome_aluno, curso_aluno) values ("{novo_aluno}","{novo_curso}")'
    cursor.execute(comandoSQL)
    conexao.commit()


def consultarTodos():
    comandoSQL = f'SELECT * FROM aluno'
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    df = pd.DataFrame(resultadoDaConsulta)
    print(df)


def consultaAlunoPorID():
    idAluno = int(input('Digite o id do aluno para a consulta: '))
    comandoSQL = f'SELECT nome_aluno, curso_aluno FROM aluno WHERE id_aluno={idAluno}'
    cursor.execute(comandoSQL)
    resultadoDaConsulta = cursor.fetchall()
    df = pd.DataFrame(resultadoDaConsulta)
    print(df)

def atualizar():
    atualizaAluno = input('Atualize para o nome: ')
    idAluno = int(input('Digite o ID do Aluno a ser atualizado: '))
    comandoSQL = f'UPDATE aluno set nome_aluno="{atualizaAluno}" where id_aluno={idAluno}'
    cursor.execute(comandoSQL)
    conexao.commit()


def delete():
    idAluno = int(input('Digite o ID do Aluno a ser excluido: '))
    comandoSQL = f'DELETE FROM aluno where id_aluno = {idAluno}'
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
        case 2:
            consultarTodos()
        case 3:
            consultaAlunoPorID()
        case 4:
            atualizar()
        case 5:
            delete()
        case 6:
            print('Você saiu com Sucesso!')
            break
        case _:
            print('Opção Inválida!')
