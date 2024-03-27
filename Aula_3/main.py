# Lista para armazenar as tarefas
tasks = []

# Função para adicionar uma tarefa à lista
def addTask():
  task = input("Por favor insira uma tarefa: ")  # Solicita ao usuário para inserir uma tarefa
  tasks.append(task)  # Adiciona a tarefa à lista
  print(f"Tarefa '{task}' adicionado à lista.")  # Confirmação de que a tarefa foi adicionada

# Função para listar as tarefas atualmente na lista
def listTasks():
  if not tasks:  # Verifica se a lista de tarefas está vazia
    print("Não há tarefas atualmente.")  # Se estiver vazia, informa que não há tarefas
  else:
    print("Tarefas Atuais:")  # Se houver tarefas, imprime o título
    for index, task in enumerate(tasks):  # Itera sobre as tarefas enumerando-as
      print(f"Tarefa #{index}. {task}")  # Imprime o índice e a tarefa

# Função para excluir uma tarefa da lista
def deleteTask():
  listTasks()  # Lista as tarefas atuais
  try:
    taskToDelete = int(input("Digite o # para excluir: "))  # Solicita ao usuário o número da tarefa a ser excluída
    if taskToDelete >= 0 and taskToDelete < len(tasks):  # Verifica se o número da tarefa está dentro dos limites da lista
      tasks.pop(taskToDelete)  # Remove a tarefa da lista
      print(f"Tarefa {taskToDelete} foi removido.")  # Confirmação de que a tarefa foi removida
    else:
      print(f"Tarefa#{taskToDelete} não foi encontrado.")  # Informa se a tarefa não foi encontrada
  except:
    print("Entrada inválida.")  # Trata exceções caso a entrada não seja um número

# Função principal que executa o aplicativo de lista de tarefas
if __name__ == "__main__":
  print("Bem-vindo ao aplicativo de lista de tarefas :")
  while True:  # Loop infinito para manter o programa em execução até que o usuário escolha sair
    print("\n")
    print("Por favor, selecione uma das seguintes opções")
    print("------------------------------------------")
    print("1. Adicione uma nova tarefa")
    print("2. Exclua uma tarefa")
    print("3. Listar tarefas")
    print("4. Desistir")

    choice = input("Digite sua escolha: ")  # Solicita ao usuário que escolha uma opção

    if (choice == "1"):  # Se a escolha for 1, chama a função para adicionar uma tarefa
      addTask()
    elif (choice == "2"):  # Se a escolha for 2, chama a função para excluir uma tarefa
      deleteTask()
    elif (choice == "3"):  # Se a escolha for 3, chama a função para listar as tarefas
      listTasks()
    elif (choice == "4"):  # Se a escolha for 4, sai do loop e encerra o programa
      break
    else:
      print("Entrada inválida. Por favor, tente novamente.")  # Mensagem de erro para escolhas inválidas

  print("Bye Bye!!")  # Mensagem de despedida quando o programa é encerrado
