import mysql.connector

def conectar_banco():

    try:
        conexao = mysql.connector.connect (
            host = 'localhost',
            database = 'cadastro',
            user = 'root',
            password = 'root',
        )
        print('conectado ao banco de daos')
        return conexao

    except Exception as erro: 
        print("erro ao conectar:[ERRO]")
        return None

def menu():
 print('1 cadastrar aluno')
 print('2 ver lista completa de alunos')
 print('3 localizar um aluno pelo id')
 print('4 atualizar apenas o telefone do aluno')
 print('5 excluir aluno do sistema')
 print('0 para sair')

def cadastrar(conexao):
    nome = input('Digite o nome do aluno: ')
    email = input('Digite o Email do aluno: ')
    telefone = (input('Entre com o telefone: '))

    try:
        cursor = conexao.cursor()
        sql = 'INSERT INTO aluno (nome,email,telefone) VALUES (%s,%s,%s)'
        dados = (nome, email, telefone)

        cursor.execute(sql, dados)
        conexao.commit()

        print('Aluno {nome} cadastrado com sucesso!')

    except Exception as erro:
        print("Erro ao cadastrar:", erro)


def listagem(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM aluno")
        registros = cursor.fetchall()

        if len(registros) == 0:
            print("Nenhum aluno cadastrado.")
            return

        print("\n LISTA DE aluno ")
        for aluno in registros:
            print(aluno)

    except Exception as erro:
        print("Erro ao listar aluno:", erro)


def buscarid(conexao):
    try:

            ID_Aluno = input('entre com o id do aluno')
            cursor = conexao.cursor()
            sql = "SELECT * FROM aluno WHERE id = %s"

            cursor.execute(sql, (ID_Aluno,))


            
            resultado = cursor.fetchone()

            if resultado:
                print('aluno encontrado')
                return
            else:
                print('nao encontrado')


    except Exception as erro:
        print("Erro ao buscar aluno:", erro)
    

def atualizartelefone(conexao):
    
 
    try:
        id_aluno = input("Digite o ID do aluno que deseja atualizar: ")
        novo_telefone = input("Digite o novo telefone: ")

        cursor = conexao.cursor()
        sql = "UPDATE aluno SET telefone = %s WHERE id = %s"
        dados = (novo_telefone, id_aluno)

        cursor.execute(sql, dados)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Telefone atualizado com sucesso!")
        else:
            print("Nenhum aluno encontrado com esse ID.")
    except Exception as erro:
        print("Erro ao atualizar telefone:", erro)

def excluiraluno(conexao):
    try:
        id_aluno = input("Digite o ID do aluno que deseja excluir: ")

        cursor = conexao.cursor()
        sql = "DELETE FROM aluno WHERE id = %s"
        cursor.execute(sql, (id_aluno,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Aluno excluído com sucesso!")
        else:
            print("Nenhum aluno encontrado com esse ID.")

    except Exception as erro:
        print("Erro ao excluir aluno:", erro)


while True:
  conexao = conectar_banco()
    
  menu()

  opcao = int(input('entre com os valores '))

  if opcao == 1:
    cadastrar(conexao)

  elif opcao == 2:
    listagem(conexao)

  elif opcao == 3:
    buscarid(conexao)

  elif opcao == 4:
    atualizartelefone(conexao)

  elif opcao == 5:
    excluiraluno(conexao)

  else:
    break
