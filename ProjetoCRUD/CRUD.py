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

class BaseDados:
    def inserir(self):
        novo_aluno = input('Digite o primeiro nome do aluno: ')
        sobrenome_aluno = input('Digite o sobrenome do aluno: ')
        cpf_aluno = int(input('Digite o CPF do aluno (APENAS NUMEROS): '))
        curso_aluno = input('Digite o curso do aluno: ')
        comandoSQL = f'INSERT INTO aluno (nome_aluno, sobrenome_aluno, cpf_aluno, curso_aluno) ' \
                     f'VALUES ("{novo_aluno}", "{sobrenome_aluno}",{cpf_aluno},"{curso_aluno}")'
        cursor.execute(comandoSQL)
        conexao.commit()

    def consultas(self):
        menu_consultas = int(input(f'{"*" * 50}\n'
                                   f'Qual consulta gostaria de fazer?\n'
                                   f'1 - Consulta por ID\n'
                                   f'2 - Consulta pelo nome\n'
                                   f'3 - Consulta pelo sobrenome\n'
                                   f'4 - Consulta pelo curso\n'
                                   f'5 - Exibir todos os alunos\n'
                                   f'6 - Retornar ao menu inicial\n'
                                   f'{"*" * 50}\n'))
        match menu_consultas:
            case 1:
                idAluno = int(input('Digite o id do aluno para a consulta: '))
                comandoSQL = f'SELECT * FROM aluno WHERE id_aluno={idAluno}'
                cursor.execute(comandoSQL)
                resultadoConsulta = cursor.fetchall()
                df = pd.DataFrame(resultadoConsulta)
                print(f'{df}{"-"*50}\n')
            case 2:
                nome_aluno = input('Digite o nome do aluno para a consulta: ')
                comandoSQL = f'SELECT * FROM aluno WHERE nome_aluno="{nome_aluno}"'
                cursor.execute(comandoSQL)
                resultadoConsulta = cursor.fetchall()
                df = pd.DataFrame(resultadoConsulta)
                print(f'{df} \n')
            case 3:
                sobrenome_aluno = input('Digite o sobrenome do aluno para a consulta: ')
                comandoSQL = f'SELECT * FROM aluno WHERE sobrenome_aluno="{sobrenome_aluno}"'
                cursor.execute(comandoSQL)
                resultadoConsulta = cursor.fetchall()
                df = pd.DataFrame(resultadoConsulta)
                print(f'{df} \n')
            case 4:
                curso_aluno = input('Digite o nome curso que deseja consultar: ')
                comandoSQL = f'SELECT * FROM aluno WHERE curso_aluno="{curso_aluno}"'
                cursor.execute(comandoSQL)
                resultadoConsulta = cursor.fetchall()
                df = pd.DataFrame(resultadoConsulta)
                print(f'{df} \n')
            case 4:
                comandoSQL = f'SELECT * FROM aluno'
                cursor.execute(comandoSQL)
                resultadoDaConsulta = cursor.fetchall()
                df = pd.DataFrame(resultadoDaConsulta)
                print(f'{df} \n')
            case 5:
                self.menu()
            case _:
                print('Seleção inválida, tente novamente')

    def atualizacoes(self):
        menu_atualizacoes = int(input(f'{"*" * 50}\n'
                                      f'Qual consulta gostaria de fazer?\n'
                                      f'1 - Encontrar e atualizar pelo ID\n'
                                      f'2 - Encontrar e atualizar pelo nome\n'
                                      f'3 - Encontrar e atualizar pelo sobrenome\n'
                                      f'4 - Retornar ao menu inicial\n'
                                      f'{"*" * 50}\n'))
        match menu_atualizacoes:
            case 1:
                idAluno = int(input('Digite o ID do Aluno a ser atualizado: '))
                atualiza_aluno = input('Atualize o nome do aluno: ')
                atualiza_sobrenome = input('Atualize o sobrenome do aluno : ')
                atualiza_cpf = int(input('Digite o cpf (SOMENTE NUMEROS): '))
                atualiza_curso = input('Digite o curso do aluno: ')
                comandoSQL = f'UPDATE aluno set nome_aluno="{atualiza_aluno}", ' \
                             f'sobrenome_aluno="{atualiza_sobrenome}", cpf_aluno={atualiza_cpf}, ' \
                             f'curso_aluno="{atualiza_curso}" where id_aluno={idAluno}'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 2:
                nome_aluno = input('Digite o nome do Aluno a ser atualizado: ')
                atualiza_aluno = input('Atualize o nome do aluno: ')
                atualiza_sobrenome = input('Atualize o sobrenome do aluno : ')
                atualiza_cpf = int(input('Digite o cpf do aluno (SOMENTE NUMEROS): '))
                atualiza_curso = input('Digite o curso do aluno: ')
                comandoSQL = f'UPDATE aluno set nome_aluno="{atualiza_aluno}", ' \
                             f'sobrenome_aluno="{atualiza_sobrenome}", cpf_aluno={atualiza_cpf}, ' \
                             f'curso_aluno="{atualiza_curso}" where nome_aluno="{nome_aluno}"'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 3:
                sobrenome_aluno = input('Digite o sobrenome do aluno a ser atualizado: ')
                atualiza_aluno = input('Atualize o nome do aluno: ')
                atualiza_sobrenome = input('Atualize o sobrenome do aluno : ')
                atualiza_cpf = int(input('Digite o cpf (SOMENTE NUMEROS): '))
                atualiza_curso = input('Digite o curso do aluno: \n')
                comandoSQL = f'UPDATE aluno set nome_aluno="{atualiza_aluno}", ' \
                             f'sobrenome_aluno="{atualiza_sobrenome}", cpf_aluno={atualiza_cpf}, ' \
                             f'curso_aluno="{atualiza_curso}" where sobrenome_aluno="{sobrenome_aluno}"'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 4:
                self.menu()
            case _:
                print('Seleção inválida, tente novamente')

    def excluir(self):
        menu_excluir = int(input(f'{"*" * 50}\n'
                                 f'Você gostaria de remover/excluir através: \n'
                                 f'1 - Do ID do aluno\n'
                                 f'2 - Do nome do aluno\n'
                                 f'3 - Do sobrenome do aluno\n'
                                 f'4 - Retornar ao menu inicial\n'
                                 f'{"*" * 50}\n'))
        match menu_excluir:
            case 1:
                idAluno = int(input('Digite o ID do Aluno a ser excluido: '))
                comandoSQL = f'DELETE FROM aluno WHERE id_aluno = {idAluno}'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 2:
                nome_aluno = input('Digite o nome do aluno a ser excluido: ')
                comandoSQL = f'DELETE FROM aluno WHERE nome_aluno="{nome_aluno}"'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 3:
                sobrenome_aluno = input('Digite o sobrenome do aluno a ser excluido: ')
                comandoSQL = f'DELETE FROM aluno WHERE sobrenome_aluno="{sobrenome_aluno}"'
                cursor.execute(comandoSQL)
                conexao.commit()
            case 4:
                self.menu()
            case _:
                print('Seleção inválida, tente novamente')

    def menu(self):
        while True:
            menu = int(input(f'{"*" * 50}\n'
                             f'Utilize o menu através dos números: \n'
                             f'1 - Cadastrar aluno\n'
                             f'2 - Consultas\n'
                             f'3 - Atualizações cadastrais\n'
                             f'4 - Remoção / Exclusão\n'
                             f'5 - Sair do sistema\n'
                             f'{"*" * 50}\n'))
            match menu:
                case 1:
                    f'{"*" * 50}\n'
                    self.inserir()
                    print(f"Aluno cadastrado com Sucesso!\n"
                          f"{'*' * 50}")
                case 2:
                    print('*' * 50)
                    self.consultas()
                    print('*' * 50)
                case 3:
                    print('*' * 50)
                    self.atualizacoes()
                    print(f"Cadastrado atualizado com Sucesso!\n"
                          f"{'*' * 50}")
                case 4:
                    self.excluir()
                    print('*' * 50)
                    print('Excluido com sucesso!')
                    print('*' * 50)
                case 5:
                    print('Você saiu com Sucesso!')
                    print('*' * 50)
                    break
                case _:
                    print('Opção Inválida!')


executar = BaseDados()
executar.menu()